import pygame
from settings import (
    TILE_SIZE, GROUND_1_IMG,
    GROUND_2_IMG, PLATFORM_IMG,
    BLOCK_ACTIVE_IMG
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



