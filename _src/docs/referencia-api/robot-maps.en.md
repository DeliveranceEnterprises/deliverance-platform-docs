# robot-maps

Floors of each scene, robot maps and their calibration. Maps are created by the connectors; through the API they are placed, renamed, calibrated and deleted.

| Method | Path | Who | Description |
| --- | --- | --- | --- |
| GET | `/api/v1/scenes/{scene_uid}/floors` | User | Floors of a scene. |
| POST | `/api/v1/scenes/{scene_uid}/floors` | User | Creates a floor. **409** if the index already exists. |
| PUT | `/api/v1/floors/{floor_uid}` | User | Modifies it. |
| DELETE | `/api/v1/floors/{floor_uid}` | User | Deletes it. **409** if it has maps. |
| GET | `/api/v1/organizations/{organization_id}/robot-maps` | User | Maps, with their robots (no image). |
| GET | `/api/v1/robot-maps/{map_uid}` | User | One map. |
| PUT | `/api/v1/robot-maps/{map_uid}` | User | Renames it or places it on a floor. |
| DELETE | `/api/v1/robot-maps/{map_uid}` | User | Deletes it. **409** if there are robots on it. |
| GET | `/api/v1/robot-maps/{map_uid}/image` | User | PNG or JPEG image (with ETag). |
| POST | `/api/v1/robot-maps/{map_uid}/calibration/preview` | User | Tries a calibration without saving it. |
| PUT | `/api/v1/robot-maps/{map_uid}/calibration` | User | Saves the calibration (replaces the pairs). |
| POST | `/api/v1/robot-maps/{map_uid}/calibration/live-pair` | User | Pair with a robot's current position, without saving it. |

*Who* can call: see the [introduction](introduccion.md#who-can-call-each-endpoint).

`calibration_level`:

| Value | Meaning |
| --- | --- |
| `exact` | Manufacturer's scale |
| `calibrated` | Two or more pairs from a user |
| `estimated` | Two or more pairs from the connector |
| `rough` | A single pair and an assumed scale |
| `none` | Not calibrated: the position is not drawn |

`world_to_pixel` is `[[a, b, tx], [c, d, ty]]`: `u = a·x + b·y + tx`, `v = c·x + d·y + ty`, from meters to pixels (`v` downwards). `heading` is in radians, counterclockwise from +x. For floors, `index` 0 is the ground floor and negative values are basements.

## Example: calibrate

```json
{
  "points": [
    {"pixel": [10, 20], "world": [0, 0]},
    {"pixel": [210, 20], "world": [10, 0]}
  ],
  "use_manual_on_exact": false
}
```

Up to 50 pairs are accepted. The response contains `world_to_pixel`, `calibration_level`, `calibration_error_m`, `resolution_m_per_px`, `rotation_deg` and `points`. `live-pair` responds 422 if the robot is not on the map or its position is more than 120 seconds old.
