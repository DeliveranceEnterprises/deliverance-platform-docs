# tasks {#tasks}

Tareas de los robots.

| Método | Ruta | Quién | Descripción |
| --- | --- | --- | --- |
| GET | `/api/v1/tasks/` | Usuario | Lista las tareas (resumidas). |
| POST | `/api/v1/tasks/` | Usuario | Crea una tarea. **409** si el robot ya tiene una en marcha. |
| GET | `/api/v1/tasks/{uid}` | Usuario | Una tarea, con `report` y `waypoints`. |
| POST | `/api/v1/tasks/{uid}/cancel` | Operador | Cancela una tarea en espera o pide parar una en marcha. **409** si ya terminó. |
| GET | `/api/v1/tasks/timeline` | Operador | Tareas de una organización entre `start` y `end` (32 días como máximo). |
| GET | `/api/v1/tasks/operation` | Operador | Lo que hacen los robots de una organización: `active`, `queue` y `recent`. |

*Quién* puede llamar: ver la [introducción](introduccion.md#who-can-call-each-endpoint).

Para arrancar una tarea configurada en un robot, ver `start-task` en [devices](devices.md#start-a-task). Las tareas no se modifican ni se borran por la API.

## `status` y `type` {#status-and-type}

| Situación | Valores de `status` |
| --- | --- |
| En espera | `Scheduled`, `Paused` (por un workflow en pausa) |
| En marcha | `Running`, `executing`, o cualquier otro |
| Terminada | `Completed`, `Failed` / `error`, `Cancelled` / `canceled` |

Compáralos sin distinguir mayúsculas. `type` es texto libre (por ejemplo `Delivery` o `Cleaning`).

## Cancelar y parar {#cancel-and-stop}

Una tarea en espera pasa a `Cancelled` al momento. Con una en marcha solo se **pide** al robot que pare: `stop_requested_at` indica cuándo y `stop_failed` pasa a `true` si 30 segundos después no se ha ejecutado.

```json
{"uid": "22222222-2222-4222-8222-222222222222", "status": "Running", "stop_requested_at": "2026-11-24T10:00:00"}
```

!!! danger
    No es una parada de emergencia.

## `waiting_for` {#waiting_for}

Por qué no ha empezado una tarea cuya hora ha llegado: `busy`, `offline`, `emergency`, `error`, `paused`, `charging` (su robot) o `connector` (un problema de su conector, que no la ha recogido).

## Los listados no traen el detalle completo {#lists-do-not-include-the-full-detail}

`GET /tasks/` y `GET /devices/{uid}/tasks` no incluyen `report` ni `waypoints`: hay que pedir la tarea individual.

## `report` y `waypoints` {#report-and-waypoints}

`report` no tiene una estructura fija: cada integración escribe sus propias claves. No asumas que un campo existe siempre. `waypoints` es la trayectoria, si el robot la comunica.

```json
{
  "uid": "22222222-2222-4222-8222-222222222222",
  "device_uid": "11111111-1111-4111-8111-111111111111",
  "task_name": "Ground floor cleaning",
  "type": "Cleaning",
  "status": "Completed",
  "start_time": "2026-11-18T09:00:00",
  "end_time": "2026-11-18T09:23:10",
  "report": {"duration": 1390, "distance": 245.3, "completed_percent": 98.4},
  "waypoints": [],
  "stop_requested_at": null,
  "stop_failed": false,
  "waiting_for": null
}
```
