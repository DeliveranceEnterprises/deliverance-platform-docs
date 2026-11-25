# 新增内容 {#whats-new}

适用于 **Platform 0.9.2** 和 **API 0.11.2** 的版本（2026 年 11 月 24 日）。

## 平台 {#in-the-platform}

- **[运行](../guia-de-uso/operation.md)**（**Operation**）：面向管理员的新版块。启动、停止和取消机器人的任务，并提供已执行内容的时间线。
- **[工作流](../guia-de-uso/workflows.md)**（**Workflows**）：自动化的可视化编辑器，包含三种方框（事件、条件和任务）、检查以及执行历史。
- **[仪表板](../guia-de-uso/dashboard.md)**（**Dashboard**）：可按组织配置，提供筛选和新卡片：最近动态（Recent Activity）、摄像头画面（Camera View）、机器人状态时间线（Robot Status Timeline）和启动任务（Start Tasks）。
- **[监控](../guia-de-uso/monitor.md)**（**Monitor**）：摄像头、状态历史、设备动态、机器人在其地图上的位置以及图表的高级模式。
- **[分析](../guia-de-uso/analytics.md)**（**Analytics**）：事件标签页，可导出为 CSV。
- **指标**：*Compliance* 更名为 *任务完成率*（*Task completion*）；*利用率*（*Utilization*）和 *可用率*（*Availability*）现在按时间计算。
- **连接器错误** 可见：如果连接器没有启动或停止任务，平台会明确指出。
- 组织的 **[等级](../guia-de-uso/admin.md#organization-tier)**（**Tier**）以及暂停。
- **语言**：English、Español 和简体中文。

## API {#in-the-api}

- 新的分组：[workflows](../referencia-api/workflows.md)、[events](../referencia-api/events.md)、[kpis](../referencia-api/kpis.md)、[robot-maps](../referencia-api/robot-maps.md)、[settings](../referencia-api/settings.md) 和 [subscriptions](../referencia-api/subscriptions.md)。
- [devices](../referencia-api/devices.md) 和 [tasks](../referencia-api/tasks.md)：任务目录、启动、取消、时间线、摄像头图像和电表配置。
- **超级用户的范围**：仅限其所属组织及该组织的下级组织。
- 每台机器人只能有一个进行中的任务（409）；已有数据的设备不能删除，只能停用（409）。
- 移除 `GET /switch-database/{data_source}`。
