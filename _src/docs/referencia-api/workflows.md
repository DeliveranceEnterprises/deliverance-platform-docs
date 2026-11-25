# workflows

Automatizaciones y sus ejecuciones. Se trabaja siempre sobre la **organización del usuario**: un superusuario no llega a los workflows de las que cuelgan de ella. El concepto se explica en la [guía](../guia-de-uso/workflows.md).

| Método | Ruta | Quién | Descripción |
| --- | --- | --- | --- |
| GET | `/api/v1/workflows/` | Usuario | Lista los workflows. |
| POST | `/api/v1/workflows/` | Operador | Crea uno, desactivado. |
| GET | `/api/v1/workflows/{uid}` | Usuario | Un workflow. |
| PUT | `/api/v1/workflows/{uid}` | Operador | Lo modifica. **409** si está activo. |
| DELETE | `/api/v1/workflows/{uid}` | Operador | Lo elimina. **409** si está activo. |
| POST | `/api/v1/workflows/{uid}/enable` | Operador | Lo activa. **422** si tiene problemas. |
| POST | `/api/v1/workflows/{uid}/disable` | Operador | Lo desactiva. **409** si tiene tareas vivas. |
| GET | `/api/v1/workflows/catalog` | Operador | Lo que se puede usar en un workflow. |
| POST | `/api/v1/workflows/validate` | Operador | Comprueba un diagrama sin guardarlo. |
| GET | `/api/v1/workflows/runs` | Operador | Ejecuciones en curso y `next_starts`. |
| GET | `/api/v1/workflows/history` | Operador | Ejecuciones terminadas (`skip`, `limit` hasta 200). |
| GET | `/api/v1/workflows/timeline` | Operador | Ejecuciones entre `start` y `end` (32 días como máximo). |
| POST | `/api/v1/workflows/runs/{run_id}/pause` | Operador | Pausa. **409** si no está en curso. |
| POST | `/api/v1/workflows/runs/{run_id}/resume` | Operador | Reanuda. |
| POST | `/api/v1/workflows/runs/{run_id}/cancel` | Operador | Cancela. |

*Quién* puede llamar: ver la [introducción](introduccion.md#quien-puede-llamar-a-cada-endpoint).

Estados de una ejecución: `running`, `scheduled`, `waiting`, `paused` y `cancelling`. Resultados: `completed`, `failed`, `cancelled` y `not_started`.

## `data`: el diagrama

Lleva `"version": 3`, `nodes` (las cajas) y `edges` (las flechas).

```json
{
  "name": "Reparto a petición",
  "data": {
    "version": 3,
    "nodes": [
      {"id": "e1", "data": {"type": "event", "properties": {"triggerType": "button"}}},
      {"id": "t1", "data": {"type": "task", "properties": {"taskName": "Table 4", "robot": {"model": "T10"}}}}
    ],
    "edges": [{"source": "e1", "target": "t1"}]
  }
}
```

| Caja | Propiedades |
| --- | --- |
| `event` | Al menos una de `triggerType`, `userId` o `robot` (`{"uid"}` o `{"model"}`). Con `schedule`: `hours` (`["07:30"]`) y `days` (`["mon"]`, vacío = todos). |
| `condition` | `kind`: `event` (`field`, `operator`, `value`), `result` (`status`: `Completed`, `Failed` o `Cancelled`; justo tras una tarea) o `pending`. |
| `task` | `robot` (`{"uid"}`, `{"model"}` o `{"from": "event"}` / `{"from": "previous"}`), `rule` (`first_free` o `most_battery`, solo con modelo), `taskName`, `taskType`, `deadlineMinutes` (30 por defecto, 0 = sin plazo), `retry` (`max` 1–10, `waitMinutes` 0–1440). |

En las flechas que salen de una condición, `sourceHandle` es `yes` o `no`. No puede haber ciclos y, tras una tarea, solo condiciones `result`.

`triggerType` admite `schedule` y las clases de [events](events.md#clases-de-evento). Una clase que no exista no da error: nunca se dispara.

`POST /workflows/validate` responde `{"runnable": true, "problems": []}`; cada problema trae `code`, `message` y `box`.
