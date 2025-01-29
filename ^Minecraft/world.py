from settings import *
from world_objects.chunk import Chunk


class World:
   def __init__(self, app):
      self.app = app
      self.chunks = [None for _ in range(WORLD_VOL)]
      self.voxels = np.empty([WORLD_VOL, CHUNK_VOL], dtype='uint8')

   def build_chunks(self):
      pass

   def build_chunk_mesh(self):
      pass

   def update(self):
      pass

   def render(self):
      pass