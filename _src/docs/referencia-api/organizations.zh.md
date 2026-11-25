# organizations {#organizations}

组织及其层级、指标和报告。

| 方法 | 路径 | 调用者 | 说明 |
| --- | --- | --- | --- |
| GET | `/api/v1/organizations/` | 用户 | 列出可访问的组织。 |
| POST | `/api/v1/organizations/` | 超级用户 | 创建组织。 |
| GET | `/api/v1/organizations/{id}` | 用户 | 单个组织。 |
| PUT | `/api/v1/organizations/{id}` | 用户 | 更新组织。只有超级用户可以更改上级组织。 |
| DELETE | `/api/v1/organizations/{id}` | 超级用户 | 删除组织。绝不能删除自己的组织。 |
| GET | `/api/v1/organizations/{id}/child` | 用户 | 直接下级组织（一级）。 |
| GET | `/api/v1/organizations/{id}/devices` | 用户 | 设备及其状态。 |
| GET | `/api/v1/organizations/{id}/scenes` | 用户 | 场景。 |
| GET | `/api/v1/organizations/{id}/task-stats` | 用户 | 自 `start_date` 起（至 `end_date` 或当前）的任务。 |
| GET | `/api/v1/organizations/{id}/metric-stats` | 用户 | 该时间段的指标，不含明细。 |
| GET | `/api/v1/organizations/{id}/metrics` | 用户 | 该时间段的指标，按设备列出。 |
| POST | `/api/v1/organizations/{id}/send-report` | 用户 | 将 PDF 报告发送到调用者的邮箱。如果未配置邮件，返回 503。 |
| GET | `/api/v1/organizations/{id}/image` | 用户 | 徽标。 |
| POST | `/api/v1/organizations/{id}/image` | 用户 | 上传徽标（`multipart`，最大 10 MB）。 |
| DELETE | `/api/v1/organizations/{id}/image` | 用户 | 删除徽标。 |

*调用者* 的含义：见[简介](introduccion.md#who-can-call-each-endpoint)。

另见 [kpis](kpis.md)、[settings](settings.md)、[robot-maps](robot-maps.md) 和 [subscriptions](subscriptions.md)。

## `metrics` 和 `metric-stats` {#metrics-and-metric-stats}

两者都需要 `start_date` 和 `end_date`（`YYYY-MM-DD`，按 UTC 日期）。`metrics` 增加明细 `per_device`。只统计机器人；连续 7 天无连接的机器人视为停用。

| 指标 | 计算方式 |
| --- | --- |
| `compliance_percentage` | 已结束任务的平均完成度（失败和过期的任务计 0；已取消的任务不计入）。 |
| `utilization_percentage` | 工作时间占可用且未充电时间的比例。 |
| `availability_percentage` | 未离线、未故障、未停止的时间占总时间的比例。 |
| `operative_percentage` | 工作或空闲时间占总时间的比例。 |

没有数据时，任何一项都可能为 `null`。`metric-stats` 还包括按结果统计的任务、`total_devices`、`out_of_service_devices`、`period_start`、`period_end`、`updated_at` 以及各累加项（`working_seconds`、`usable_seconds`、`available_seconds`、`operative_seconds`、`total_seconds`、`completion_sum`）。

要合并多个组织，**请将秒数相加**；不要对百分比求平均。在 `metrics` 中，`cleaning_hours` 是工作小时数，与机器人类型无关。

## 其他字段 {#other-fields}

| 字段 | 含义 |
| --- | --- |
| `parent_id` | 上级组织。根组织中指向自身。 |
| `report_enabled` | 是否启用报告邮件。 |
| `report_frequency` | 包含 `daily`、`weekly` 和/或 `monthly` 的列表。 |

## 层级和权限 {#hierarchy-and-permissions}

**超级用户** 管理其组织及其下的整个分支。**普通用户** 只能看到自己的组织。

## 示例：创建组织 {#example-create-an-organization}

```json
{
  "name": "North Site",
  "parent_id": "00000000-0000-4000-8000-000000000001",
  "report_enabled": true,
  "report_frequency": ["weekly"]
}
```

响应会增加 `uid`。
