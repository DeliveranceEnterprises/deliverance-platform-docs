# organizations

Organizaciones, su jerarquía, sus métricas y sus informes.

| Método | Ruta | Quién | Descripción |
| --- | --- | --- | --- |
| GET | `/api/v1/organizations/` | Usuario | Lista las organizaciones a su alcance. |
| POST | `/api/v1/organizations/` | Superusuario | Crea una organización. |
| GET | `/api/v1/organizations/{id}` | Usuario | Una organización. |
| PUT | `/api/v1/organizations/{id}` | Usuario | La actualiza. Solo un superusuario cambia el padre. |
| DELETE | `/api/v1/organizations/{id}` | Superusuario | La elimina. Nunca la propia. |
| GET | `/api/v1/organizations/{id}/child` | Usuario | Hijas directas (un nivel). |
| GET | `/api/v1/organizations/{id}/devices` | Usuario | Dispositivos, con su estado. |
| GET | `/api/v1/organizations/{id}/scenes` | Usuario | Escenas. |
| GET | `/api/v1/organizations/{id}/task-stats` | Usuario | Tareas desde `start_date` (hasta `end_date` o ahora). |
| GET | `/api/v1/organizations/{id}/metric-stats` | Usuario | Métricas del periodo, sin desglose. |
| GET | `/api/v1/organizations/{id}/metrics` | Usuario | Métricas del periodo, por dispositivo. |
| POST | `/api/v1/organizations/{id}/send-report` | Usuario | Envía el informe en PDF al email de quien llama. 503 si no hay email configurado. |
| GET | `/api/v1/organizations/{id}/image` | Usuario | Logo. |
| POST | `/api/v1/organizations/{id}/image` | Usuario | Sube el logo (`multipart`, máximo 10 MB). |
| DELETE | `/api/v1/organizations/{id}/image` | Usuario | Elimina el logo. |

*Quién* puede llamar: ver la [introducción](introduccion.md#quien-puede-llamar-a-cada-endpoint).

Ver también [kpis](kpis.md), [settings](settings.md), [robot-maps](robot-maps.md) y [subscriptions](subscriptions.md).

## `metrics` y `metric-stats`

Ambos requieren `start_date` y `end_date` (`YYYY-MM-DD`, días en UTC). `metrics` añade el desglose `per_device`. Solo cuentan los robots; uno sin conexión durante 7 días está fuera de servicio.

| Métrica | Cómo se calcula |
| --- | --- |
| `compliance_percentage` | Media de lo completado en las tareas terminadas (fallidas y caducadas, 0; canceladas, fuera). |
| `utilization_percentage` | Tiempo trabajando sobre el tiempo disponible y sin cargar. |
| `availability_percentage` | Tiempo no desconectado, averiado ni parado, sobre el total. |
| `operative_percentage` | Tiempo trabajando o libre, sobre el total. |

Cualquiera puede ser `null` si no hay datos. `metric-stats` incluye además las tareas por resultado, `total_devices`, `out_of_service_devices`, `period_start`, `period_end`, `updated_at` y los sumandos (`working_seconds`, `usable_seconds`, `available_seconds`, `operative_seconds`, `total_seconds`, `completion_sum`).

Para combinar varias organizaciones, **suma los segundos**; no promedies los porcentajes. En `metrics`, `cleaning_hours` son las horas trabajando, sea cual sea el robot.

## Otros campos

| Campo | Significado |
| --- | --- |
| `parent_id` | Organización padre. En una organización raíz apunta a sí misma. |
| `report_enabled` | Si están activados los emails de informe. |
| `report_frequency` | Lista con `daily`, `weekly` y/o `monthly`. |

## Jerarquía y permisos

Un **superusuario** gestiona su organización y toda la rama que cuelga de ella. Un **usuario normal** solo ve la suya.

## Ejemplo: crear una organización

```json
{
  "name": "Sede Norte",
  "parent_id": "00000000-0000-4000-8000-000000000001",
  "report_enabled": true,
  "report_frequency": ["weekly"]
}
```

La respuesta añade `uid`.
