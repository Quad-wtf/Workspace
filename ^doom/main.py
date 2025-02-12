from wad_data import WADData
from settings import *
import pygame as pg
import sys
from map_renderer import MapRenderer


class DoomEngine:
    def __init__(self, wad_path='doom/wad/DOOM.WAD'):
        self.wad_path = wad_path
        self.screen = pg.display.set_mode(WIN_RES)
        self.clock = pg.time.Clock()
        self.running = True
        self.dt = 1 / 60
        self.on_init()

    def on_init(self):
        self.wad_data = WADData(self, map_name='E1M1')
        self.map_renderer = MapRenderer(self)

    def update(self):
        self.dt = self.clock.tick()
        pg.display.flip()
        pg.display.set_caption(f'{self.clock.get_fps()}')

    def draw(self):
        self.screen.fill('black')
        self.map_renderer.draw()

    def check_events(self):
        for e in pg.event.get():
            if e.type == pg.QUIT:
                self.running = False

    def run(self):
        while self.running:
            self.check_events()
            self.update()
            self.draw()
        pg.quit()
        sys.exit()


if __name__ == '__main__':
    doom = DoomEngine()
    doom.run()
