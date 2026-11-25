# login {#login}

认证和密码恢复。

| 方法 | 路径 | 调用者 | 说明 |
| --- | --- | --- | --- |
| POST | `/api/v1/login/access-token` | 公开 | 使用凭据获取令牌。 |
| POST | `/api/v1/login/test-token` | 用户 | 检查令牌并返回用户。 |
| POST | `/api/v1/password-recovery/{email}` | 公开 | 发送密码恢复邮件。 |
| POST | `/api/v1/reset-password/` | 公开 | 设置新密码：`{"token", "new_password"}`。 |

*调用者* 的含义：见[简介](introduccion.md#who-can-call-each-endpoint)。

## 示例 {#example}

请求采用 `application/x-www-form-urlencoded` 格式，而非 JSON：

```bash
curl -X POST 'https://<host>/api/v1/login/access-token' \
  -H 'Content-Type: application/x-www-form-urlencoded' \
  -d 'grant_type=password&username=user@example.com&password=myPassword'
```

```json
{"access_token": "eyJhbGciOi...", "token_type": "bearer"}
```

在其余请求中，通过请求头 `Authorization: Bearer <access_token>` 发送该 `access_token`。
