import pygame as pg
from math import sin, cos
from settings import *

class RayCasting:
   def __init__(self, game) -> None:
      self.game = game
      self.ray_casting_result: list = []
      self.objects_to_render: list = []
      self.textures = self.game.object_renderer.wall_textures

   def get_objects_to_render(self) -> None:
      self.objects_to_render: list = []
      for ray, values in enumerate(self.ray_casting_result):
         depth, proj_height, texture, offset = values

         if proj_height < HEIGHT:
            wall_column = self.textures[texture].subsurface(
               offset * (TEXTURE_SIZE - SCALE), 0, SCALE, TEXTURE_SIZE
            )
            wall_column: pg.Surface = pg.transform.scale(wall_column, (SCALE, proj_height))
            wall_pos: tuple = (ray * SCALE, HALF_HEIGHT - proj_height // 2)
         else:
            texture_height = TEXTURE_SIZE * HEIGHT / proj_height
            wall_column = self.textures[texture].subsurface(
               offset * (TEXTURE_SIZE - SCALE), HALF_TEXTURE_SIZE - texture_height // 2, SCALE, texture_height
            )
            wall_column: pg.Surface = pg.transform.scale(wall_column, (SCALE, HEIGHT))
            wall_pos = (ray * SCALE, 0)

         self.objects_to_render.append((depth, wall_column, wall_pos))

   def ray_cast(self) -> None:
    self.ray_casting_result: list = []
    ox, oy = self.game.player.pos
    x_map, y_map = self.game.player.map_pos

    # Set a fixed texture for the entire wall (just choose one texture from self.textures)
    texture = 1  # Assuming you want texture with ID 1 (change this as needed)

    ray_angle = self.game.player.angle - HALF_FOV + 0.0001
    for ray in range(NUM_RAYS):
        sin_a = sin(ray_angle)
        cos_a = cos(ray_angle)

        # Horizontals
        y_hor, dy = (y_map + 1, 1) if sin_a > 0 else (y_map - 1e-6, -1)
        depth_hor = (y_hor - oy) / sin_a
        x_hor = ox + depth_hor * cos_a
        delta_depth = dy / sin_a
        dx = delta_depth * cos_a

        for i in range(MAX_DEPTH):
            tile_hor = int(x_hor), int(y_hor)
            if tile_hor in self.game.map.world_map:
                # We don't need to change the texture here since we're using the same one for all rays
                break
            x_hor += dx
            y_hor += dy
            depth_hor += delta_depth

        # Verticals
        x_vert, dx = (x_map + 1, 1) if cos_a > 0 else (x_map - 1e-6, -1)
        depth_vert = (x_vert - ox) / cos_a
        y_vert: float = oy + depth_vert * sin_a
        delta_depth = dx / cos_a
        dy = delta_depth * sin_a

        for i in range(MAX_DEPTH):
            tile_vert = int(x_vert), int(y_vert)
            if tile_vert in self.game.map.world_map:
                # We don't need to change the texture here either
                break
            x_vert += dx
            y_vert += dy
            depth_vert += delta_depth

        # Choose the closest depth and texture
        if depth_vert < depth_hor:
            depth = depth_vert
            y_vert %= 1
            offset = y_vert if cos_a > 0 else (1 - y_vert)
        else:
            depth = depth_hor
            x_hor %= 1
            offset = (1 - x_hor) if sin_a > 0 else x_hor

        # Remove fishbowl effect
        depth *= cos(self.game.player.angle - ray_angle)

        # Projection
        proj_height: float = SCREEN_DIST / (depth + 0.0001)

        # Ray casting result with the same texture for all rays
        self.ray_casting_result.append((depth, proj_height, texture, offset))
        self.objects_to_render.append(texture)

        ray_angle += DELTA_ANGLE


   def update(self) -> None:
      self.ray_cast()
      self.get_objects_to_render()