import pygame
from settings import (
    TILE_SIZE, GROUND_1_IMG,
    GROUND_2_IMG, PLATFORM_IMG,
    BLOCK_ACTIVE_IMG,
    PLAYER_STATIC, PLAYER_SPEED,
    PLAYER_WIDTH, PLAYER_HEIGHT,
    GRAVITY, BLOCK_ACTIVE_EMPTY, COIN_IMG
)

class Tile(pygame.sprite.Sprite):
    def __init__(self, x, y, tile_type='ground1'):
        # наследование свойств родительского класса
        super().__init__()
        self.tile_type = tile_type
        if tile_type == 'ground1':
            self.image = pygame.image.load(GROUND_1_IMG).convert_alpha()
        elif tile_type == 'ground2':
            self.image = pygame.image.load(GROUND_2_IMG).convert_alpha()
        elif tile_type == 'platform':
            self.image = pygame.image.load(PLATFORM_IMG).convert_alpha()
        elif tile_type == 'block_active':
            self.image = pygame.image.load(BLOCK_ACTIVE_IMG).convert_alpha()

        self.image = pygame.transform.scale(
            self.image, (TILE_SIZE, TILE_SIZE)
        )
        # получаем хитбокс (прямоугольник)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def hit(self):
        if self.tile_type == 'block_active':
            self.tile_type = 'block_empty'
            self.image = pygame.image.load(BLOCK_ACTIVE_EMPTY).convert_alpha()
            self.image = pygame.transform.scale(
                self.image, (TILE_SIZE, TILE_SIZE)
            )
            return True # успешно выбили бонус
        return  False

class Coin(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load(COIN_IMG).convert_alpha()
        self.image = pygame.transform.scale(
            self.image, (32, 32)
        )
        self.rect = self.image.get_rect()
        self.rect.x = x + 16
        self.rect.y = y + 16

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load(PLAYER_STATIC).convert_alpha()
        self.image = pygame.transform.scale(
            self.image, (PLAYER_WIDTH, PLAYER_HEIGHT)
        )
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.vx = 0
        self.vy = 0
        # находится ли персонаж на твердой поверхности
        self.on_ground = False
        self.score = 0

    def update(self):
        if not self.on_ground:
            self.vy = self.vy + GRAVITY

        self.rect.x = self.rect.x + self.vx
