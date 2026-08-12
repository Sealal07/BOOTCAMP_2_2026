import pygame
from settings import TILE_SIZE
from sprites import Tile

class Level:
    def __init__(self):
        # группа тайлов для удобного обновления отрисовки всех блоков
        self.tiles = pygame.sprite.Group()
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



