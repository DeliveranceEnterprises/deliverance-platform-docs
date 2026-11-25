# users

Users: own profile and administration.

| Method | Path | Who | Description |
| --- | --- | --- | --- |
| GET | `/api/v1/users/` | Superuser | Lists the users within reach. |
| POST | `/api/v1/users/` | Superuser | Creates a user. 400 if the email already exists. |
| GET | `/api/v1/users/me` | User | The current user. |
| PATCH | `/api/v1/users/me` | User | Updates the current user. 409 if the email already exists. |
| DELETE | `/api/v1/users/me` | User | Deletes the current user (403 for superusers). |
| PATCH | `/api/v1/users/me/password` | User | Changes the password. |
| POST | `/api/v1/users/signup` | Public | Sign-up. The user is left with no organization. |
| GET | `/api/v1/users/{user_id}` | User | Oneself, or a user within reach. |
| PATCH | `/api/v1/users/{user_id}` | Superuser | Updates a user. |
| DELETE | `/api/v1/users/{user_id}` | Superuser | Deletes a user; never oneself. |
| GET | `/api/v1/users/me/image` | User | Own image. |
| POST | `/api/v1/users/me/image` | User | Uploads the image (`multipart`, field `file`, 10 MB maximum). |
| DELETE | `/api/v1/users/me/image` | User | Deletes the image. |
| GET | `/api/v1/users/{user_id}/image` | User | A user's image. |

*Who* can call: see the [introduction](introduccion.md#who-can-call-each-endpoint).

User preferences are in [settings](settings.md).

## Fields that are not self-explanatory

| Field | Meaning |
| --- | --- |
| `is_active` | If `false`, the user cannot log in. |
| `is_superuser` | Administers their organization and those below it. |
| `report_enabled` | Receives the analytics reports by email. |
| `alarm_enabled` | Receives an email when an alarm goes off. |
| `organization_id` | Their organization, or `null`. Assigned by a superuser. |

## Example: create a user

```json
{
  "email": "new.user@example.com",
  "full_name": "New User",
  "password": "aSecurePassword123",
  "organization_id": "00000000-0000-4000-8000-000000000001",
  "is_superuser": false
}
```

The response adds `id` and the other fields, and never includes the password.
