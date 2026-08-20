import pygame
from settings import (
    TILE_SIZE, GROUND_1_IMG,
    GROUND_2_IMG, PLATFORM_IMG,
    BLOCK_ACTIVE_IMG,
    PLAYER_STATIC, PLAYER_SPEED,
    PLAYER_WIDTH, PLAYER_HEIGHT,
    GRAVITY, BLOCK_ACTIVE_EMPTY, COIN_IMG,
    ENEMY_WIDTH, ENEMY_HEIGHT, ENEMY_SPEED, ENEMY_IMG,
    WIDTH, PLAYER_RUN, PLAYER_JUMP, PLAYER_DEATH
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
        # подготовка текстур
        self.img_static = pygame.transform.scale(
            pygame.image.load(PLAYER_STATIC).convert_alpha(),
            (PLAYER_WIDTH, PLAYER_HEIGHT)
        )
        self.img_run = pygame.transform.scale(
            pygame.image.load(PLAYER_RUN).convert_alpha(),
            (PLAYER_WIDTH, PLAYER_HEIGHT)
        )
        self.img_jump = pygame.transform.scale(
            pygame.image.load(PLAYER_JUMP).convert_alpha(),
            (PLAYER_WIDTH, PLAYER_HEIGHT)
        )
        self.img_death = pygame.transform.scale(
            pygame.image.load(PLAYER_DEATH).convert_alpha(),
            (PLAYER_WIDTH, PLAYER_HEIGHT)
        )
        self.image = self.img_static




        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.vx = 0
        self.vy = 0
        # находится ли персонаж на твердой поверхности
        self.on_ground = False
        self.score = 0
        self.lives = 3

        self.facing_left = False
        self.is_dead = False

    def update(self):
        if self.is_dead:
            self.image = self.img_death
            return

        if not self.on_ground:
            self.vy = self.vy + GRAVITY

        self.rect.x = self.rect.x + self.vx

        if self.vx < 0:
            self.facing_left = True
        elif self.vx > 0:
            self.facing_left = False

#         изображение по состоянию
        if not self.on_ground:
            current_img = self.img_jump
        elif self.vx != 0:
            current_img = self.img_run
        elif self.vx == 0 and self.on_ground:
            current_img = self.img_static

        if self.facing_left:
            self.image = pygame.transform.flip(current_img,
                                               True, False)
        else:
            self.image = current_img

class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()

        self.image = pygame.image.load(ENEMY_IMG).convert_alpha()
        self.image = pygame.transform.scale(
            self.image, (ENEMY_WIDTH, ENEMY_HEIGHT)
        )
        self.rect = self.image.get_rect()
        self.rect.x = x # координата x (расположение врага)
        self.rect.y = y # координата y (расположение врага)

        self.direction = 1 # направление движения (1-вправо, -1-влево)
        self.vx = ENEMY_SPEED * self.direction

    def reverse(self):
        self.direction *= -1
        self.vx = ENEMY_SPEED * self.direction

    #обновление каждый кадр
    def update(self):
        self.rect.x += self.vx
        if self.rect.right >= WIDTH or self.rect.left <= 0:
            self.reverse()







