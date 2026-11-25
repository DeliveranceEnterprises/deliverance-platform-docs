# events {#events}

所发生事情的记录。**只读**：不能通过 API 创建、修改或删除事件。

| 方法 | 路径 | 调用者 | 说明 |
| --- | --- | --- | --- |
| GET | `/api/v1/events/` | 用户 | 列出事件，从最新到最旧。 |
| GET | `/api/v1/events/{uid}` | 用户 | 单个事件。 |

*调用者* 的含义：见[简介](introduccion.md#who-can-call-each-endpoint)。

筛选条件：`organization_id`（默认为自己的组织，不包括下级组织）、`event_type`、`device_uid`、`trigger_type`（可重复）、`since`（包含）、`until`（不包含）、`skip` 和 `limit`（1–1000）。筛选作用于 `occurred_at`。

| 字段 | 含义 |
| --- | --- |
| `occurred_at` / `created_at` | 发生时间 / 记录时间 |
| `category` | `device`、`connector`、`workflow`、`activity`（用户操作）或 `system` |
| `actor_type`、`actor_id`、`actor_name` | 执行者：`user`、`integration` 或 `system` |
| `subject_type`、`subject_id`、`subject_name` | 对象；名称为当时的名称 |
| `event_type` | 设备上发生的事情为 `trigger`；用户活动为其他值（`create_user`、`workflow_enabled`...） |

## 事件类型 {#event-types}

在 `trigger` 事件中，`description.trigger_type` 为：

| 分组 | 值 |
| --- | --- |
| 任务 | `task_started`、`task_completed`、`task_failed`、`task_cancelled`、`task_expired`、`task_manual` |
| 机器人 | `robot_offline`、`robot_fault`、`robot_emergency`、`robot_charging`、`robot_recovered`（处于该状态 60 秒后）、`battery` |
| 告警 | `alarm`、`alarm_cleared` |
| 信号 | `button`、`spill`、`shipping_order`、`camera_alarm` |
| 连接器 | `connector_error`（`payload`：`stop`、`not_taken` 或 `no_data`）、`connector_recovered` |

`description.late` 表示该事件记录有延迟；此类事件不会启动工作流。

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
