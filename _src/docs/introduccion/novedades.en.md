# What's new

Edition for **Platform 0.9.2** and **API 0.11.2** (24 November 2026).

## In the platform

- **[Operation](../guia-de-uso/operation.md)**: new section for administrators. Start, stop and cancel robot tasks, with a timeline of what has run.
- **[Workflows](../guia-de-uso/workflows.md)**: visual automation editor with three boxes (event, condition and task), checks and run history.
- **[Dashboard](../guia-de-uso/dashboard.md)** configurable per organization, with filters and new cards: Recent Activity, Camera View, Robot Status Timeline and Start Tasks.
- **[Monitor](../guia-de-uso/monitor.md)**: cameras, status history, device activity, robot position on its map and an advanced chart mode.
- **[Analytics](../guia-de-uso/analytics.md)**: events tab with CSV export.
- **Metrics**: *Compliance* is now called *Task completion*, and *Utilization* and *Availability* are now calculated over time.
- **Connector errors** made visible: if a connector does not start or stop a task, the platform says so.
- **[Tiers](../guia-de-uso/admin.md#organization-tier)** of organizations, and suspension.
- **Languages**: English, Español and 简体中文.

## In the API

- New groups: [workflows](../referencia-api/workflows.md), [events](../referencia-api/events.md), [kpis](../referencia-api/kpis.md), [robot-maps](../referencia-api/robot-maps.md), [settings](../referencia-api/settings.md) and [subscriptions](../referencia-api/subscriptions.md).
- [devices](../referencia-api/devices.md) and [tasks](../referencia-api/tasks.md): task catalog, start, cancellation, timeline, camera image and meter configuration.
- **Superuser scope**: only their own organization and those below it.
- Only one task can be running per robot (409), and a device with data cannot be deleted, only disabled (409).
- `GET /switch-database/{data_source}` is removed.
