# kpis

Indicators for **this moment** and status history. For a period, see `metric-stats` in [organizations](organizations.md).

| Method | Path | Who | Description |
| --- | --- | --- | --- |
| GET | `/api/v1/organizations/{id}/kpis` | User | Current indicators. |
| GET | `/api/v1/devices/{uid}/status/history` | User | Status changes since `since` (`limit` 1–5000, 500 by default). Kept for about 35 days. |

*Who* can call: see the [introduction](introduccion.md#who-can-call-each-endpoint).

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

| Field | Meaning |
| --- | --- |
| `availability`, `utilization`, `operative` | Of the robots in service, at this moment |
| `compliance` | Today always `null`: it needs a planned time |
| `mtbf_hours` | Operating hours between faults, since `accumulated_since` |
| `mttr_hours` | Hours per repaired fault, since `accumulated_since` |
| `source` | `stored` (recorded recently) or `live` (calculated on request) |
