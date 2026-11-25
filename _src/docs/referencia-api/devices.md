# devices

Dispositivos, su estado, tareas, alarmas y lecturas.

| Método | Ruta | Quién | Descripción |
| --- | --- | --- | --- |
| GET | `/api/v1/devices/` | Usuario | Lista los dispositivos. |
| POST | `/api/v1/devices/` | Usuario | Crea un dispositivo en la organización del usuario. |
| GET | `/api/v1/devices/status` | Usuario | Estado de todos. |
| GET | `/api/v1/devices/{uid}/status` | Usuario | Estado de uno. |
| GET | `/api/v1/devices/{uid}/status/history` | Usuario | Histórico de estado (ver [kpis](kpis.md)). |
| GET | `/api/v1/devices/{uid}/snapshot` | Usuario | Imagen de una cámara. |
| GET | `/api/v1/devices/{id}` | Usuario | Un dispositivo. |
| PUT | `/api/v1/devices/{id}` | Usuario | Lo actualiza. |
| DELETE | `/api/v1/devices/{id}` | Superusuario | Lo elimina. **409** si ya tiene datos: hay que deshabilitarlo. |
| GET | `/api/v1/devices/own/{owner_id}` | Usuario | Los de una organización. |
| GET | `/api/v1/devices/{uid}/tasks` | Usuario | Tareas del dispositivo. |
| POST | `/api/v1/devices/{uid}/tasks` | Usuario | Crea una tarea. **409** si ya hay una en marcha. |
| GET | `/api/v1/devices/{uid}/task-catalog` | Operador | Tareas que se le pueden dar. |
| GET | `/api/v1/devices/{uid}/operation` | Operador | Lo que hace: `active`, `queue` y `recent`. |
| POST | `/api/v1/devices/{uid}/start-task` | Operador | Arranca una tarea por su nombre. |
| GET | `/api/v1/devices/{uid}/alarms` | Usuario | Alarmas. |
| POST | `/api/v1/devices/{uid}/alarms` | Usuario | Crea una alarma. |
| GET | `/api/v1/devices/{uid}/alarms/{alarm_id}` | Usuario | Una alarma. |
| PATCH | `/api/v1/devices/{uid}/alarms/{alarm_id}` | Usuario | La actualiza. |
| DELETE | `/api/v1/devices/{uid}/alarms/{alarm_id}` | Usuario | La elimina. |
| GET | `/api/v1/devices/{uid}/readings/{resolution}` | Usuario | Lecturas a esa resolución. |
| GET | `/api/v1/devices/{uid}/readings/{resolution}/{measure_type}` | Usuario | Lecturas de una magnitud. |
| GET | `/api/v1/devices/{uid}/meter-config` | Usuario | Nombres de los canales de un medidor. |
| PUT | `/api/v1/devices/{uid}/meter-config` | Usuario | Los sustituye: `{"channels": {"L1": "Cocina"}}`. |

*Quién* puede llamar: ver la [introducción](introduccion.md#quien-puede-llamar-a-cada-endpoint).

## Crear un dispositivo

Son obligatorios `name`, `model`, `category`, `serial_number` y `mac_address`. El propietario es siempre la organización del usuario y `enabled` es `false` por defecto.

```json
{
  "name": "Robot limpieza 04",
  "model": "X100",
  "category": "robot",
  "serial_number": "SN-00313",
  "mac_address": "AA:BB:CC:00:11:23"
}
```

La respuesta añade `uid` y `owner_id`.

## `category`

| `category` (API) | Se agrupa en el Dashboard como |
| --- | --- |
| `robot` | Robot |
| `sensor` (incluye las cámaras) | Sensor |
| `meter` | IoT |
| `hub` | IoT |

## `status`

| Valor | Significado |
| --- | --- |
| `running` | Haciendo su trabajo |
| `idle` | Encendido y libre |
| `charging` | Cargando |
| `paused` | Parado a propósito, puede continuar |
| `emergency` | Parada de emergencia |
| `error` | Avería |
| `offline` | Sin conexión |

El texto guardado puede venir con otras mayúsculas o con un valor propio del fabricante. `battery_level` es `null` en los dispositivos sin batería.

## Arrancar una tarea

`GET /devices/{uid}/task-catalog` devuelve `{"data": [{"name", "type"}], "count", "from_robot"}`. `from_robot` es `false` si el robot no comunica sus tareas y la lista son las que ha ejecutado últimamente.

`POST /devices/{uid}/start-task` con `{"name": "Table 4"}` crea una tarea `Scheduled`. Responde **409** si no es un robot habilitado y **422** si el robot no tiene esa tarea (el nombre debe ser exacto).

!!! warning
    Un robot real puede moverse.

## `snapshot`: imagen de una cámara

Devuelve `image` (data URL o `null`), `taken_at`, `error` y `unchanged`. Cada llamada pide imágenes nuevas, así que hay que repetirla cada pocos segundos; la primera puede no traer imagen. Con `known_taken_at` no se reenvía una imagen que ya se tiene. Responde 404 si no es una cámara.

## `readings`

`limit_data_points` (500 por defecto) limita los puntos. Sin lecturas responde 404. Valores habituales:

| `resolution` | Aplica a |
| --- | --- |
| `5min` | Medidores y sensores |
| `60min` | Medidores y sensores |
| `1day` | Medidores y sensores |

| Tipo de dispositivo | `measure_type` | Unidad |
| --- | --- | --- |
| Medidor | `energy` | Wh |
| Medidor | `power` | W |
| Medidor | `voltage` | V |
| Medidor | `current` | A |
| Medidor | `power_factor` | (sin unidad) |
| Medidor | `reactive_power` | VAr |
| Sensor | `temperature` | °C |
| Sensor | `humidity` | % |
| Sensor | `light` | lux |
| Sensor | `motion` | (sin unidad) |

## `alarms`

| Campo | Significado | Valores |
| --- | --- | --- |
| `device_uid` | El dispositivo | Obligatorio |
| `source` | Qué dato se vigila | `status`, `error_code`, `battery_level`, `reading`, `maintenance`, `last_connection` (minutos) |
| `operator` | Cómo se compara | `equals`, `lt`, `lte`, `gt`, `gte`, `present`, `absent` |
| `value` | El umbral | Un objeto: `{"threshold": 20}` |
| `extra` | Parámetros | `measure_type` y `endpoint_name` para `reading`; `key` para `maintenance` |
| `start_date` | Desde cuándo | Obligatorio |

`source` y `operator` no se validan: una alarma con un valor desconocido nunca salta.

```json
{
  "device_uid": "11111111-1111-4111-8111-111111111111",
  "name": "Batería baja",
  "source": "battery_level",
  "operator": "lt",
  "value": {"threshold": 20},
  "start_date": "2026-11-24T00:00:00"
}
```

Al saltar y al apagarse se registra un evento `alarm` o `alarm_cleared` (ver [events](events.md)).
