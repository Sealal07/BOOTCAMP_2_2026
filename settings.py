import pygame
import os

WIDTH = 1024
HEIGHT = 768
FPS = 60

TILE_SIZE = 64
PLAYER_WIDTH = 64
PLAYER_HEIGHT = 64

PLAYER_SPEED = 5 # скорость персонажа

GRAVITY = 0.6 # сила гравитации
JUMP_FORCE = -16 # сила прыжка


ENEMY_WIDTH = 60
ENEMY_HEIGHT = 60
ENEMY_SPEED = 2

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# print(BASE_DIR)
ASSETS_DIR = os.path.join(BASE_DIR, 'assets')
# print(ASSETS_DIR)

GROUND_1_IMG = os.path.join(ASSETS_DIR, 'tiles', 'ground.png')
GROUND_2_IMG = os.path.join(ASSETS_DIR, 'tiles', 'ground2.png')
PLATFORM_IMG = os.path.join(ASSETS_DIR, 'tiles', 'block.png')
BLOCK_ACTIVE_IMG = os.path.join(ASSETS_DIR, 'tiles', 'block_active.png')

PLAYER_STATIC = os.path.join(ASSETS_DIR, 'player', 'player_static.png')
PLAYER_RUN = os.path.join(ASSETS_DIR, 'player', 'player_run.png')
PLAYER_JUMP = os.path.join(ASSETS_DIR, 'player', 'player_jump.png')
PLAYER_DEATH = os.path.join(ASSETS_DIR, 'player', 'player_death.png')




BLOCK_ACTIVE_EMPTY = os.path.join(ASSETS_DIR, 'tiles', 'block_empty.png')
COIN_IMG = os.path.join(ASSETS_DIR, 'ui', 'coin.png')
ENEMY_IMG = os.path.join(ASSETS_DIR, 'enemy', 'enemy_static.png')