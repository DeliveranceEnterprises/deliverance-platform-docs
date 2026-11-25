# settings

Preferences stored by key.

| Method | Path | Who | Description |
| --- | --- | --- | --- |
| GET | `/api/v1/users/me/settings` | User | All of one's own. |
| GET | `/api/v1/users/me/settings/{key}` | User | One. |
| PUT | `/api/v1/users/me/settings/{key}` | User | Saves it. |
| DELETE | `/api/v1/users/me/settings/{key}` | User | Deletes it. |
| GET | `/api/v1/organizations/{id}/settings` | User | Those of the organization. |
| GET | `/api/v1/organizations/{id}/settings/{key}` | User | One. |
| PUT | `/api/v1/organizations/{id}/settings/{key}` | User | Saves it, for all its users. |
| DELETE | `/api/v1/organizations/{id}/settings/{key}` | User | Deletes it. |

*Who* can call: see the [introduction](introduccion.md#who-can-call-each-endpoint).

| Level | Keys |
| --- | --- |
| User | `ui.theme` (`light` or `dark`), `ui.language`, `dashboard.filters`, `dashboard.cardState` |
| Organization | `dashboard.layout` |

The value is any JSON up to 64 KB. `version` (optional) is the version the change starts from, 0 if it did not exist: if someone else saved first, it responds **409** with the current value. Without `version` the value is overwritten. When deleting, it goes in the query (`?version=`).

```json
{"value": "dark", "version": 0}
```
