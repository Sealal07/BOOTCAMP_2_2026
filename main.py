import sys
import pygame
from level import Level
from settings import WIDTH, HEIGHT, FPS

# 1. инициализация всех модулей Pygame

pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption('Bootcamp Platformer')

# таймер для контроля частоты кадров
clock = pygame.time.Clock()


level = Level()

running = True

# Главный игровой цикл
while running:
    clock.tick(FPS)
    # обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((0, 100, 250)) # rgb
    level.tiles.draw(screen)
    # обновляем экран для отображения изменений
    pygame.display.flip()

pygame.quit()
sys.exit()







