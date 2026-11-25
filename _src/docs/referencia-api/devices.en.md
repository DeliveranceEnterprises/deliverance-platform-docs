# devices

Devices, their status, tasks, alarms and readings.

| Method | Path | Who | Description |
| --- | --- | --- | --- |
| GET | `/api/v1/devices/` | User | Lists the devices. |
| POST | `/api/v1/devices/` | User | Creates a device in the user's organization. |
| GET | `/api/v1/devices/status` | User | Status of all of them. |
| GET | `/api/v1/devices/{uid}/status` | User | Status of one. |
| GET | `/api/v1/devices/{uid}/status/history` | User | Status history (see [kpis](kpis.md)). |
| GET | `/api/v1/devices/{uid}/snapshot` | User | Image from a camera. |
| GET | `/api/v1/devices/{id}` | User | One device. |
| PUT | `/api/v1/devices/{id}` | User | Updates it. |
| DELETE | `/api/v1/devices/{id}` | Superuser | Deletes it. **409** if it already has data: it must be disabled instead. |
| GET | `/api/v1/devices/own/{owner_id}` | User | Those of an organization. |
| GET | `/api/v1/devices/{uid}/tasks` | User | Tasks of the device. |
| POST | `/api/v1/devices/{uid}/tasks` | User | Creates a task. **409** if one is already running. |
| GET | `/api/v1/devices/{uid}/task-catalog` | Operator | Tasks it can be given. |
| GET | `/api/v1/devices/{uid}/operation` | Operator | What it is doing: `active`, `queue` and `recent`. |
| POST | `/api/v1/devices/{uid}/start-task` | Operator | Starts a task by its name. |
| GET | `/api/v1/devices/{uid}/alarms` | User | Alarms. |
| POST | `/api/v1/devices/{uid}/alarms` | User | Creates an alarm. |
| GET | `/api/v1/devices/{uid}/alarms/{alarm_id}` | User | One alarm. |
| PATCH | `/api/v1/devices/{uid}/alarms/{alarm_id}` | User | Updates it. |
| DELETE | `/api/v1/devices/{uid}/alarms/{alarm_id}` | User | Deletes it. |
| GET | `/api/v1/devices/{uid}/readings/{resolution}` | User | Readings at that resolution. |
| GET | `/api/v1/devices/{uid}/readings/{resolution}/{measure_type}` | User | Readings of one measure. |
| GET | `/api/v1/devices/{uid}/meter-config` | User | Names of a meter's channels. |
| PUT | `/api/v1/devices/{uid}/meter-config` | User | Replaces them: `{"channels": {"L1": "Kitchen"}}`. |

*Who* can call: see the [introduction](introduccion.md#who-can-call-each-endpoint).

## Create a device

`name`, `model`, `category`, `serial_number` and `mac_address` are required. The owner is always the user's organization, and `enabled` is `false` by default.

```json
{
  "name": "Cleaning robot 04",
  "model": "X100",
  "category": "robot",
  "serial_number": "SN-00313",
  "mac_address": "AA:BB:CC:00:11:23"
}
```

The response adds `uid` and `owner_id`.

## `category`

| `category` (API) | Grouped in the Dashboard as |
| --- | --- |
| `robot` | Robot |
| `sensor` (includes cameras) | Sensor |
| `meter` | IoT |
| `hub` | IoT |

## `status`

| Value | Meaning |
| --- | --- |
| `running` | Doing its job |
| `idle` | On and free |
| `charging` | Charging |
| `paused` | Stopped on purpose, can continue |
| `emergency` | Emergency stop |
| `error` | Fault |
| `offline` | No connection |

The stored text may come in a different case or with a value specific to the manufacturer. `battery_level` is `null` on devices without a battery.

## Start a task

`GET /devices/{uid}/task-catalog` returns `{"data": [{"name", "type"}], "count", "from_robot"}`. `from_robot` is `false` if the robot does not report its tasks and the list is the ones it has run lately.

`POST /devices/{uid}/start-task` with `{"name": "Table 4"}` creates a `Scheduled` task. It responds **409** if it is not an enabled robot and **422** if the robot does not have that task (the name must match exactly).

!!! warning
    A real robot may move.

## `snapshot`: image from a camera

Returns `image` (data URL or `null`), `taken_at`, `error` and `unchanged`. Each call requests new images, so it must be repeated every few seconds; the first one may bring no image. With `known_taken_at`, an image you already have is not sent again. It responds 404 if it is not a camera.

## `readings`

`limit_data_points` (500 by default) limits the points. With no readings it responds 404. Usual values:

| `resolution` | Applies to |
| --- | --- |
| `5min` | Meters and sensors |
| `60min` | Meters and sensors |
| `1day` | Meters and sensors |

| Device type | `measure_type` | Unit |
| --- | --- | --- |
| Meter | `energy` | Wh |
| Meter | `power` | W |
| Meter | `voltage` | V |
| Meter | `current` | A |
| Meter | `power_factor` | (no unit) |
| Meter | `reactive_power` | VAr |
| Sensor | `temperature` | °C |
| Sensor | `humidity` | % |
| Sensor | `light` | lux |
| Sensor | `motion` | (no unit) |

## `alarms`

| Field | Meaning | Values |
| --- | --- | --- |
| `device_uid` | The device | Required |
| `source` | Which data is watched | `status`, `error_code`, `battery_level`, `reading`, `maintenance`, `last_connection` (minutes) |
| `operator` | How it is compared | `equals`, `lt`, `lte`, `gt`, `gte`, `present`, `absent` |
| `value` | The threshold | An object: `{"threshold": 20}` |
| `extra` | Parameters | `measure_type` and `endpoint_name` for `reading`; `key` for `maintenance` |
| `start_date` | Since when | Required |

`source` and `operator` are not validated: an alarm with an unknown value never goes off.

```json
{
  "device_uid": "11111111-1111-4111-8111-111111111111",
  "name": "Low battery",
  "source": "battery_level",
  "operator": "lt",
  "value": {"threshold": 20},
  "start_date": "2026-11-24T00:00:00"
}
```

When it goes off and when it clears, an `alarm` or `alarm_cleared` event is recorded (see [events](events.md)).
