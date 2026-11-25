# devices {#devices}

设备及其状态、任务、告警和读数。

| 方法 | 路径 | 调用者 | 说明 |
| --- | --- | --- | --- |
| GET | `/api/v1/devices/` | 用户 | 列出设备。 |
| POST | `/api/v1/devices/` | 用户 | 在用户的组织中创建设备。 |
| GET | `/api/v1/devices/status` | 用户 | 所有设备的状态。 |
| GET | `/api/v1/devices/{uid}/status` | 用户 | 单个设备的状态。 |
| GET | `/api/v1/devices/{uid}/status/history` | 用户 | 状态历史（见 [kpis](kpis.md)）。 |
| GET | `/api/v1/devices/{uid}/snapshot` | 用户 | 摄像头图像。 |
| GET | `/api/v1/devices/{id}` | 用户 | 单个设备。 |
| PUT | `/api/v1/devices/{id}` | 用户 | 更新设备。 |
| DELETE | `/api/v1/devices/{id}` | 超级用户 | 删除设备。如果已有数据则返回 **409**：须改为停用。 |
| GET | `/api/v1/devices/own/{owner_id}` | 用户 | 某个组织的设备。 |
| GET | `/api/v1/devices/{uid}/tasks` | 用户 | 设备的任务。 |
| POST | `/api/v1/devices/{uid}/tasks` | 用户 | 创建任务。如果已有任务在进行则返回 **409**。 |
| GET | `/api/v1/devices/{uid}/task-catalog` | 操作员 | 可以下达给该设备的任务。 |
| GET | `/api/v1/devices/{uid}/operation` | 操作员 | 设备正在做什么：`active`、`queue` 和 `recent`。 |
| POST | `/api/v1/devices/{uid}/start-task` | 操作员 | 按名称启动任务。 |
| GET | `/api/v1/devices/{uid}/alarms` | 用户 | 告警列表。 |
| POST | `/api/v1/devices/{uid}/alarms` | 用户 | 创建告警。 |
| GET | `/api/v1/devices/{uid}/alarms/{alarm_id}` | 用户 | 单个告警。 |
| PATCH | `/api/v1/devices/{uid}/alarms/{alarm_id}` | 用户 | 更新告警。 |
| DELETE | `/api/v1/devices/{uid}/alarms/{alarm_id}` | 用户 | 删除告警。 |
| GET | `/api/v1/devices/{uid}/readings/{resolution}` | 用户 | 该分辨率下的读数。 |
| GET | `/api/v1/devices/{uid}/readings/{resolution}/{measure_type}` | 用户 | 某个测量量的读数。 |
| GET | `/api/v1/devices/{uid}/meter-config` | 用户 | 电表各通道的名称。 |
| PUT | `/api/v1/devices/{uid}/meter-config` | 用户 | 替换通道名称：`{"channels": {"L1": "Kitchen"}}`。 |

*调用者* 的含义：见[简介](introduccion.md#who-can-call-each-endpoint)。

## 创建设备 {#create-a-device}

`name`、`model`、`category`、`serial_number` 和 `mac_address` 为必填。所有者始终是用户的组织，`enabled` 默认为 `false`。

```json
{
  "name": "Cleaning robot 04",
  "model": "X100",
  "category": "robot",
  "serial_number": "SN-00313",
  "mac_address": "AA:BB:CC:00:11:23"
}
```

响应会增加 `uid` 和 `owner_id`。

## `category` {#category}

| `category`（API） | 在仪表板（Dashboard）中的分组 |
| --- | --- |
| `robot` | 机器人（Robot） |
| `sensor`（包括摄像头） | 传感器（Sensor） |
| `meter` | 物联网（IoT） |
| `hub` | 物联网 |

## `status` {#status}

| 值 | 含义 |
| --- | --- |
| `running` | 正在工作 |
| `idle` | 已开机且空闲 |
| `charging` | 充电中 |
| `paused` | 被主动停住，可以继续 |
| `emergency` | 紧急停止 |
| `error` | 故障 |
| `offline` | 无连接 |

保存的文本可能大小写不同，或使用厂商自有的值。没有电池的设备，`battery_level` 为 `null`。

## 启动任务 {#start-a-task}

`GET /devices/{uid}/task-catalog` 返回 `{"data": [{"name", "type"}], "count", "from_robot"}`。如果机器人不上报其任务，列表为其最近执行过的任务，此时 `from_robot` 为 `false`。

`POST /devices/{uid}/start-task` 携带 `{"name": "Table 4"}` 会创建一个 `Scheduled` 任务。如果不是已启用的机器人，返回 **409**；如果机器人没有该任务，返回 **422**（名称必须完全一致）。

!!! warning
    真实的机器人可能会移动。

## `snapshot`：摄像头图像 {#snapshot-image-from-a-camera}

返回 `image`（data URL 或 `null`）、`taken_at`、`error` 和 `unchanged`。每次调用都会请求新图像，因此需每隔几秒重复调用；第一次可能没有图像。使用 `known_taken_at` 时，不会重新发送已有的图像。如果设备不是摄像头，返回 404。

## `readings` {#readings}

`limit_data_points`（默认 500）限制数据点数量。没有读数时返回 404。常见值：

| `resolution` | 适用于 |
| --- | --- |
| `5min` | 电表和传感器 |
| `60min` | 电表和传感器 |
| `1day` | 电表和传感器 |

| 设备类型 | `measure_type` | 单位 |
| --- | --- | --- |
| 电表 | `energy` | Wh |
| 电表 | `power` | W |
| 电表 | `voltage` | V |
| 电表 | `current` | A |
| 电表 | `power_factor` | （无单位） |
| 电表 | `reactive_power` | VAr |
| 传感器 | `temperature` | °C |
| 传感器 | `humidity` | % |
| 传感器 | `light` | lux |
| 传感器 | `motion` | （无单位） |

## `alarms` {#alarms}

| 字段 | 含义 | 值 |
| --- | --- | --- |
| `device_uid` | 设备 | 必填 |
| `source` | 监测哪项数据 | `status`、`error_code`、`battery_level`、`reading`、`maintenance`、`last_connection`（分钟） |
| `operator` | 如何比较 | `equals`、`lt`、`lte`、`gt`、`gte`、`present`、`absent` |
| `value` | 阈值 | 一个对象：`{"threshold": 20}` |
| `extra` | 参数 | `reading` 使用 `measure_type` 和 `endpoint_name`；`maintenance` 使用 `key` |
| `start_date` | 起始时间 | 必填 |

`source` 和 `operator` 不做校验：取值未知的告警永远不会触发。

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

触发和解除时会记录一个 `alarm` 或 `alarm_cleared` 事件（见 [events](events.md)）。
