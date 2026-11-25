# subscriptions {#subscriptions}

Tier de cada organización.

| Método | Ruta | Quién | Descripción |
| --- | --- | --- | --- |
| GET | `/api/v1/subscriptions/tiers` | Usuario | Los tiers y lo que incluyen. |
| GET | `/api/v1/subscriptions` | Usuario | Tier de las organizaciones a su alcance (sin barra final). |
| GET | `/api/v1/organizations/{id}/subscription` | Usuario | Tier de una organización; el detalle, solo a superusuarios. |
| PUT | `/api/v1/organizations/{id}/subscription/payer` | Superusuario | Del padre: si su factura incluye la de la hija (`{"billed_to_parent": true}`). |
| GET | `/api/v1/organizations/{id}/subscription/history` | Superusuario | Cambios. |
| GET | `/api/v1/organizations/{id}/subscription/usage` | Superusuario | Uso de un mes (`?month=YYYY-MM`). |
| GET | `/api/v1/organizations/{id}/subscription/robot-log` | Superusuario | Altas y bajas de robots en servicio. |

*Quién* puede llamar: ver la [introducción](introduccion.md#who-can-call-each-endpoint).

`tier` es `watch`, `operate` u `orchestrate`. `state` es `active`, `expiring` (60 días o menos), `expired` o `suspended`. El tier, el contrato y la suspensión los cambia Deliverance.

Mientras una organización está suspendida, sus usuarios reciben **403** `organization_suspended` al iniciar sesión y en cualquier llamada.
