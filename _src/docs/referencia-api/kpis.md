# kpis

Indicadores de **este momento** e histórico de estado. Para un periodo, ver `metric-stats` en [organizations](organizations.md).

| Método | Ruta | Quién | Descripción |
| --- | --- | --- | --- |
| GET | `/api/v1/organizations/{id}/kpis` | Usuario | Indicadores actuales. |
| GET | `/api/v1/devices/{uid}/status/history` | Usuario | Cambios de estado desde `since` (`limit` 1–5000, 500 por defecto). Se guardan unos 35 días. |

*Quién* puede llamar: ver la [introducción](introduccion.md#quien-puede-llamar-a-cada-endpoint).

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

| Campo | Significado |
| --- | --- |
| `availability`, `utilization`, `operative` | De los robots en servicio, en este momento |
| `compliance` | Hoy siempre `null`: necesita un tiempo planificado |
| `mtbf_hours` | Horas operativas entre averías, desde `accumulated_since` |
| `mttr_hours` | Horas por avería reparada, desde `accumulated_since` |
| `source` | `stored` (registrado hace poco) o `live` (calculado al pedirlo) |
