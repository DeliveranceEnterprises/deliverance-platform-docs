# events

Log of what happens. It is **read-only**: events cannot be created, modified or deleted through the API.

| Method | Path | Who | Description |
| --- | --- | --- | --- |
| GET | `/api/v1/events/` | User | Lists the events, from newest to oldest. |
| GET | `/api/v1/events/{uid}` | User | One event. |

*Who* can call: see the [introduction](introduccion.md#who-can-call-each-endpoint).

Filters: `organization_id` (by default, one's own, not including those below it), `event_type`, `device_uid`, `trigger_type` (repeatable), `since` (inclusive), `until` (exclusive), `skip` and `limit` (1–1000). They apply to `occurred_at`.

| Field | Meaning |
| --- | --- |
| `occurred_at` / `created_at` | When it happened / when it was recorded |
| `category` | `device`, `connector`, `workflow`, `activity` (user actions) or `system` |
| `actor_type`, `actor_id`, `actor_name` | Who: `user`, `integration` or `system` |
| `subject_type`, `subject_id`, `subject_name` | About what; the name is the one at that moment |
| `event_type` | `trigger` for what happens to devices; other values for activity (`create_user`, `workflow_enabled`...) |

## Event types

In a `trigger` event, `description.trigger_type` is:

| Group | Values |
| --- | --- |
| Tasks | `task_started`, `task_completed`, `task_failed`, `task_cancelled`, `task_expired`, `task_manual` |
| Robot | `robot_offline`, `robot_fault`, `robot_emergency`, `robot_charging`, `robot_recovered` (after 60 seconds in that state), `battery` |
| Alarms | `alarm`, `alarm_cleared` |
| Signals | `button`, `spill`, `shipping_order`, `camera_alarm` |
| Connectors | `connector_error` (`payload`: `stop`, `not_taken` or `no_data`), `connector_recovered` |

`description.late` means it was recorded late; such an event does not start workflows.

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
