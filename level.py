import pygame
from settings import TILE_SIZE
from sprites import Tile, Player, Coin

class Level:
    def __init__(self):
        # группа тайлов для удобного обновления отрисовки всех блоков
        self.tiles = pygame.sprite.Group()
        self.coins = pygame.sprite.Group()
        self.player_group = pygame.sprite.GroupSingle()
        self.setup_level()

    def setup_level(self):
        with open('level.txt', 'r') as file:
            level_map = [line.strip() for line in file.readlines()]

        #  row_idx-номер строки, row-сама строка
        for row_idx, row in enumerate(level_map):
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

    def update(self):
        self.player_group.update()
        self.handle_collisions()

