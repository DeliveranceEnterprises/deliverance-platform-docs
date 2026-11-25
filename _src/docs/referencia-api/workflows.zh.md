# workflows {#workflows}

自动化流程及其执行。操作范围始终是 **用户的组织**：超级用户无法访问下级组织的工作流。概念说明见[指南](../guia-de-uso/workflows.md)。

| 方法 | 路径 | 调用者 | 说明 |
| --- | --- | --- | --- |
| GET | `/api/v1/workflows/` | 用户 | 列出工作流。 |
| POST | `/api/v1/workflows/` | 操作员 | 创建工作流，初始为停用。 |
| GET | `/api/v1/workflows/{uid}` | 用户 | 单个工作流。 |
| PUT | `/api/v1/workflows/{uid}` | 操作员 | 修改工作流。如果已启用，返回 **409**。 |
| DELETE | `/api/v1/workflows/{uid}` | 操作员 | 删除工作流。如果已启用，返回 **409**。 |
| POST | `/api/v1/workflows/{uid}/enable` | 操作员 | 启用工作流。如果有问题，返回 **422**。 |
| POST | `/api/v1/workflows/{uid}/disable` | 操作员 | 停用工作流。如果有未结束的任务，返回 **409**。 |
| GET | `/api/v1/workflows/catalog` | 操作员 | 工作流中可以使用的内容。 |
| POST | `/api/v1/workflows/validate` | 操作员 | 检查流程图，不保存。 |
| GET | `/api/v1/workflows/runs` | 操作员 | 进行中的执行和 `next_starts`。 |
| GET | `/api/v1/workflows/history` | 操作员 | 已结束的执行（`skip`，`limit` 最大 200）。 |
| GET | `/api/v1/workflows/timeline` | 操作员 | `start` 和 `end` 之间的执行（最多 32 天）。 |
| POST | `/api/v1/workflows/runs/{run_id}/pause` | 操作员 | 暂停。如果不在进行中，返回 **409**。 |
| POST | `/api/v1/workflows/runs/{run_id}/resume` | 操作员 | 继续。 |
| POST | `/api/v1/workflows/runs/{run_id}/cancel` | 操作员 | 取消。 |

*调用者* 的含义：见[简介](introduccion.md#who-can-call-each-endpoint)。

执行的状态：`running`、`scheduled`、`waiting`、`paused` 和 `cancelling`。结果：`completed`、`failed`、`cancelled` 和 `not_started`。

## `data`：流程图 {#data-the-diagram}

包含 `"version": 3`、`nodes`（方框）和 `edges`（箭头）。

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

| 方框 | 属性 |
| --- | --- |
| `event` | `triggerType`、`userId` 或 `robot`（`{"uid"}` 或 `{"model"}`）中至少一项。使用 `schedule` 时：`hours`（`["07:30"]`）和 `days`（`["mon"]`，空 = 每天）。 |
| `condition` | `kind`：`event`（`field`、`operator`、`value`）、`result`（`status`：`Completed`、`Failed` 或 `Cancelled`；紧接在任务之后）或 `pending`。 |
| `task` | `robot`（`{"uid"}`、`{"model"}` 或 `{"from": "event"}` / `{"from": "previous"}`）、`rule`（`first_free` 或 `most_battery`，仅用于指定型号时）、`taskName`、`taskType`、`deadlineMinutes`（默认 30，0 = 无期限）、`retry`（`max` 1–10，`waitMinutes` 0–1440）。 |

从条件引出的箭头中，`sourceHandle` 为 `yes` 或 `no`。不能有循环；任务之后只能接 `result` 条件。

`triggerType` 可取 `schedule` 和 [events](events.md#event-types) 中的类型。不存在的类型不会报错：它永远不会触发。

`POST /workflows/validate` 返回 `{"runnable": true, "problems": []}`；每个问题包含 `code`、`message` 和 `box`。
