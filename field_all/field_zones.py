import pygame
import sys
import os
from useful_functions import load_image
import main


class Object(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__(main.all_sprites)

        self.shade_value = False
        self.width = 20
        self.height = 20

        self.image = None
        self.base_image = None
        if self.image is not None:
            self.rect = self.image.get_rect()
            self.rect.x = 0
            self.rect.y = 0

    def set_group(self, group):
        if type(group) == pygame.sprite.Group:
            self.add(group)
            return True
        return False

    def set_size(self, width, height):
        try:
            if width >= 0 and height >= 0:
                self.width = width
                self.height = height
                return True
            return False
        except Exception:
            return False

    def set_image(self, image_name):
        if type(image_name) == str:
            img = load_image(image_name)
            if type(img) != bool:
                self.base_image = img
                self.image = self.base_image.copy()
                self.rect = self.image.get_rect()
                self.rect.x = 0
                self.rect.y = 0
                self.mask = pygame.mask.from_surface(self.image)
                return True
        return False

    def shade(self, value):
        if type(value) == bool:
            if value:
                self.image.fill(pygame.Color(150, 150, 150), special_flags=pygame.BLEND_RGB_MULT)
                self.mask = pygame.mask.from_surface(self.image)
            else:
                self.image = self.base_image.copy()
                self.mask = pygame.mask.from_surface(self.image)
            self.shade_value = value
            return True
        return False


class VWall(Object):
    def __init__(self):
        super().__init__()
        self.set_group(main.barriers)
        self.set_image('field/vertical_wall.png')
        self.set_group(main.walls)


class HWall(Object):
    def __init__(self):
        super().__init__()
        self.set_group(main.barriers)
        self.set_image('field/horizontal_wall.png')
        self.set_group(main.walls)


class WNWall(Object):
    def __init__(self):
        super().__init__()
        self.set_group(main.barriers)
        self.set_image('field/wn_wall.png')
        self.set_group(main.walls)


class NEWall(Object):
    def __init__(self):
        super().__init__()
        self.set_group(main.barriers)
        self.set_image('field/ne_wall.png')
        self.set_group(main.walls)


class ESWall(Object):
    def __init__(self):
        super().__init__()
        self.set_group(main.barriers)
        self.set_image('field/es_wall.png')
        self.set_group(main.walls)


class SWWall(Object):
    def __init__(self):
        super().__init__()
        self.set_group(main.barriers)
        self.set_image('field/sw_wall.png')
        self.set_group(main.walls)


class ESWWall(Object):
    def __init__(self):
        super().__init__()
        self.set_group(main.barriers)
        self.set_image('field/esw_wall.png')
        self.set_group(main.walls)


class NESWall(Object):
    def __init__(self):
        super().__init__()
        self.set_group(main.barriers)
        self.set_image('field/nes_wall.png')
        self.set_group(main.walls)


class SWNWall(Object):
    def __init__(self):
        super().__init__()
        self.set_group(main.barriers)
        self.set_image('field/swn_wall.png')
        self.set_group(main.walls)


class WNEWall(Object):
    def __init__(self):
        super().__init__()
        self.set_group(main.barriers)
        self.set_image('field/wne_wall.png')
        self.set_group(main.walls)


class NESWWall(Object):
    def __init__(self):
        super().__init__()
        self.set_group(main.barriers)
        self.set_image('field/nesw_wall.png')
        self.set_group(main.walls)


class BPanel(Object):
    def __init__(self):
        super().__init__()
        self.set_image('field/black_panel.png')
        self.set_group(main.floor)


class WoodenRoom(Object):
    def __init__(self):
        super().__init__()
        self.set_size(140, 140)
        self.set_image('field/wooden_room.png')
        self.set_group(main.rooms)


class StoneRoom(Object):
    def __init__(self):
        super().__init__()
        self.set_size(180, 80)
        self.set_image('field/stone_room.png')
        self.set_group(main.rooms)


class ParquetRoom(Object):
    def __init__(self):
        super().__init__()
        self.set_size(240, 340)
        self.set_image('field/parquet_room.png')
        self.set_group(main.rooms)


class Billiard(Object):
    def __init__(self):
        super().__init__()
        self.set_group(main.barriers)
        self.set_size(100, 61)
        self.set_image('field/billiard.png')
        self.set_group(main.furniture)


class Poker(Object):
    def __init__(self):
        super().__init__()
        self.set_group(main.barriers)
        self.set_size(152, 146)
        self.set_image('field/poker_table.png')
        self.set_group(main.furniture)


class Field:
    def __init__(self, file=None):
        self.cell_size = 20
        self.startx, self.starty = 50, 50

        if file is None:
            self.board = [[WNWall(), HWall(),      HWall(),    HWall(), HWall(),  HWall(), HWall(), HWall(), NEWall(),  None,    WNWall(),  HWall(),       HWall(), HWall(), HWall(), HWall(), HWall(), HWall(), HWall(), HWall(), HWall(), HWall(), HWall(), NEWall()],
                          [VWall(),  WoodenRoom(), None,       None,    None,     None,    None,    None,    VWall(),   None,    VWall(),   ParquetRoom(), None,    None,    None,    None,    None,    None,    None,    None,    None,    None,    None,    VWall()],
                          [VWall(),  None,         None,       None,    None,     None,    None,    None,    VWall(),   None,    VWall(),   None,          None,    None,    None,    None,    None,    None,    None,    None,    None,    None,    None,    VWall()],
                          [VWall(),  None,         Billiard(), None,    None,     None,    None,    None,    VWall(),   None,    VWall(),   None,          None,    None,    None,    None,    None,    None,    None,    None,    None,    None,    None,    VWall()],
                          [VWall(),  None,         None,       None,    None,     None,    None,    None,    VWall(),   None,    VWall(),   None,          None,    None,    Poker(), None,    None,    None,    None,    None,    None,    None,    None,    VWall()],
                          [VWall(),  None,         None,       None,    None,     None,    None,    None,    VWall(),   None,    VWall(),   None,          None,    None,    None,    None,    None,    None,    None,    None,    None,    None,    None,    VWall()],
                          [VWall(),  None,         None,       None,    None,     None,    None,    None,    VWall(),   None,    VWall(),   None,          None,    None,    None,    None,    None,    None,    None,    None,    None,    None,    None,    VWall()],
                          [VWall(),  None,         None,       None,    None,     None,    None,    None,    VWall(),   None,    VWall(),   None,          None,    None,    None,    None,    None,    None,    None,    None,    None,    None,    None,    VWall()],
                          [NESWall(), HWall(),     HWall(),    HWall(), BPanel(), HWall(), HWall(), HWall(), WNEWall(), HWall(), SWNWall(), None,          None,    None,    None,    None,    None,    None,    None,    None,    None,    None,    None,    VWall()],
                          [VWall(),  StoneRoom(),  None,       None,    None,     None,    None,    None,    None,      None,    VWall(),   None,          None,    None,    None,    None,    None,    None,    None,    None,    None,    None,    None,    VWall()],
                          [VWall(),  None,         None,       None,    None,     None,    None,    None,    None,      None,    BPanel(),  None,          None,    None,    None,    None,    None,    None,    None,    None,    None,    None,    None,    VWall()],
                          [VWall(),  None,         None,       None,    None,     None,    None,    None,    None,      None,    BPanel(),  None,          None,    None,    None,    None,    None,    None,    None,    None,    None,    None,    None,    VWall()],
                          [VWall(),  None,         None,       None,    None,     None,    None,    None,    None,      None,    VWall(),   None,          None,    None,    None,    None,    None,    None,    None,    None,    None,    None,    None,    VWall()],
                          [SWWall(), HWall(),      HWall(),    HWall(), HWall(),  HWall(), HWall(), HWall(), HWall(),   HWall(), SWNWall(), None,          None,    None,    None,    None,    None,    None,    None,    None,    None,    None,    None,    VWall()],
                          [None,     None,         None,       None,    None,     None,    None,    None,    None,      None,    VWall(),   None,          None,    None,    None,    None,    None,    None,    None,    None,    None,    None,    None,    VWall()],
                          [None,     None,         None,       None,    None,     None,    None,    None,    None,      None,    VWall(),   None,          None,    None,    None,    None,    None,    None,    None,    None,    None,    None,    None,    VWall()],
                          [None,     None,         None,       None,    None,     None,    None,    None,    None,      None,    VWall(),   None,          None,    None,    None,    None,    None,    None,    None,    None,    None,    None,    None,    VWall()],
                          [None,     None,         None,       None,    None,     None,    None,    None,    None,      None,    VWall(),   None,          None,    None,    None,    None,    None,    None,    None,    None,    None,    None,    None,    VWall()],
                          [None,     None,         None,       None,    None,     None,    None,    None,    None,      None,    SWWall(),  HWall(),       HWall(), HWall(), HWall(), HWall(), HWall(), HWall(), HWall(), HWall(), HWall(), HWall(), HWall(), ESWall()]]
        else:
            pass

        self.width = len(self.board[0])
        self.height = len(self.board)

    def get_cell(self, cell_x, cell_y):
        try:
            x = (cell_x - self.startx) // self.cell_size
            y = (cell_y - self.starty) // self.cell_size
            cell = self.board[y][x]
            return cell
        except Exception:
            return False

    def render(self):
        pixel_w = self.width * self.cell_size + self.startx
        pixel_h = self.height * self.cell_size + self.starty
        for y in range(self.starty, pixel_h, self.cell_size):
            for x in range(self.startx, pixel_w, self.cell_size):
                cell = self.get_cell(x, y)
                if type(cell) == bool and cell is False:
                    return False
                if cell is not None:
                    cell.rect.x = x
                    cell.rect.y = y

    def move(self, hero, value_px):
        if pygame.key.get_pressed()[pygame.K_UP]:
            self.starty += value_px
            self.render()
            crossing = pygame.sprite.spritecollideany(hero, main.barriers)
            if crossing is not None and \
                    ('Wall' in crossing.__class__.__name__ or pygame.sprite.collide_mask(hero, crossing)):
                self.starty += -value_px

        if pygame.key.get_pressed()[pygame.K_DOWN]:
            self.starty -= value_px
            self.render()
            crossing = pygame.sprite.spritecollideany(hero, main.barriers)
            if crossing is not None and \
                    ('Wall' in crossing.__class__.__name__ or pygame.sprite.collide_mask(hero, crossing)):
                self.starty -= -value_px

        if pygame.key.get_pressed()[pygame.K_RIGHT]:
            self.startx -= value_px
            self.render()
            crossing = pygame.sprite.spritecollideany(hero, main.barriers)
            if crossing is not None and \
                    ('Wall' in crossing.__class__.__name__ or pygame.sprite.collide_mask(hero, crossing)):
                self.startx -= -value_px

        if pygame.key.get_pressed()[pygame.K_LEFT]:
            self.startx += value_px
            self.render()
            crossing = pygame.sprite.spritecollideany(hero, main.barriers)
            if crossing is not None and \
                    ('Wall' in crossing.__class__.__name__ or pygame.sprite.collide_mask(hero, crossing)):
                self.startx += -value_px
