# tasks {#tasks}

机器人的任务。

| 方法 | 路径 | 调用者 | 说明 |
| --- | --- | --- | --- |
| GET | `/api/v1/tasks/` | 用户 | 列出任务（摘要）。 |
| POST | `/api/v1/tasks/` | 用户 | 创建任务。如果机器人已有任务在进行，返回 **409**。 |
| GET | `/api/v1/tasks/{uid}` | 用户 | 单个任务，含 `report` 和 `waypoints`。 |
| POST | `/api/v1/tasks/{uid}/cancel` | 操作员 | 取消等待中的任务，或请求停止进行中的任务。如果已结束，返回 **409**。 |
| GET | `/api/v1/tasks/timeline` | 操作员 | 某个组织在 `start` 和 `end` 之间的任务（最多 32 天）。 |
| GET | `/api/v1/tasks/operation` | 操作员 | 某个组织的机器人正在做什么：`active`、`queue` 和 `recent`。 |

*调用者* 的含义：见[简介](introduccion.md#who-can-call-each-endpoint)。

要启动机器人中已配置的任务，见 [devices](devices.md#start-a-task) 中的 `start-task`。不能通过 API 修改或删除任务。

## `status` 和 `type` {#status-and-type}

| 情况 | `status` 的值 |
| --- | --- |
| 等待中 | `Scheduled`、`Paused`（因工作流暂停） |
| 进行中 | `Running`、`executing` 或任何其他值 |
| 已结束 | `Completed`、`Failed` / `error`、`Cancelled` / `canceled` |

比较时不区分大小写。`type` 是自由文本（例如 `Delivery` 或 `Cleaning`）。

## 取消和停止 {#cancel-and-stop}

等待中的任务会立即变为 `Cancelled`。对于进行中的任务，只是 **请求** 机器人停止：`stop_requested_at` 表示请求时间；如果 30 秒后仍未执行，`stop_failed` 变为 `true`。

```json
{"uid": "22222222-2222-4222-8222-222222222222", "status": "Running", "stop_requested_at": "2026-11-24T10:00:00"}
```

!!! danger
    这不是紧急停止。

## `waiting_for` {#waiting_for}

任务到了开始时间却尚未开始的原因：`busy`、`offline`、`emergency`、`error`、`paused`、`charging`（其机器人）或 `connector`（其连接器有问题，未取走该任务）。

## 列表不含完整详情 {#lists-do-not-include-the-full-detail}

`GET /tasks/` 和 `GET /devices/{uid}/tasks` 不包含 `report` 和 `waypoints`：须单独请求该任务。

## `report` 和 `waypoints` {#report-and-waypoints}

`report` 没有固定结构：每个集成写入各自的键。不要假定某个字段始终存在。`waypoints` 是轨迹（如果机器人上报）。

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
