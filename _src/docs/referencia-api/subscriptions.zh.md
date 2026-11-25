# subscriptions {#subscriptions}

各组织的等级（tier）。

| 方法 | 路径 | 调用者 | 说明 |
| --- | --- | --- | --- |
| GET | `/api/v1/subscriptions/tiers` | 用户 | 各等级及其包含的内容。 |
| GET | `/api/v1/subscriptions` | 用户 | 可访问组织的等级（末尾无斜杠）。 |
| GET | `/api/v1/organizations/{id}/subscription` | 用户 | 单个组织的等级；详细信息仅限超级用户。 |
| PUT | `/api/v1/organizations/{id}/subscription/payer` | 超级用户 | 上级组织的超级用户：其账单是否包含下级组织的账单（`{"billed_to_parent": true}`）。 |
| GET | `/api/v1/organizations/{id}/subscription/history` | 超级用户 | 变更记录。 |
| GET | `/api/v1/organizations/{id}/subscription/usage` | 超级用户 | 某个月的用量（`?month=YYYY-MM`）。 |
| GET | `/api/v1/organizations/{id}/subscription/robot-log` | 超级用户 | 在役机器人的增减记录。 |

*调用者* 的含义：见[简介](introduccion.md#who-can-call-each-endpoint)。

`tier` 为 `watch`、`operate` 或 `orchestrate`。`state` 为 `active`、`expiring`（剩余 60 天或更少）、`expired` 或 `suspended`。等级、合同和暂停状态由 Deliverance 更改。

组织暂停期间，其用户在登录和任何调用时都会收到 **403** `organization_suspended`。
