# login

Authentication and password recovery.

| Method | Path | Who | Description |
| --- | --- | --- | --- |
| POST | `/api/v1/login/access-token` | Public | Gets the token from the credentials. |
| POST | `/api/v1/login/test-token` | User | Checks the token and returns the user. |
| POST | `/api/v1/password-recovery/{email}` | Public | Sends the recovery email. |
| POST | `/api/v1/reset-password/` | Public | Sets a new password: `{"token", "new_password"}`. |

*Who* can call: see the [introduction](introduccion.md#who-can-call-each-endpoint).

## Example

The request is sent as `application/x-www-form-urlencoded`, not as JSON:

```bash
curl -X POST 'https://<host>/api/v1/login/access-token' \
  -H 'Content-Type: application/x-www-form-urlencoded' \
  -d 'grant_type=password&username=user@example.com&password=myPassword'
```

```json
{"access_token": "eyJhbGciOi...", "token_type": "bearer"}
```

That `access_token` is sent in all other requests, in the `Authorization: Bearer <access_token>` header.
