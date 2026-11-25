# ¿Qué es Deliverance Platform? {#what-is-deliverance-platform}

Deliverance Platform es la plataforma que centraliza la gestión de dispositivos robóticos e IoT de una organización (robots, sensores, cámaras y medidores) en un único panel, sin importar el fabricante de cada dispositivo.

Desde la plataforma se puede activar y organizar dispositivos, monitorizar su operación en tiempo real, dar tareas a los robots, automatizarlas con workflows, consultar analíticas de uso y consumo, y administrar usuarios y organizaciones.

## Conceptos clave {#key-concepts}

Antes de navegar por el resto del manual conviene tener claros estos conceptos, que aparecen en casi todas las páginas:

- **Organización**: la entidad (cliente, sede, departamento) a la que pertenecen los dispositivos y usuarios. La plataforma soporta varias organizaciones y una jerarquía entre ellas (niveles).
- **Administrador**: un usuario con la marca *Superuser*. Gestiona su organización y las que cuelgan de ella, nunca las demás.
- **Tier**: el nivel contratado por una organización: *Watch*, *Operate* u *Orchestrate*.
- **Dispositivo**: cualquier robot, elemento IoT o sensor dado de alta en la plataforma. Se agrupan en tres categorías: **Robot**, **IoT** y **Sensor** (las cámaras son sensores).
- **Conector**: el componente que une la plataforma con los dispositivos de un fabricante. Si un fallo es del conector, la plataforma lo indica como *Connector error*.
- **Tarea**: una operación ejecutada por un robot (limpieza, entrega/reparto, etc.), con su propio estado, histórico y métricas.
- **Workflow**: una automatización: cuando ocurre un evento, y si se cumplen unas condiciones, un robot recibe una tarea.
- **Evento**: algo que ha ocurrido y queda registrado: una tarea que termina, un robot que se desconecta, una alarma, etc.
- **Escena**: la ubicación (edificio y planta) en la que opera un dispositivo. Un robot puede mostrarse sobre su mapa.

## Cómo está organizado este manual {#how-this-manual-is-organized}

- **Guía de uso**: explica cada pantalla de la plataforma desde el punto de vista de quien la usa en el navegador.
- **Referencia de API**: documenta los endpoints REST disponibles para quien quiera integrarse por código con Deliverance.
