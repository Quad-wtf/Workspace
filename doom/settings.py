from math import pi, tan

# game settings
RES = WIDTH, HEIGHT = 1600, 900
HALF_WIDTH: int = WIDTH // 2
HALF_HEIGHT: int = HEIGHT // 2
FPS: int = 0

PLAYER_POS: tuple = 1.5, 5 # mini map
PLAYER_ANGLE: int = 0
PLAYER_SPEED: float = 0.004
PLAYER_ROT_SPEED: float = 0.002
PLAYER_SIZE_SCALE: int = 60

FOV: float = pi / 3
HALF_FOV: float = FOV / 2
NUM_RAYS: int = WIDTH // 2
HALF_NUM_RAYS: int = NUM_RAYS // 2
DELTA_ANGLE = FOV / NUM_RAYS
MAX_DEPTH = 20

SCREEN_DIST: float = HALF_WIDTH / tan(HALF_FOV)
SCALE: float = WIDTH // NUM_RAYS

TEXTURE_SIZE: int = 256
HALF_TEXTURE_SIZE: int =  TEXTURE_SIZE // 2