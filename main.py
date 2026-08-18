import sys
import pygame
from level import Level
from settings import WIDTH, HEIGHT, FPS, PLAYER_SPEED, JUMP_FORCE

# 1. инициализация всех модулей Pygame

pygame.init()
pygame.font.init()
font = pygame.font.SysFont('Arial', 42)

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

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] or keys[pygame.K_a]:
        level.player.vx = -PLAYER_SPEED
    elif keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        level.player.vx = PLAYER_SPEED
    else:
        level.player.vx = 0

    if keys[pygame.K_SPACE] and level.player.on_ground:
        level.player.vy = JUMP_FORCE
        level.player.on_ground = False

    level.update()

    screen.fill((131, 216, 255)) # rgb
    # level.tiles.draw(screen)
    # level.coins.draw(screen)
    # level.enemies.draw(screen)
    # level.player_group.draw(screen)
    level.draw(screen)
    score_text = font.render(f'Очки: {level.player.score}',
                             True, (255, 215, 0))
    screen.blit(score_text, (20, 20))
    # обновляем экран для отображения изменений
    pygame.display.flip()

pygame.quit()
sys.exit()







