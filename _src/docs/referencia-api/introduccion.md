# Referencia de API: Introducción

Esta referencia corresponde a la **API 0.11.2**.

## ¿Qué es una API REST?

Una **API REST** es una forma estándar de que un programa hable con otro por internet: en vez de abrir el navegador y hacer clic en botones, un programa envía una petición HTTP a una dirección concreta (**endpoint**) y recibe una respuesta, normalmente en formato JSON. Cada endpoint tiene un método (**GET** para leer, **POST** para crear, **PUT/PATCH** para modificar, **DELETE** para borrar) y una ruta (por ejemplo `/api/v1/devices/`).

## ¿Para qué sirve la API de Deliverance?

Da acceso por código a lo que se puede ver y hacer desde la plataforma: dispositivos, tareas, workflows, eventos, métricas, organizaciones y usuarios. Sirve para integrar los datos en otro sistema, automatizar acciones o construir herramientas propias.

## Categorías (tags)

| Categoría | Contenido |
| --- | --- |
| [login](login.md) | Obtener y verificar el token de acceso. |
| [users](users.md) | Usuarios. |
| [organizations](organizations.md) | Organizaciones, jerarquía, métricas e informes. |
| [devices](devices.md) | Dispositivos, estado, tareas, alarmas y lecturas IoT. |
| [tasks](tasks.md) | Tareas de los robots: consulta, cancelación y cronograma. |
| [workflows](workflows.md) | Automatizaciones y sus ejecuciones. |
| [events](events.md) | Registro de eventos (solo lectura). |
| [kpis](kpis.md) | Indicadores actuales e histórico de estado. |
| [scenes](scenes.md) | Escenas (edificios) de una organización. |
| [robot-maps](robot-maps.md) | Plantas, mapas de robots y su calibración. |
| [settings](settings.md) | Preferencias de usuario y de organización. |
| [subscriptions](subscriptions.md) | Tier de las organizaciones. |
| [utils](utils.md) | Comprobación del servicio. |

## Quién puede llamar a cada endpoint

| Etiqueta | Significado |
| --- | --- |
| **Público** | Sin token. |
| **Usuario** | Cualquier usuario activo, sobre los datos de su organización. Un superusuario llega también a las que cuelgan de ella. |
| **Superusuario** | Solo superusuarios, sobre su organización y las que cuelgan de ella. |
| **Operador** | Quien puede operar robots y workflows; hoy, los superusuarios. |

Un usuario sin organización no accede a ningún dato.

## Campos y patrones básicos

- **Identificadores**: son UUID. El campo se llama `uid` en todos los recursos, salvo en los usuarios, donde es `id`.
- **Fechas y horas**: formato ISO 8601. Sin zona horaria, son UTC.
- **Listados**: devuelven un objeto `{"data": [...], "count": 12}`. En los paginados, `count` es el total disponible; en los no paginados, los elementos devueltos.
- **Paginación**: `skip` (cuántos saltarse) y `limit` (cuántos devolver como máximo).
- **Campos libres**: `category`, `type` y `status` son texto sin lista cerrada. Compáralos sin distinguir mayúsculas y tolera valores desconocidos.

## Errores habituales

| Código | Significado |
| --- | --- |
| 400 | Petición no válida; algunas rutas lo usan también para permisos insuficientes. |
| 401 / 403 | Sin token, token no válido o caducado, o sin permiso. |
| 403 `password_expired` | Contraseña caducada: solo funciona el cambio de contraseña. |
| 403 `organization_suspended` | La organización del usuario está suspendida. |
| 404 | No existe. |
| 409 | Conflicto con el estado actual (se indica en cada página). |
| 422 | Los datos no son válidos. |
