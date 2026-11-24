# scenes

Escenas: los edificios en los que operan los dispositivos. Sus plantas y mapas están en [robot-maps](robot-maps.md).

| Método | Ruta | Quién | Descripción |
| --- | --- | --- | --- |
| GET | `/api/v1/scenes/` | Usuario | Lista las escenas a su alcance. |
| POST | `/api/v1/scenes/` | Usuario | Crea una escena. |
| GET | `/api/v1/scenes/{scene_id}` | Usuario | Una escena. |
| PUT | `/api/v1/scenes/{scene_id}` | Usuario | La actualiza. |
| DELETE | `/api/v1/scenes/{scene_id}` | Usuario | La elimina. |

*Quién* puede llamar: ver la [introducción](introduccion.md#quien-puede-llamar-a-cada-endpoint).

## `floorplan` e `items`: objetos libres, esta es su forma real

El schema solo dice "object", sin más detalle. La forma real es un plano 3D con esquinas,
paredes y texturas:

```json
{
  "floorplan": {
    "corners": {
      "corner1": {"x": 0, "y": 0},
      "corner2": {"x": 400, "y": 0},
      "corner3": {"x": 400, "y": 300},
      "corner4": {"x": 0, "y": 300}
    },
    "walls": [
      {
        "corner1": "corner1",
        "corner2": "corner2",
        "frontTexture": {"url": "/plan3d/rooms/textures/wallmap.png", "stretch": true, "scale": 0},
        "backTexture": {"url": "/plan3d/rooms/textures/wallmap.png", "stretch": true, "scale": 0}
      }
    ],
    "wallTextures": [],
    "floorTextures": {},
    "newFloorTextures": {
      "corner1,corner2,corner3,corner4": {"url": "/plan3d/rooms/textures/hardwood.jpg", "scale": 100}
    }
  },
  "items": []
}
```

`corners` son puntos con nombre; `walls` conecta dos corners entre sí con su textura;
`items` es una lista de objetos colocados en la escena.


## Ejemplo: crear una escena

Solo `organization_id` es obligatorio:

```json
{"label": "Edificio principal", "organization_id": "00000000-0000-4000-8000-000000000001"}
```

La respuesta añade `uid`, `floorplan` e `items`.
