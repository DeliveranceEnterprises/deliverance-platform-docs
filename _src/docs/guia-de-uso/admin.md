# Admin: Panel de administrador

Gestión de usuarios y organizaciones. Solo aparece a los administradores, que gestionan **su organización y las que cuelgan de ella**.

## Users

![Usuarios](../assets/capturas/admin-users.png)

Lista de usuarios: nombre, email, organización, rol y estado. El menú de cada fila permite editarlo o borrarlo.

### Añadir un usuario

![Añadir un usuario](../assets/capturas/admin-add-user.png)

- **Email** y **Full name**.
- **Organization**: a qué organización pertenece.
- **Password** y **Confirm Password**: contraseña inicial.
- **Superuser**: administrador de su organización y de las que cuelgan de ella.
- **Active**: si se desmarca, no podrá iniciar sesión.

## Organizations

![Organizaciones](../assets/capturas/admin-organizations.png)

Las organizaciones por jerarquía, con su nivel y su tier. La propia está marcada como *Current* y sus acciones están desactivadas.

### Añadir una organización

![Añadir una organización](../assets/capturas/admin-add-organization.png)

Nombre, descripción, dirección y **Parent Organization**, la organización de la que cuelga.

## Tier de una organización

![Tier de una organización](../assets/capturas/admin-tier.png)

**Tier details** muestra el nivel contratado (*Watch*, *Operate* u *Orchestrate*), el fin de contrato, desde cuándo está en ese nivel, los robots en servicio, a quién se factura, la referencia del contrato y lo que incluye. El tier lo cambia Deliverance.

**Billed to** indica quién recibe la factura. El administrador de la organización padre puede incluir en la suya la de una organización hija con *Add its bill to...*

Estados: *Active*, *Ends soon*, *Expired* y *Suspended*. Que un contrato termine no cambia nada por sí solo. Cuando Deliverance **suspende** una organización, sus usuarios no pueden entrar en la plataforma; sus datos, conectores y workflows continúan.
