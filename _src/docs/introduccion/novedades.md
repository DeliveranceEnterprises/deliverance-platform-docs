# Novedades

Edición para **Platform 0.9.2** y **API 0.11.2** (24 de noviembre de 2026).

## En la plataforma

- **[Operation](../guia-de-uso/operation.md)**: nueva sección para administradores. Arrancar, parar y cancelar tareas de los robots, con el cronograma de lo ejecutado.
- **[Workflows](../guia-de-uso/workflows.md)**: editor visual de automatizaciones con tres cajas (evento, condición y tarea), comprobaciones e histórico de ejecuciones.
- **[Dashboard](../guia-de-uso/dashboard.md)** configurable por organización, con filtros y tarjetas nuevas: Recent Activity, Camera View, Robot Status Timeline y Start Tasks.
- **[Monitor](../guia-de-uso/monitor.md)**: cámaras, histórico de estado, actividad del dispositivo, posición del robot sobre su mapa y modo avanzado de gráficas.
- **[Analytics](../guia-de-uso/analytics.md)**: pestaña de eventos con exportación a CSV.
- **Métricas**: *Compliance* pasa a llamarse *Task completion*, y *Utilization* y *Availability* se calculan ahora sobre tiempo.
- **Errores de conector** visibles: si un conector no arranca o no para una tarea, la plataforma lo dice.
- **[Tiers](../guia-de-uso/admin.md#tier-de-una-organizacion)** de las organizaciones y suspensión.
- **Idiomas**: English, Español y 简体中文.

## En la API

- Nuevos grupos: [workflows](../referencia-api/workflows.md), [events](../referencia-api/events.md), [kpis](../referencia-api/kpis.md), [robot-maps](../referencia-api/robot-maps.md), [settings](../referencia-api/settings.md) y [subscriptions](../referencia-api/subscriptions.md).
- [devices](../referencia-api/devices.md) y [tasks](../referencia-api/tasks.md): catálogo de tareas, arranque, cancelación, cronograma, imagen de cámara y configuración de medidores.
- **Alcance de los superusuarios**: solo su organización y las que cuelgan de ella.
- Solo puede haber una tarea en marcha por robot (409), y un dispositivo con datos no se borra, se deshabilita (409).
- Desaparece `GET /switch-database/{data_source}`.
