# tasks

Robot tasks.

| Method | Path | Who | Description |
| --- | --- | --- | --- |
| GET | `/api/v1/tasks/` | User | Lists the tasks (summarized). |
| POST | `/api/v1/tasks/` | User | Creates a task. **409** if the robot already has one running. |
| GET | `/api/v1/tasks/{uid}` | User | One task, with `report` and `waypoints`. |
| POST | `/api/v1/tasks/{uid}/cancel` | Operator | Cancels a waiting task or requests to stop a running one. **409** if it has already finished. |
| GET | `/api/v1/tasks/timeline` | Operator | Tasks of an organization between `start` and `end` (32 days maximum). |
| GET | `/api/v1/tasks/operation` | Operator | What the robots of an organization are doing: `active`, `queue` and `recent`. |

*Who* can call: see the [introduction](introduccion.md#who-can-call-each-endpoint).

To start a task configured on a robot, see `start-task` in [devices](devices.md#start-a-task). Tasks cannot be modified or deleted through the API.

## `status` and `type`

| Situation | `status` values |
| --- | --- |
| Waiting | `Scheduled`, `Paused` (by a paused workflow) |
| Running | `Running`, `executing`, or any other |
| Finished | `Completed`, `Failed` / `error`, `Cancelled` / `canceled` |

Compare them case-insensitively. `type` is free text (for example `Delivery` or `Cleaning`).

## Cancel and stop

A waiting task becomes `Cancelled` immediately. With a running one, the robot is only **requested** to stop: `stop_requested_at` says when, and `stop_failed` becomes `true` if it has not been carried out 30 seconds later.

```json
{"uid": "22222222-2222-4222-8222-222222222222", "status": "Running", "stop_requested_at": "2026-11-24T10:00:00"}
```

!!! danger
    It is not an emergency stop.

## `waiting_for`

Why a task whose time has come has not started: `busy`, `offline`, `emergency`, `error`, `paused`, `charging` (its robot) or `connector` (a problem with its connector, which has not picked it up).

## Lists do not include the full detail

`GET /tasks/` and `GET /devices/{uid}/tasks` do not include `report` or `waypoints`: request the individual task.

## `report` and `waypoints`

`report` has no fixed structure: each integration writes its own keys. Do not assume that a field always exists. `waypoints` is the path travelled, if the robot reports it.

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
