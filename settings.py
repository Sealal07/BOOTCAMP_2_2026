import pygame
import os

WIDTH = 1024
HEIGHT = 768
FPS = 60

TILE_SIZE = 64
PLAYER_WIDTH = 64
PLAYER_HEIGHT = 64

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# print(BASE_DIR)
ASSETS_DIR = os.path.join(BASE_DIR, 'assets')
# print(ASSETS_DIR)

GROUND_1_IMG = os.path.join(ASSETS_DIR, 'tiles', 'ground.png')
GROUND_2_IMG = os.path.join(ASSETS_DIR, 'tiles', 'ground2.png')
PLATFORM_IMG = os.path.join(ASSETS_DIR, 'tiles', 'block.png')
BLOCK_ACTIVE_IMG = os.path.join(ASSETS_DIR, 'tiles', 'block_active.png')

