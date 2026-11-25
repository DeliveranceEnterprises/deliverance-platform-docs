# users {#users}

Usuarios: perfil propio y administración.

| Método | Ruta | Quién | Descripción |
| --- | --- | --- | --- |
| GET | `/api/v1/users/` | Superusuario | Lista los usuarios a su alcance. |
| POST | `/api/v1/users/` | Superusuario | Crea un usuario. 400 si el email ya existe. |
| GET | `/api/v1/users/me` | Usuario | El usuario actual. |
| PATCH | `/api/v1/users/me` | Usuario | Actualiza el usuario actual. 409 si el email ya existe. |
| DELETE | `/api/v1/users/me` | Usuario | Elimina el usuario actual (403 para superusuarios). |
| PATCH | `/api/v1/users/me/password` | Usuario | Cambia la contraseña. |
| POST | `/api/v1/users/signup` | Público | Registro. El usuario queda sin organización. |
| GET | `/api/v1/users/{user_id}` | Usuario | Uno mismo, o un usuario a su alcance. |
| PATCH | `/api/v1/users/{user_id}` | Superusuario | Actualiza un usuario. |
| DELETE | `/api/v1/users/{user_id}` | Superusuario | Elimina un usuario; nunca a uno mismo. |
| GET | `/api/v1/users/me/image` | Usuario | Imagen propia. |
| POST | `/api/v1/users/me/image` | Usuario | Sube la imagen (`multipart`, campo `file`, máximo 10 MB). |
| DELETE | `/api/v1/users/me/image` | Usuario | Elimina la imagen. |
| GET | `/api/v1/users/{user_id}/image` | Usuario | Imagen de un usuario. |

*Quién* puede llamar: ver la [introducción](introduccion.md#who-can-call-each-endpoint).

Las preferencias del usuario están en [settings](settings.md).

## Campos que no son autoexplicativos {#fields-that-are-not-self-explanatory}

| Campo | Significado |
| --- | --- |
| `is_active` | Si es `false`, no puede iniciar sesión. |
| `is_superuser` | Administra su organización y las que cuelgan de ella. |
| `report_enabled` | Recibe los informes de analítica por email. |
| `alarm_enabled` | Recibe aviso por email cuando salta una alarma. |
| `organization_id` | Su organización, o `null`. La asigna un superusuario. |

## Ejemplo: crear un usuario {#example-create-a-user}

```json
{
  "email": "new.user@example.com",
  "full_name": "New User",
  "password": "aSecurePassword123",
  "organization_id": "00000000-0000-4000-8000-000000000001",
  "is_superuser": false
}
```

La respuesta añade `id` y el resto de campos, y nunca incluye la contraseña.
