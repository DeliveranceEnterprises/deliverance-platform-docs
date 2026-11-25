# API 参考：简介 {#api-reference-introduction}

本参考对应 **API 0.11.2**。

## 什么是 REST API？ {#what-is-a-rest-api}

**REST API** 是程序之间通过互联网通信的一种标准方式：程序无需打开浏览器点击按钮，而是向特定地址（**端点**）发送 HTTP 请求并收到响应，通常为 JSON 格式。每个端点都有一个方法（**GET** 用于读取，**POST** 用于创建，**PUT/PATCH** 用于修改，**DELETE** 用于删除）和一个路径（例如 `/api/v1/devices/`）。

## Deliverance API 有什么用途？ {#what-is-the-deliverance-api-for}

通过代码访问平台上可以查看和操作的内容：设备、任务、工作流、事件、指标、组织和用户。可用于将数据集成到其他系统、自动执行操作或构建自有工具。

## 类别（tags） {#categories-tags}

| 类别 | 内容 |
| --- | --- |
| [login](login.md) | 获取和验证访问令牌。 |
| [users](users.md) | 用户。 |
| [organizations](organizations.md) | 组织、层级、指标和报告。 |
| [devices](devices.md) | 设备、状态、任务、告警和 IoT 读数。 |
| [tasks](tasks.md) | 机器人任务：查询、取消和时间线。 |
| [workflows](workflows.md) | 自动化流程及其执行记录。 |
| [events](events.md) | 事件记录（只读）。 |
| [kpis](kpis.md) | 当前指标和状态历史。 |
| [scenes](scenes.md) | 组织的场景（建筑）。 |
| [robot-maps](robot-maps.md) | 楼层、机器人地图及其标定。 |
| [settings](settings.md) | 用户和组织的偏好设置。 |
| [subscriptions](subscriptions.md) | 组织的等级（tier）。 |
| [utils](utils.md) | 服务检查。 |

## 谁可以调用各端点 {#who-can-call-each-endpoint}

| 标签 | 含义 |
| --- | --- |
| **公开** | 无需令牌。 |
| **用户** | 任何有效用户，仅限其组织的数据。超级用户还可访问其下级组织的数据。 |
| **超级用户** | 仅限超级用户，范围为其组织及下级组织。 |
| **操作员** | 可以操作机器人和工作流的用户；目前为超级用户。 |

没有组织的用户无法访问任何数据。

## 基本字段和模式 {#basic-fields-and-patterns}

- **标识符**：均为 UUID。所有资源中该字段都名为 `uid`，但用户资源中为 `id`。
- **日期和时间**：ISO 8601 格式。未注明时区的为 UTC。
- **列表**：返回对象 `{"data": [...], "count": 12}`。在分页列表中，`count` 是可用总数；在不分页的列表中，是返回的元素数。
- **分页**：`skip`（跳过的数量）和 `limit`（最多返回的数量）。
- **自由字段**：`category`、`type` 和 `status` 是没有固定取值列表的文本。比较时不区分大小写，并应容许未知值。

## 常见错误 {#common-errors}

| 代码 | 含义 |
| --- | --- |
| 400 | 请求无效；部分路径也用它表示权限不足。 |
| 401 / 403 | 没有令牌、令牌无效或已过期，或没有权限。 |
| 403 `password_expired` | 密码已过期：只能执行密码更改。 |
| 403 `organization_suspended` | 用户所属组织已暂停。 |
| 404 | 不存在。 |
| 409 | 与当前状态冲突（各页面有说明）。 |
| 422 | 数据无效。 |
