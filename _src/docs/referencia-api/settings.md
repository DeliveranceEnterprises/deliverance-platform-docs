# settings

Preferencias guardadas por clave.

| Método | Ruta | Quién | Descripción |
| --- | --- | --- | --- |
| GET | `/api/v1/users/me/settings` | Usuario | Todas las propias. |
| GET | `/api/v1/users/me/settings/{key}` | Usuario | Una. |
| PUT | `/api/v1/users/me/settings/{key}` | Usuario | La guarda. |
| DELETE | `/api/v1/users/me/settings/{key}` | Usuario | La elimina. |
| GET | `/api/v1/organizations/{id}/settings` | Usuario | Las de la organización. |
| GET | `/api/v1/organizations/{id}/settings/{key}` | Usuario | Una. |
| PUT | `/api/v1/organizations/{id}/settings/{key}` | Usuario | La guarda, para todos sus usuarios. |
| DELETE | `/api/v1/organizations/{id}/settings/{key}` | Usuario | La elimina. |

*Quién* puede llamar: ver la [introducción](introduccion.md#quien-puede-llamar-a-cada-endpoint).

| Nivel | Claves |
| --- | --- |
| Usuario | `ui.theme` (`light` o `dark`), `ui.language`, `dashboard.filters`, `dashboard.cardState` |
| Organización | `dashboard.layout` |

El valor es cualquier JSON de hasta 64 KB. `version` (opcional) es la versión de la que parte el cambio, 0 si no existía: si otra persona guardó antes, responde **409** con el valor actual. Sin `version` se sobrescribe. Al borrar va en la consulta (`?version=`).

```json
{"value": "dark", "version": 0}
```
