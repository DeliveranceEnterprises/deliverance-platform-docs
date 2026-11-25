# scenes

Scenes: the buildings where the devices operate. Their floors and maps are in [robot-maps](robot-maps.md).

| Method | Path | Who | Description |
| --- | --- | --- | --- |
| GET | `/api/v1/scenes/` | User | Lists the scenes within reach. |
| POST | `/api/v1/scenes/` | User | Creates a scene. |
| GET | `/api/v1/scenes/{scene_id}` | User | One scene. |
| PUT | `/api/v1/scenes/{scene_id}` | User | Updates it. |
| DELETE | `/api/v1/scenes/{scene_id}` | User | Deletes it. |

*Who* can call: see the [introduction](introduccion.md#who-can-call-each-endpoint).

## `floorplan` and `items`: free objects, this is their actual shape

The schema only says "object", with no more detail. The actual shape is a 3D plan with corners,
walls and textures:

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

`corners` are named points; `walls` connects two corners to each other with its texture;
`items` is a list of objects placed in the scene.


## Example: create a scene

Only `organization_id` is required:

```json
{"label": "Main building", "organization_id": "00000000-0000-4000-8000-000000000001"}
```

The response adds `uid`, `floorplan` and `items`.
