# users {#users}

用户：个人资料和管理。

| 方法 | 路径 | 调用者 | 说明 |
| --- | --- | --- | --- |
| GET | `/api/v1/users/` | 超级用户 | 列出可访问的用户。 |
| POST | `/api/v1/users/` | 超级用户 | 创建用户。如果邮箱已存在，返回 400。 |
| GET | `/api/v1/users/me` | 用户 | 当前用户。 |
| PATCH | `/api/v1/users/me` | 用户 | 更新当前用户。如果邮箱已存在，返回 409。 |
| DELETE | `/api/v1/users/me` | 用户 | 删除当前用户（超级用户返回 403）。 |
| PATCH | `/api/v1/users/me/password` | 用户 | 更改密码。 |
| POST | `/api/v1/users/signup` | 公开 | 注册。用户没有所属组织。 |
| GET | `/api/v1/users/{user_id}` | 用户 | 自己，或可访问的用户。 |
| PATCH | `/api/v1/users/{user_id}` | 超级用户 | 更新用户。 |
| DELETE | `/api/v1/users/{user_id}` | 超级用户 | 删除用户；绝不能删除自己。 |
| GET | `/api/v1/users/me/image` | 用户 | 自己的图像。 |
| POST | `/api/v1/users/me/image` | 用户 | 上传图像（`multipart`，字段 `file`，最大 10 MB）。 |
| DELETE | `/api/v1/users/me/image` | 用户 | 删除图像。 |
| GET | `/api/v1/users/{user_id}/image` | 用户 | 某个用户的图像。 |

*调用者* 的含义：见[简介](introduccion.md#who-can-call-each-endpoint)。

用户的偏好设置见 [settings](settings.md)。

## 含义不直观的字段 {#fields-that-are-not-self-explanatory}

| 字段 | 含义 |
| --- | --- |
| `is_active` | 如果为 `false`，则无法登录。 |
| `is_superuser` | 管理其组织及下级组织。 |
| `report_enabled` | 通过邮件接收分析报告。 |
| `alarm_enabled` | 告警触发时通过邮件收到通知。 |
| `organization_id` | 所属组织，或 `null`。由超级用户分配。 |

## 示例：创建用户 {#example-create-a-user}

```json
{
  "email": "new.user@example.com",
  "full_name": "New User",
  "password": "aSecurePassword123",
  "organization_id": "00000000-0000-4000-8000-000000000001",
  "is_superuser": false
}
```

响应会增加 `id` 和其余字段，且绝不包含密码。
