# kpis {#kpis}

**此刻**的指标和状态历史。如需某个时间段的数据，见 [organizations](organizations.md) 中的 `metric-stats`。

| 方法 | 路径 | 调用者 | 说明 |
| --- | --- | --- | --- |
| GET | `/api/v1/organizations/{id}/kpis` | 用户 | 当前指标。 |
| GET | `/api/v1/devices/{uid}/status/history` | 用户 | 自 `since` 起的状态变化（`limit` 1–5000，默认 500）。保留约 35 天。 |

*调用者* 的含义：见[简介](introduccion.md#who-can-call-each-endpoint)。

```json
{
  "t": "2026-11-24T10:00:00Z",
  "source": "stored",
  "accumulated_since": "2026-11-01T00:00:00Z",
  "robots": {"in_service": 3, "by_status": {"idle": 2, "charging": 1}},
  "availability": 100.0,
  "utilization": 0.0,
  "operative": 66.67,
  "compliance": null,
  "mtbf_hours": 120.5,
  "mttr_hours": 0.4
}
```

| 字段 | 含义 |
| --- | --- |
| `availability`、`utilization`、`operative` | 在役机器人此刻的数值 |
| `compliance` | 目前始终为 `null`：需要计划时间 |
| `mtbf_hours` | 自 `accumulated_since` 起，两次故障之间的可运行小时数 |
| `mttr_hours` | 自 `accumulated_since` 起，每次已修复故障的小时数 |
| `source` | `stored`（不久前记录）或 `live`（请求时计算） |
