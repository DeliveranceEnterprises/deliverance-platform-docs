# What is Deliverance Platform?

Deliverance Platform brings the management of an organization's robotic and IoT devices (robots, sensors, cameras and meters) together in a single panel, whatever the manufacturer of each device.

From the platform you can enable and organize devices, monitor their operation in real time, give tasks to robots, automate them with workflows, view usage and consumption analytics, and manage users and organizations.

## Key concepts

Before reading the rest of the manual, it helps to be clear on these concepts, which appear on almost every page:

- **Organization**: the entity (customer, site, department) that devices and users belong to. The platform supports several organizations and a hierarchy between them (levels).
- **Administrator**: a user marked as *Superuser*. Manages their own organization and those below it, never any others.
- **Tier**: the level an organization has contracted: *Watch*, *Operate* or *Orchestrate*.
- **Device**: any robot, IoT element or sensor registered in the platform. Devices fall into three categories: **Robot**, **IoT** and **Sensor** (cameras are sensors).
- **Connector**: the component that links the platform to a manufacturer's devices. If a failure comes from the connector, the platform shows it as *Connector error*.
- **Task**: an operation run by a robot (cleaning, delivery, etc.), with its own status, history and metrics.
- **Workflow**: an automation: when an event occurs, and if certain conditions are met, a robot receives a task.
- **Event**: something that has happened and is recorded: a task that ends, a robot that goes offline, an alarm, etc.
- **Scene**: the location (building and floor) where a device operates. A robot can be shown on its map.

## How this manual is organized

- **User guide**: explains each screen of the platform from the point of view of someone using it in the browser.
- **API reference**: documents the REST endpoints available to anyone who wants to integrate with Deliverance by code.
