# settings {#settings}

按键保存的偏好设置。

| 方法 | 路径 | 调用者 | 说明 |
| --- | --- | --- | --- |
| GET | `/api/v1/users/me/settings` | 用户 | 自己的所有设置。 |
| GET | `/api/v1/users/me/settings/{key}` | 用户 | 单项设置。 |
| PUT | `/api/v1/users/me/settings/{key}` | 用户 | 保存设置。 |
| DELETE | `/api/v1/users/me/settings/{key}` | 用户 | 删除设置。 |
| GET | `/api/v1/organizations/{id}/settings` | 用户 | 组织的设置。 |
| GET | `/api/v1/organizations/{id}/settings/{key}` | 用户 | 单项设置。 |
| PUT | `/api/v1/organizations/{id}/settings/{key}` | 用户 | 保存设置，对组织的所有用户生效。 |
| DELETE | `/api/v1/organizations/{id}/settings/{key}` | 用户 | 删除设置。 |

*调用者* 的含义：见[简介](introduccion.md#who-can-call-each-endpoint)。

| 级别 | 键 |
| --- | --- |
| 用户 | `ui.theme`（`light` 或 `dark`）、`ui.language`、`dashboard.filters`、`dashboard.cardState` |
| 组织 | `dashboard.layout` |

值为任意 JSON，最大 64 KB。`version`（可选）是更改所基于的版本，原先不存在则为 0：如果其他人已先保存，返回 **409** 和当前值。不带 `version` 则直接覆盖。删除时放在查询参数中（`?version=`）。

```json
{"value": "dark", "version": 0}
```
