# workflows

Automations and their runs. They always work on the **user's organization**: a superuser does not reach the workflows of the organizations below it. The concept is explained in the [guide](../guia-de-uso/workflows.md).

| Method | Path | Who | Description |
| --- | --- | --- | --- |
| GET | `/api/v1/workflows/` | User | Lists the workflows. |
| POST | `/api/v1/workflows/` | Operator | Creates one, disabled. |
| GET | `/api/v1/workflows/{uid}` | User | One workflow. |
| PUT | `/api/v1/workflows/{uid}` | Operator | Modifies it. **409** if it is enabled. |
| DELETE | `/api/v1/workflows/{uid}` | Operator | Deletes it. **409** if it is enabled. |
| POST | `/api/v1/workflows/{uid}/enable` | Operator | Enables it. **422** if it has problems. |
| POST | `/api/v1/workflows/{uid}/disable` | Operator | Disables it. **409** if it has live tasks. |
| GET | `/api/v1/workflows/catalog` | Operator | What can be used in a workflow. |
| POST | `/api/v1/workflows/validate` | Operator | Checks a diagram without saving it. |
| GET | `/api/v1/workflows/runs` | Operator | Runs in progress and `next_starts`. |
| GET | `/api/v1/workflows/history` | Operator | Finished runs (`skip`, `limit` up to 200). |
| GET | `/api/v1/workflows/timeline` | Operator | Runs between `start` and `end` (32 days maximum). |
| POST | `/api/v1/workflows/runs/{run_id}/pause` | Operator | Pauses. **409** if it is not in progress. |
| POST | `/api/v1/workflows/runs/{run_id}/resume` | Operator | Resumes. |
| POST | `/api/v1/workflows/runs/{run_id}/cancel` | Operator | Cancels. |

*Who* can call: see the [introduction](introduccion.md#who-can-call-each-endpoint).

Run states: `running`, `scheduled`, `waiting`, `paused` and `cancelling`. Results: `completed`, `failed`, `cancelled` and `not_started`.

## `data`: the diagram

It contains `"version": 3`, `nodes` (the boxes) and `edges` (the arrows).

```json
{
  "name": "Delivery on request",
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

| Box | Properties |
| --- | --- |
| `event` | At least one of `triggerType`, `userId` or `robot` (`{"uid"}` or `{"model"}`). With `schedule`: `hours` (`["07:30"]`) and `days` (`["mon"]`, empty = all). |
| `condition` | `kind`: `event` (`field`, `operator`, `value`), `result` (`status`: `Completed`, `Failed` or `Cancelled`; right after a task) or `pending`. |
| `task` | `robot` (`{"uid"}`, `{"model"}` or `{"from": "event"}` / `{"from": "previous"}`), `rule` (`first_free` or `most_battery`, only with a model), `taskName`, `taskType`, `deadlineMinutes` (30 by default, 0 = no deadline), `retry` (`max` 1–10, `waitMinutes` 0–1440). |

On arrows leaving a condition, `sourceHandle` is `yes` or `no`. There can be no cycles and, after a task, only `result` conditions.

`triggerType` accepts `schedule` and the types in [events](events.md#event-types). A type that does not exist gives no error: it never fires.

`POST /workflows/validate` responds `{"runnable": true, "problems": []}`; each problem carries `code`, `message` and `box`.
