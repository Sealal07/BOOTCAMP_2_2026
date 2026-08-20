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

is_menu = True
start_btn = pygame.Rect(WIDTH // 2 - 125,
                          HEIGHT // 2 + 30,
                          250, 60)


restart_btn = pygame.Rect(WIDTH // 2 - 125,
                          HEIGHT // 2 + 30,
                          250, 60)

running = True

# Главный игровой цикл
while running:
    clock.tick(FPS)
    # обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if is_menu and start_btn.collidepoint(event.pos):
                is_menu = False

            elif level.game_over and restart_btn.collidepoint(event.pos):
                level.restart()

    if is_menu:
        screen.fill((30, 30, 40))
        title_text = font.render('BOOTCAMP PLATFORMER',
                                 True, (255, 255, 0))
        title_rect = title_text.get_rect(center=(
                                        WIDTH // 2,
                                        HEIGHT // 2 - 100
                                    ))
        screen.blit(title_text, title_rect)

        desc_line = [
            'Добро  пожаловать в платформер!',
            'Управление: A/D-движение, Пробел-прыжок.',
            'Собирайте монеты, выбивайте бонусы и побеждайте врагов!'
        ]

        for i, line in enumerate(desc_line):
            desc_text = font.render(line,
                                    True,
                                    (220, 220, 220))
            desc_rect = desc_text.get_rect(center=(
                                        WIDTH // 2,
                                        HEIGHT // 2 - 60 + i * 35
                                    ))
            screen.blit(desc_text, desc_rect)

        pygame.draw.rect(screen, (0, 200, 100), start_btn)
        btn_start_text = font.render('СТАРТ',
                                     True, (255, 255, 255))
        btn_start_rect = btn_start_text.get_rect(center=(
                                                 start_btn.center
                                                  ))
        screen.blit(btn_start_text, btn_start_rect)

    else:
        if not level.game_over:
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
        lives_text = font.render(f'Жизни: {level.player.lives}',
                                 True, (255, 60, 50))
        screen.blit(score_text, (20, 20))
        screen.blit(lives_text, (20, 70))

        if level.game_over:
            overlay = pygame.Surface((WIDTH, HEIGHT),
                                     pygame.SRCALPHA)
            overlay.fill((0, 0, 0, 100))
            screen.blit(overlay, (0, 0))

            go_text = font.render('GAME OVER',
                                  True, (255, 50, 50))
            go_rect = go_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 -50))
            screen.blit(go_text, go_rect)

            pygame.draw.rect(screen, (0, 200, 100), restart_btn)
            btn_text = font.render('Начать',
                                   True, (255, 255, 255))
            btn_rect = btn_text.get_rect(center=restart_btn.center)
            screen.blit(btn_text, btn_rect)


    # обновляем экран для отображения изменений
    pygame.display.flip()

pygame.quit()
sys.exit()







