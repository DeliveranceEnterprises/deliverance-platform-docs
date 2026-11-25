# organizations

Organizations, their hierarchy, metrics and reports.

| Method | Path | Who | Description |
| --- | --- | --- | --- |
| GET | `/api/v1/organizations/` | User | Lists the organizations within reach. |
| POST | `/api/v1/organizations/` | Superuser | Creates an organization. |
| GET | `/api/v1/organizations/{id}` | User | One organization. |
| PUT | `/api/v1/organizations/{id}` | User | Updates it. Only a superuser changes the parent. |
| DELETE | `/api/v1/organizations/{id}` | Superuser | Deletes it. Never one's own. |
| GET | `/api/v1/organizations/{id}/child` | User | Direct children (one level). |
| GET | `/api/v1/organizations/{id}/devices` | User | Devices, with their status. |
| GET | `/api/v1/organizations/{id}/scenes` | User | Scenes. |
| GET | `/api/v1/organizations/{id}/task-stats` | User | Tasks since `start_date` (until `end_date` or now). |
| GET | `/api/v1/organizations/{id}/metric-stats` | User | Metrics for the period, with no breakdown. |
| GET | `/api/v1/organizations/{id}/metrics` | User | Metrics for the period, per device. |
| POST | `/api/v1/organizations/{id}/send-report` | User | Sends the PDF report to the caller's email. 503 if email is not configured. |
| GET | `/api/v1/organizations/{id}/image` | User | Logo. |
| POST | `/api/v1/organizations/{id}/image` | User | Uploads the logo (`multipart`, 10 MB maximum). |
| DELETE | `/api/v1/organizations/{id}/image` | User | Deletes the logo. |

*Who* can call: see the [introduction](introduccion.md#who-can-call-each-endpoint).

See also [kpis](kpis.md), [settings](settings.md), [robot-maps](robot-maps.md) and [subscriptions](subscriptions.md).

## `metrics` and `metric-stats`

Both require `start_date` and `end_date` (`YYYY-MM-DD`, days in UTC). `metrics` adds the `per_device` breakdown. Only robots count; one with no connection for 7 days is out of service.

| Metric | How it is calculated |
| --- | --- |
| `compliance_percentage` | Average completion of finished tasks (failed and expired count as 0; cancelled are left out). |
| `utilization_percentage` | Time working over time available and not charging. |
| `availability_percentage` | Time not disconnected, faulty or stopped, over the total. |
| `operative_percentage` | Time working or free, over the total. |

Any of them can be `null` if there is no data. `metric-stats` also includes the tasks by result, `total_devices`, `out_of_service_devices`, `period_start`, `period_end`, `updated_at` and the addends (`working_seconds`, `usable_seconds`, `available_seconds`, `operative_seconds`, `total_seconds`, `completion_sum`).

To combine several organizations, **add up the seconds**; do not average the percentages. In `metrics`, `cleaning_hours` is the hours working, whatever the robot.

## Other fields

| Field | Meaning |
| --- | --- |
| `parent_id` | Parent organization. In a root organization it points to itself. |
| `report_enabled` | Whether report emails are on. |
| `report_frequency` | List with `daily`, `weekly` and/or `monthly`. |

## Hierarchy and permissions

A **superuser** manages their organization and the whole branch below it. A **regular user** only sees their own.

## Example: create an organization

```json
{
  "name": "North Site",
  "parent_id": "00000000-0000-4000-8000-000000000001",
  "report_enabled": true,
  "report_frequency": ["weekly"]
}
```

The response adds `uid`.
