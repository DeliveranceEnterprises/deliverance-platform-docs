# Referencia de API: Introducción y autenticación

La API de Deliverance Platform es una API REST (OpenAPI 3.1), montada bajo el prefijo `/api/v1`. El esquema OpenAPI completo está disponible en `/api/v1/openapi.json`, y puede explorarse de forma interactiva en el propio Swagger UI del backend.

## Autenticación

La mayoría de endpoints requieren autenticación (se identifican en Swagger por el icono de candado 🔒). El flujo es:

1. Obtener un token llamando a `POST /api/v1/login/access-token` con las credenciales del usuario.
2. Enviar ese token como `Bearer token` en la cabecera `Authorization` del resto de peticiones.

> Los endpoints sin candado (por ejemplo `POST /api/v1/users/signup` o `GET /api/v1/utils/health-check/`) son de acceso público, sin token.

Ver el detalle de estos endpoints en [login](login.md).

## Acceder a la documentación interactiva (Swagger UI)

El propio backend expone una documentación interactiva de la API en `<host>/docs`, generada
automáticamente a partir del esquema OpenAPI (por ejemplo, si la API está desplegada en
`https://api.miempresa.com`, la documentación interactiva está en
`https://api.miempresa.com/docs`). Desde ahí se puede ver cada endpoint, su formato de
entrada y de salida, y probarlo directamente desde el navegador sin necesidad de escribir
ninguna petición a mano: se pulsa el botón **Authorize** arriba a la derecha, se pega el
token de acceso (ver más abajo cómo conseguirlo), y a partir de ahí cualquier endpoint se
puede ejecutar desde la propia página con el botón **Try it out**.

## Probar la API desde terminal

Para usar la API fuera del navegador, con `curl` o cualquier otro cliente HTTP, el flujo
completo son dos pasos: pedir un token, y usarlo en la siguiente petición.

```bash
# 1. Obtener el token con las credenciales del usuario
TOKEN=$(curl -s -X POST 'https://<host>/api/v1/login/access-token' \
  -H 'Content-Type: application/x-www-form-urlencoded' \
  -d 'grant_type=password&username=usuario@empresa.com&password=miContraseña' \
  | python3 -c 'import sys, json; print(json.load(sys.stdin)["access_token"])')

# 2. Usar ese token en cualquier endpoint protegido, en la cabecera Authorization
curl -s 'https://<host>/api/v1/devices/' \
  -H "Authorization: Bearer $TOKEN"
```

El primer comando guarda el token en la variable `TOKEN` (extrayéndolo de la respuesta
JSON con Python), y el segundo lo reutiliza para pedir el listado de dispositivos como
ejemplo. El mismo patrón sirve para cualquier otro endpoint de esta referencia: solo cambia
la ruta y el método (`GET` para leer, `POST` para crear, `PUT`/`PATCH` para modificar,
`DELETE` para borrar).

## Convenciones

- Los recursos con `{id}` / `{uid}` / `{scene_id}` / etc. en la ruta operan sobre un elemento concreto.
- Los verbos siguen la convención REST habitual: `GET` (leer), `POST` (crear), `PUT`/`PATCH` (actualizar), `DELETE` (eliminar).


## Duración del token y de la contraseña

El token caduca a los 8 días (valor por defecto) y no se renueva: se pide otro. La contraseña caduca a los 180 días de cambiarse; con ella caducada se puede obtener token, pero solo funciona `PATCH /api/v1/users/me/password`.
