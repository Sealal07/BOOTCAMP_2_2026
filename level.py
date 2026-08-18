import pygame
from settings import TILE_SIZE, HEIGHT, WIDTH
from sprites import Tile, Player, Coin, Enemy

class Camera:
    # класс для отслеживания игрока и смещения мира
    def __init__(self, width, height):
        self.camera = pygame.Rect(0, 0, width, height)
        self.width = width
        self.height = height

    # смещает rect любого объекта на велечину сдвига камеры
    def apply(self, entity):
        return entity.rect.move(self.camera.topleft)

    #Центрируем камеру на игроке
    def update(self, target):
        x = -target.rect.centerx + int(WIDTH / 2)
        y = -target.rect.centery + int(HEIGHT / 2)
        x = min(0, x) #левая граница
        y = min(0, y) #верхняя граница
        self.camera.topleft = (x, y)



class Level:
    def __init__(self):
        # группа тайлов для удобного обновления отрисовки всех блоков
        self.tiles = pygame.sprite.Group()
        self.coins = pygame.sprite.Group()
        self.enemies = pygame.sprite.Group()
        self.player_group = pygame.sprite.GroupSingle()
        self.setup_level()

        # ИНИЦИАЛИЗАЦИЯ КАМЕРЫ
        # общая ширина уровня на основе длины карты
        level_pixel_width = len(self.level_map[0])*TILE_SIZE
        level_pixel_height = len(self.level_map)*TILE_SIZE
        self.camera = Camera(level_pixel_width, level_pixel_height)

    def setup_level(self):
        with open('level.txt', 'r') as file:
            self.level_map = [line.strip() for line in file.readlines()]

        #  row_idx-номер строки, row-сама строка
        for row_idx, row in enumerate(self.level_map):
            #  col_idx-номер колонки, col-символ
            for col_idx, col in enumerate(row):
                x = col_idx * TILE_SIZE
                y = row_idx * TILE_SIZE
                if col == '1':
                    tile = Tile(x, y, 'ground1')
                    self.tiles.add(tile)
                elif col == '2':
                    tile = Tile(x, y, 'ground2')
                    self.tiles.add(tile)
                elif col == '3':
                    tile = Tile(x, y, 'platform')
                    self.tiles.add(tile)
                elif col == '4':
                    tile = Tile(x, y, 'block_active')
                    self.tiles.add(tile)
                elif col == '5':
                    self.coins.add(Coin(x, y))
                elif col == 'X':
                    self.enemies.add(Enemy(x, y))


        self.player = Player(100, 500)
        self.player_group.add(self.player)

    def handle_collisions(self):
    # логика столкновения игрока с твердой землей
        player = self.player
        hits = pygame.sprite.spritecollide(player, self.tiles, False)
        for hit in hits:
            if player.vx > 0:
                player.rect.right = hit.rect.left
            elif player.vx < 0:
                player.rect.left = hit.rect.right

        player.rect.y = player.rect.y + player.vy
        player.on_ground = False
        hits = pygame.sprite.spritecollide(player, self.tiles, False)
        for hit in hits:
            if player.vy > 0:
                player.rect.bottom = hit.rect.top
                player.vy = 0
                player.on_ground = True
            elif player.vy < 0:
                player.rect.top = hit.rect.bottom
                player.vy = 0
                if hit.tile_type == 'block_active':
                    if hit.hit():
                        player.score += 50
        coin_hits = pygame.sprite.spritecollide(player, self.coins, True)
        for coin in coin_hits:
            player.score += 10

        # столкновение врагов со стенами
        for enemy in self.enemies:
            if pygame.sprite.spritecollideany(enemy, self.tiles):
                enemy.reverse()

        #  битва: игрок vs враг
        enemy_hits = pygame.sprite.spritecollide(player,self.enemies, False)
        for enemy in enemy_hits:
            if player.vy > 0 and player.rect.bottom <= enemy.rect.centery + 10:
                enemy.kill()
                player.vy = -10 # эффект отскока
                player.score += 100
            else:
                player.score = max(0, player.score - 50)
                player.rect.x = 100
                player.rect.y = 300
                player.vy = 0

    def update(self):
        self.player_group.update()
        self.enemies.update()
        self.handle_collisions()
        self.camera.update(self.player)

    def draw(self, surface):
        # метод отрисовки всех спрайтов со сдвигом камеры
        for sprite in self.tiles:
            surface.blit(sprite.image, self.camera.apply(sprite))
        for sprite in self.coins:
            surface.blit(sprite.image, self.camera.apply(sprite))
        for sprite in self.enemies:
            surface.blit(sprite.image, self.camera.apply(sprite))
        for sprite in self.player_group:
            surface.blit(sprite.image, self.camera.apply(sprite))



