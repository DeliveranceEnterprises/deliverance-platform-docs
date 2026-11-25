# API Reference: Introduction and authentication

The Deliverance Platform API is a REST API (OpenAPI 3.1), mounted under the prefix `/api/v1`. The full OpenAPI schema is available at `/api/v1/openapi.json`, and can be explored interactively in the backend's own Swagger UI.

## Authentication

Most endpoints require authentication (Swagger marks them with the padlock icon 🔒). The flow is:

1. Get a token by calling `POST /api/v1/login/access-token` with the user's credentials.
2. Send that token as a `Bearer token` in the `Authorization` header of all other requests.

> Endpoints without a padlock (for example `POST /api/v1/users/signup` or `GET /api/v1/utils/health-check/`) are public and need no token.

See the details of these endpoints in [login](login.md).

## Open the interactive documentation (Swagger UI)

The backend itself serves interactive API documentation at `<host>/docs`, generated
automatically from the OpenAPI schema (for example, if the API is deployed at
`https://api.example.com`, the interactive documentation is at
`https://api.example.com/docs`). There you can see each endpoint and its input and
output format, and try it directly from the browser without writing any request by
hand: press the **Authorize** button at the top right, paste the access token (see
below how to get it), and from then on any endpoint can be run from the page itself
with the **Try it out** button.

## Try the API from the terminal

To use the API outside the browser, with `curl` or any other HTTP client, the full
flow has two steps: request a token, and use it in the next request.

```bash
# 1. Get the token with the user's credentials
TOKEN=$(curl -s -X POST 'https://<host>/api/v1/login/access-token' \
  -H 'Content-Type: application/x-www-form-urlencoded' \
  -d 'grant_type=password&username=user@example.com&password=myPassword' \
  | python3 -c 'import sys, json; print(json.load(sys.stdin)["access_token"])')

# 2. Use that token on any protected endpoint, in the Authorization header
curl -s 'https://<host>/api/v1/devices/' \
  -H "Authorization: Bearer $TOKEN"
```

The first command saves the token in the `TOKEN` variable (extracting it from the JSON
response with Python), and the second reuses it to request the list of devices as an
example. The same pattern works for any other endpoint in this reference: only the path
and the method change (`GET` to read, `POST` to create, `PUT`/`PATCH` to modify,
`DELETE` to delete).

## Conventions

- Resources with `{id}` / `{uid}` / `{scene_id}` / etc. in the path operate on a specific item.
- Verbs follow the usual REST convention: `GET` (read), `POST` (create), `PUT`/`PATCH` (update), `DELETE` (delete).


## Token and password lifetime

The token expires after 8 days (default value) and cannot be renewed: request a new one. The password expires 180 days after it was changed; once it has expired a token can still be obtained, but only `PATCH /api/v1/users/me/password` works.
