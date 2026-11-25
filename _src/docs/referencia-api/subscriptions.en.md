# subscriptions

Tier of each organization.

| Method | Path | Who | Description |
| --- | --- | --- | --- |
| GET | `/api/v1/subscriptions/tiers` | User | The tiers and what they include. |
| GET | `/api/v1/subscriptions` | User | Tier of the organizations within reach (no trailing slash). |
| GET | `/api/v1/organizations/{id}/subscription` | User | Tier of an organization; the details, only for superusers. |
| PUT | `/api/v1/organizations/{id}/subscription/payer` | Superuser | Of the parent: whether its invoice includes the child's (`{"billed_to_parent": true}`). |
| GET | `/api/v1/organizations/{id}/subscription/history` | Superuser | Changes. |
| GET | `/api/v1/organizations/{id}/subscription/usage` | Superuser | Usage for a month (`?month=YYYY-MM`). |
| GET | `/api/v1/organizations/{id}/subscription/robot-log` | Superuser | Robots entering and leaving service. |

*Who* can call: see the [introduction](introduccion.md#who-can-call-each-endpoint).

`tier` is `watch`, `operate` or `orchestrate`. `state` is `active`, `expiring` (60 days or less), `expired` or `suspended`. The tier, the contract and the suspension are changed by Deliverance.

While an organization is suspended, its users receive **403** `organization_suspended` when logging in and on any call.
