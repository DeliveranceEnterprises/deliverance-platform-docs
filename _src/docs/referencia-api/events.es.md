# events {#events}

Registro de lo que ocurre. Es de **solo lectura**: los eventos no se crean, modifican ni borran por la API.

| Método | Ruta | Quién | Descripción |
| --- | --- | --- | --- |
| GET | `/api/v1/events/` | Usuario | Lista los eventos, del más reciente al más antiguo. |
| GET | `/api/v1/events/{uid}` | Usuario | Un evento. |

*Quién* puede llamar: ver la [introducción](introduccion.md#who-can-call-each-endpoint).

Filtros: `organization_id` (por defecto, la propia, sin incluir las que cuelgan de ella), `event_type`, `device_uid`, `trigger_type` (repetible), `since` (incluido), `until` (excluido), `skip` y `limit` (1–1000). Se aplican sobre `occurred_at`.

| Campo | Significado |
| --- | --- |
| `occurred_at` / `created_at` | Cuándo ocurrió / cuándo se registró |
| `category` | `device`, `connector`, `workflow`, `activity` (acciones de usuarios) o `system` |
| `actor_type`, `actor_id`, `actor_name` | Quién: `user`, `integration` o `system` |
| `subject_type`, `subject_id`, `subject_name` | Sobre qué; el nombre es el de aquel momento |
| `event_type` | `trigger` para lo que ocurre a los dispositivos; otros valores para la actividad (`create_user`, `workflow_enabled`...) |

## Clases de evento {#event-types}

En un evento `trigger`, `description.trigger_type` es:

| Grupo | Valores |
| --- | --- |
| Tareas | `task_started`, `task_completed`, `task_failed`, `task_cancelled`, `task_expired`, `task_manual` |
| Robot | `robot_offline`, `robot_fault`, `robot_emergency`, `robot_charging`, `robot_recovered` (tras 60 segundos en ese estado), `battery` |
| Alarmas | `alarm`, `alarm_cleared` |
| Señales | `button`, `spill`, `shipping_order`, `camera_alarm` |
| Conectores | `connector_error` (`payload`: `stop`, `not_taken` o `no_data`), `connector_recovered` |

`description.late` indica que se registró con retraso; un evento así no arranca workflows.

```json
{
  "data": [{
    "uid": "33333333-3333-4333-8333-333333333333",
    "event_type": "trigger",
    "priority": "info",
    "organization_id": "00000000-0000-4000-8000-000000000001",
    "description": {"trigger_type": "battery", "payload": "18", "device_uid": "11111111-1111-4111-8111-111111111111"},
    "occurred_at": "2026-11-24T10:00:00Z",
    "created_at": "2026-11-24T10:00:02Z",
    "category": "device",
    "actor_type": "system",
    "subject_type": "device",
    "subject_id": "11111111-1111-4111-8111-111111111111",
    "subject_name": "Robot 01"
  }],
  "count": 1
}
```
