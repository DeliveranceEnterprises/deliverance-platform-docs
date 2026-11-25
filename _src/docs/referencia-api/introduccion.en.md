# API Reference: Introduction

This reference covers **API 0.11.2**.

## What is a REST API?

A **REST API** is a standard way for one program to talk to another over the internet: instead of opening the browser and clicking buttons, a program sends an HTTP request to a specific address (**endpoint**) and receives a response, usually in JSON format. Each endpoint has a method (**GET** to read, **POST** to create, **PUT/PATCH** to modify, **DELETE** to delete) and a path (for example `/api/v1/devices/`).

## What is the Deliverance API for?

It gives access from code to what can be seen and done in the platform: devices, tasks, workflows, events, metrics, organizations and users. Use it to integrate the data into another system, automate actions or build your own tools.

## Categories (tags)

| Category | Contents |
| --- | --- |
| [login](login.md) | Get and verify the access token. |
| [users](users.md) | Users. |
| [organizations](organizations.md) | Organizations, hierarchy, metrics and reports. |
| [devices](devices.md) | Devices, status, tasks, alarms and IoT readings. |
| [tasks](tasks.md) | Robot tasks: query, cancellation and timeline. |
| [workflows](workflows.md) | Automations and their runs. |
| [events](events.md) | Event log (read-only). |
| [kpis](kpis.md) | Current indicators and status history. |
| [scenes](scenes.md) | Scenes (buildings) of an organization. |
| [robot-maps](robot-maps.md) | Floors, robot maps and their calibration. |
| [settings](settings.md) | User and organization preferences. |
| [subscriptions](subscriptions.md) | Organization tiers. |
| [utils](utils.md) | Service check. |

## Who can call each endpoint

| Label | Meaning |
| --- | --- |
| **Public** | No token. |
| **User** | Any active user, on the data of their organization. A superuser also reaches the organizations below it. |
| **Superuser** | Superusers only, on their organization and those below it. |
| **Operator** | Whoever can operate robots and workflows; today, superusers. |

A user with no organization has no access to any data.

## Basic fields and patterns

- **Identifiers**: they are UUIDs. The field is called `uid` in every resource except users, where it is `id`.
- **Dates and times**: ISO 8601 format. Without a time zone, they are UTC.
- **Lists**: they return an object `{"data": [...], "count": 12}`. In paginated lists, `count` is the total available; in non-paginated ones, the number of items returned.
- **Pagination**: `skip` (how many to skip) and `limit` (the maximum number to return).
- **Free fields**: `category`, `type` and `status` are text with no closed list. Compare them case-insensitively and tolerate unknown values.

## Common errors

| Code | Meaning |
| --- | --- |
| 400 | Invalid request; some paths also use it for insufficient permissions. |
| 401 / 403 | No token, invalid or expired token, or no permission. |
| 403 `password_expired` | Expired password: only changing the password works. |
| 403 `organization_suspended` | The user's organization is suspended. |
| 404 | Does not exist. |
| 409 | Conflict with the current state (described on each page). |
| 422 | The data is not valid. |
