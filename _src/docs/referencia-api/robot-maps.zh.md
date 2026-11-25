# robot-maps {#robot-maps}

各场景的楼层、机器人地图及其标定。地图由连接器创建；通过 API 可以放置、重命名、标定和删除地图。

| 方法 | 路径 | 调用者 | 说明 |
| --- | --- | --- | --- |
| GET | `/api/v1/scenes/{scene_uid}/floors` | 用户 | 场景的楼层。 |
| POST | `/api/v1/scenes/{scene_uid}/floors` | 用户 | 创建楼层。如果索引已存在，返回 **409**。 |
| PUT | `/api/v1/floors/{floor_uid}` | 用户 | 修改楼层。 |
| DELETE | `/api/v1/floors/{floor_uid}` | 用户 | 删除楼层。如果有地图，返回 **409**。 |
| GET | `/api/v1/organizations/{organization_id}/robot-maps` | 用户 | 地图及其机器人（不含图像）。 |
| GET | `/api/v1/robot-maps/{map_uid}` | 用户 | 单个地图。 |
| PUT | `/api/v1/robot-maps/{map_uid}` | 用户 | 重命名地图或将其放置到楼层。 |
| DELETE | `/api/v1/robot-maps/{map_uid}` | 用户 | 删除地图。如果其中有机器人，返回 **409**。 |
| GET | `/api/v1/robot-maps/{map_uid}/image` | 用户 | PNG 或 JPEG 图像（带 ETag）。 |
| POST | `/api/v1/robot-maps/{map_uid}/calibration/preview` | 用户 | 试算标定，不保存。 |
| PUT | `/api/v1/robot-maps/{map_uid}/calibration` | 用户 | 保存标定（替换点对）。 |
| POST | `/api/v1/robot-maps/{map_uid}/calibration/live-pair` | 用户 | 使用机器人当前位置的点对，不保存。 |

*调用者* 的含义：见[简介](introduccion.md#who-can-call-each-endpoint)。

`calibration_level`：

| 值 | 含义 |
| --- | --- |
| `exact` | 厂商提供的比例 |
| `calibrated` | 用户提供的两个或更多点对 |
| `estimated` | 连接器提供的两个或更多点对 |
| `rough` | 仅一个点对和一个假定比例 |
| `none` | 未标定：不绘制位置 |

`world_to_pixel` 为 `[[a, b, tx], [c, d, ty]]`：`u = a·x + b·y + tx`，`v = c·x + d·y + ty`，从米换算为像素（`v` 向下）。`heading` 以弧度表示，从 +x 起逆时针方向。楼层中，`index` 0 为首层（地面层），负数为地下层。

## 示例：标定 {#example-calibrate}

```json
{
  "points": [
    {"pixel": [10, 20], "world": [0, 0]},
    {"pixel": [210, 20], "world": [10, 0]}
  ],
  "use_manual_on_exact": false
}
```

最多支持 50 个点对。响应包含 `world_to_pixel`、`calibration_level`、`calibration_error_m`、`resolution_m_per_px`、`rotation_deg` 和 `points`。如果机器人不在该地图上，或其位置已超过 120 秒，`live-pair` 返回 422。
