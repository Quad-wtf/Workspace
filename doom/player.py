from settings import *
import pygame as pg
from math import cos, sin, tau, tan

class Player:
   def __init__(self, game) -> None:
      self.game = game
      self.x, self.y = PLAYER_POS
      self.angle = PLAYER_ANGLE

   def movement(self) -> None:
      sin_a = sin(self.angle)
      cos_a = cos(self.angle)
      dx, dy = 0, 0
      speed = PLAYER_SPEED * self.game.delta_time
      speed_sin = speed * sin_a
      speed_cos = speed * cos_a

      keys = pg.key.get_pressed()
      if keys[pg.K_w]:
         dx += speed_cos
         dy += speed_sin
      if keys[pg.K_s]:
         dx += -speed_cos
         dy += -speed_sin
      if keys[pg.K_a]:
         dx += speed_sin
         dy += -speed_cos
      if keys[pg.K_d]:
         dx += -speed_sin
         dy += speed_cos

      self.check_wall_collision(dx, dy)

      if keys[pg.K_LEFT]:
         self.angle -= PLAYER_ROT_SPEED * self.game.delta_time
      if keys[pg.K_RIGHT]:
         self.angle += PLAYER_ROT_SPEED * self.game.delta_time
      self.angle %= tau

   def check_wall(self, x, y) -> bool:
      return (x, y) not in self.game.map.world_map
   
   def check_wall_collision(self, dx, dy) -> None:
      if self.check_wall(int(self.x + dx), int(self.y)):
         self.x += dx
      if self.check_wall(int(self.x), int(self.y + dy)):
         self.y += dy

   def draw(self) -> None:
      # pg.draw.line(self.game.screen, 'purple', (self.x * 100, self.y * 100), (self.x * 100 + WIDTH * cos(self.angle), self.y * 100 + WIDTH * sin(self.angle)), 2)
      pg.draw.circle(self.game.screen, 'red', (self.x * 100, self.y * 100), 15)

   def update(self) -> None:
      self.movement()

   @property
   def pos(self) -> None:
      return self.x, self.y
   
   @property
   def map_pos(self) -> None:
      return int(self.x), int(self.y)