# login

Autenticación y recuperación de contraseña.

| Método | Ruta | Quién | Descripción |
| --- | --- | --- | --- |
| POST | `/api/v1/login/access-token` | Público | Obtiene el token a partir de las credenciales. |
| POST | `/api/v1/login/test-token` | Usuario | Comprueba el token y devuelve el usuario. |
| POST | `/api/v1/password-recovery/{email}` | Público | Envía el email de recuperación. |
| POST | `/api/v1/reset-password/` | Público | Establece una contraseña nueva: `{"token", "new_password"}`. |

*Quién* puede llamar: ver la [introducción](introduccion.md#quien-puede-llamar-a-cada-endpoint).

## Ejemplo

La petición va en formato `application/x-www-form-urlencoded`, no en JSON:

```bash
curl -X POST 'https://<host>/api/v1/login/access-token' \
  -H 'Content-Type: application/x-www-form-urlencoded' \
  -d 'grant_type=password&username=usuario@empresa.com&password=miContraseña'
```

```json
{"access_token": "eyJhbGciOi...", "token_type": "bearer"}
```

Ese `access_token` se envía en el resto de peticiones, en la cabecera `Authorization: Bearer <access_token>`.
