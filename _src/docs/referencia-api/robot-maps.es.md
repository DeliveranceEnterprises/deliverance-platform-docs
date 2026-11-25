# robot-maps {#robot-maps}

Plantas de cada escena, mapas de los robots y su calibración. Los mapas los crean los conectores; por la API se colocan, se renombran, se calibran y se borran.

| Método | Ruta | Quién | Descripción |
| --- | --- | --- | --- |
| GET | `/api/v1/scenes/{scene_uid}/floors` | Usuario | Plantas de una escena. |
| POST | `/api/v1/scenes/{scene_uid}/floors` | Usuario | Crea una planta. **409** si el índice ya existe. |
| PUT | `/api/v1/floors/{floor_uid}` | Usuario | La modifica. |
| DELETE | `/api/v1/floors/{floor_uid}` | Usuario | La elimina. **409** si tiene mapas. |
| GET | `/api/v1/organizations/{organization_id}/robot-maps` | Usuario | Mapas, con sus robots (sin imagen). |
| GET | `/api/v1/robot-maps/{map_uid}` | Usuario | Un mapa. |
| PUT | `/api/v1/robot-maps/{map_uid}` | Usuario | Lo renombra o lo coloca en una planta. |
| DELETE | `/api/v1/robot-maps/{map_uid}` | Usuario | Lo elimina. **409** si hay robots en él. |
| GET | `/api/v1/robot-maps/{map_uid}/image` | Usuario | Imagen PNG o JPEG (con ETag). |
| POST | `/api/v1/robot-maps/{map_uid}/calibration/preview` | Usuario | Prueba una calibración sin guardarla. |
| PUT | `/api/v1/robot-maps/{map_uid}/calibration` | Usuario | Guarda la calibración (sustituye los pares). |
| POST | `/api/v1/robot-maps/{map_uid}/calibration/live-pair` | Usuario | Par con la posición actual de un robot, sin guardarlo. |

*Quién* puede llamar: ver la [introducción](introduccion.md#who-can-call-each-endpoint).

`calibration_level`:

| Valor | Significado |
| --- | --- |
| `exact` | Escala del fabricante |
| `calibrated` | Dos o más pares de un usuario |
| `estimated` | Dos o más pares del conector |
| `rough` | Un solo par y una escala supuesta |
| `none` | Sin calibrar: no se dibuja la posición |

`world_to_pixel` es `[[a, b, tx], [c, d, ty]]`: `u = a·x + b·y + tx`, `v = c·x + d·y + ty`, de metros a píxeles (`v` hacia abajo). `heading` va en radianes, en sentido antihorario desde +x. En las plantas, `index` 0 es la baja y los negativos son sótanos.

## Ejemplo: calibrar {#example-calibrate}

```json
{
  "points": [
    {"pixel": [10, 20], "world": [0, 0]},
    {"pixel": [210, 20], "world": [10, 0]}
  ],
  "use_manual_on_exact": false
}
```

Se admiten hasta 50 pares. La respuesta trae `world_to_pixel`, `calibration_level`, `calibration_error_m`, `resolution_m_per_px`, `rotation_deg` y `points`. `live-pair` responde 422 si el robot no está en el mapa o su posición tiene más de 120 segundos.
