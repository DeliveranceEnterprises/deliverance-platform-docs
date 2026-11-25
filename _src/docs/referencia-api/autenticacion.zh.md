# API 参考：简介和认证 {#api-reference-introduction-and-authentication}

Deliverance Platform 的 API 是一个 REST API（OpenAPI 3.1），挂载在前缀 `/api/v1` 下。完整的 OpenAPI 架构可在 `/api/v1/openapi.json` 获取，也可以在后端自带的 Swagger UI 中交互式浏览。

## 认证 {#authentication}

大多数端点需要认证（在 Swagger 中以锁形图标 🔒 标识）。流程如下：

1. 使用用户凭据调用 `POST /api/v1/login/access-token` 获取令牌。
2. 在其余请求的 `Authorization` 请求头中以 `Bearer token` 形式发送该令牌。

> 没有锁形图标的端点（例如 `POST /api/v1/users/signup` 或 `GET /api/v1/utils/health-check/`）可公开访问，无需令牌。

这些端点的详细信息见 [login](login.md)。

## 访问交互式文档（Swagger UI） {#open-the-interactive-documentation-swagger-ui}

后端自身在 `<host>/docs` 提供 API 的交互式文档，由 OpenAPI 架构自动生成（例如，如果 API 部署在
`https://api.example.com`，则交互式文档位于
`https://api.example.com/docs`）。在那里可以查看每个端点及其输入和输出格式，
并直接在浏览器中测试，无需手写任何请求：点击右上角的 **Authorize** 按钮，
粘贴访问令牌（获取方法见下文），之后即可在页面上用 **Try it out** 按钮执行任何端点。

## 从终端测试 API {#try-the-api-from-the-terminal}

要在浏览器之外使用 API（通过 `curl` 或任何其他 HTTP 客户端），完整流程分两步：
请求令牌，然后在下一个请求中使用它。

```bash
# 1. 使用用户凭据获取令牌
TOKEN=$(curl -s -X POST 'https://<host>/api/v1/login/access-token' \
  -H 'Content-Type: application/x-www-form-urlencoded' \
  -d 'grant_type=password&username=user@example.com&password=myPassword' \
  | python3 -c 'import sys, json; print(json.load(sys.stdin)["access_token"])')

# 2. 在任何受保护端点的 Authorization 请求头中使用该令牌
curl -s 'https://<host>/api/v1/devices/' \
  -H "Authorization: Bearer $TOKEN"
```

第一条命令将令牌保存到变量 `TOKEN` 中（用 Python 从 JSON 响应中提取），
第二条命令使用该令牌，以请求设备列表为例。同样的模式适用于本参考中的任何其他端点：
只需更改路径和方法（`GET` 用于读取，`POST` 用于创建，`PUT`/`PATCH` 用于修改，
`DELETE` 用于删除）。

## 约定 {#conventions}

- 路径中带有 `{id}` / `{uid}` / `{scene_id}` 等的资源针对某个具体元素进行操作。
- 方法遵循常见的 REST 约定：`GET`（读取）、`POST`（创建）、`PUT`/`PATCH`（更新）、`DELETE`（删除）。


## 令牌和密码的有效期 {#token-and-password-lifetime}

令牌在 8 天后过期（默认值），且不会续期：需重新获取。密码在更改 180 天后过期；密码过期后仍可获取令牌，但只能使用 `PATCH /api/v1/users/me/password`。
