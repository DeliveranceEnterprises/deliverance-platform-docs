# scenes {#scenes}

场景：设备运行所在的建筑。其楼层和地图见 [robot-maps](robot-maps.md)。

| 方法 | 路径 | 调用者 | 说明 |
| --- | --- | --- | --- |
| GET | `/api/v1/scenes/` | 用户 | 列出可访问的场景。 |
| POST | `/api/v1/scenes/` | 用户 | 创建场景。 |
| GET | `/api/v1/scenes/{scene_id}` | 用户 | 单个场景。 |
| PUT | `/api/v1/scenes/{scene_id}` | 用户 | 更新场景。 |
| DELETE | `/api/v1/scenes/{scene_id}` | 用户 | 删除场景。 |

*调用者* 的含义：见[简介](introduccion.md#who-can-call-each-endpoint)。

## `floorplan` 和 `items`：自由对象的实际结构 {#floorplan-and-items-free-objects-this-is-their-actual-shape}

架构中只写了 “object”，没有更多细节。实际结构是一个带有角点、墙壁和纹理的 3D 平面图：

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

`corners` 是带名称的点；`walls` 将两个角点相连，并带有纹理；
`items` 是放置在场景中的对象列表。


## 示例：创建场景 {#example-create-a-scene}

只有 `organization_id` 为必填：

```json
{"label": "Main building", "organization_id": "00000000-0000-4000-8000-000000000001"}
```

响应会增加 `uid`、`floorplan` 和 `items`。
