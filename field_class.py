import pygame
import sys
import os
from useful_functions import load_image
import main
from enemies_class import *


class Object(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__(main.all_sprites)

        self.width = 20
        self.height = 20

        self.image = None
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
                self.image = img
                self.rect = self.image.get_rect()
                self.set_size(*self.rect.size)
                self.rect.x = 0
                self.rect.y = 0
                self.mask = pygame.mask.from_surface(self.image)
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


class PorchRoom(Object):
    def __init__(self):
        super().__init__()
        self.set_size(180, 80)
        self.set_image('field/porch_room.png')
        self.set_group(main.rooms)


class GardenRoom(Object):
    def __init__(self):
        super().__init__()
        self.set_size(960, 2400)
        self.set_image('field/garden_room.png')
        self.set_group(main.rooms)


class HallRoom(Object):
    def __init__(self):
        super().__init__()
        self.set_image('field/hallway_room.png')
        self.set_group(main.rooms)


class CabinetRoom(Object):
    def __init__(self):
        super().__init__()
        self.set_size(240, 340)
        self.set_image('field/cabinet_room.png')
        self.set_group(main.rooms)


class Shrub1(Object):
    def __init__(self):
        super().__init__()
        self.set_group(main.barriers)
        self.set_image('field/shrub1.png')
        self.set_group(main.furniture)


class Shrub2(Object):
    def __init__(self):
        super().__init__()
        self.set_group(main.barriers)
        self.set_image('field/shrub2.png')
        self.set_group(main.furniture)


class Field:
    def __init__(self, file=None):
        self.cell_size = 20
        self.startx, self.starty = 50, 50

        if file is None:
            self.board = [[WNWall(),  HWall(),       HWall(), HWall(), HWall(), HWall(), HWall(), HWall(), HWall(), HWall(), HWall(),  HWall(),  HWall(),  HWall(),  HWall(), HWall(), HWall(), HWall(), HWall(), HWall(), HWall(), HWall(), HWall(),   HWall(),      HWall(),  HWall(),  HWall(), HWall(),  HWall(),  HWall(),  HWall(),  HWall(), HWall(),     HWall(), HWall(), NEWall()],
                          [VWall(),   HallRoom(),    None,    None,    None,    None,    None,    None,    None,    None,    None,     None,     None,     None,     None,    None,    None,    None,    None,    None,    None,    None,    None,      None,         None,     None,     None,    None,     None,     None,     None,     None,    None,        None,    None,    VWall()],
                          [VWall(),   None,          None,    None,    None,    None,    None,    None,    None,    None,    None,     None,     None,     None,     None,    None,    None,    None,    None,    None,    None,    None,    None,      Enemy(main.all_sprites, main.enemies, main.all_not_hero),         None,     None,     None,    None,     None,     None,     None,     None,    None,        None,    None,    VWall()],
                          [VWall(),   None,          None,    None,    None,    None,    None,    None,    None,    None,    None,     None,     None,     None,     None,    None,    None,    None,    None,    None,    None,    None,    None,      None,         None,     None,     None,    None,     None,     None,     None,     None,    None,        None,    None,    VWall()],
                          [VWall(),   None,          None,    None,    None,    None,    None,    None,    None,    None,    None,     None,     None,     None,     None,    None,    None,    None,    None,    None,    None,    None,    None,      None,         None,     None,     None,    None,     None,     None,     None,     None,    None,        None,    None,    VWall()],
                          [VWall(),   None,          None,    None,    None,    None,    None,    None,    None,    None,    Enemy(main.all_sprites, main.enemies, main.all_not_hero),     None,     None,     None,     None,    None,    None,    None,    None,    None,    None,    None,    None,      None,         None,     None,     None,    None,     None,     None,     None,     None,    None,        None,    None,    VWall()],
                          [VWall(),   None,          None,    None,    None,    None,    None,    None,    None,    None,    None,     None,     None,     None,     None,    None,    None,    None,    None,    None,    None,    None,    None,      None,         None,     None,     None,    None,     None,     None,     None,     None,    None,        None,    Enemy(main.all_sprites, main.enemies, main.all_not_hero),    VWall()],
                          [VWall(),   None,          None,    None,    None,    None,    None,    None,    None,    None,    None,     None,     None,     None,     None,    None,    None,    None,    None,    None,    None,    None,    None,      None,         None,     None,     None,    None,     None,     None,     None,     None,    None,        None,    None,    VWall()],
                          [VWall(),   None,          None,    None,    None,    None,    None,    None,    None,    None,    None,     None,     None,     None,     None,    None,    None,    None,    None,    None,    None,    None,    None,      None,         None,     None,     None,    None,     None,     None,     None,     None,    None,        None,    None,    VWall()],
                          [NESWall(), HWall(),       HWall(), HWall(), HWall(), HWall(), HWall(), HWall(), HWall(), HWall(), BPanel(), BPanel(), BPanel(), HWall(),  HWall(), HWall(), HWall(), HWall(), HWall(), HWall(), HWall(), HWall(), ESWWall(), HWall(),      HWall(),  HWall(),  HWall(), BPanel(), BPanel(), BPanel(), BPanel(), HWall(), HWall(),     HWall(), HWall(), SWNWall()],
                          [VWall(),   CabinetRoom(), None,    None,    None,    None,    None,    None,    None,    None,    None,     None,     None,     None,     None,    None,    None,    None,    None,    None,    None,    None,    VWall(),   PorchRoom(),  None,     None,     None,    None,     None,     None,     None,     None,    None,        None,    None,    VWall()],
                          [VWall(),   None,          None,    None,    Enemy(main.all_sprites, main.enemies, main.all_not_hero),    None,    None,    None,    None,    None,    None,     None,     None,     None,     None,    None,    None,    None,    None,    None,    None,    None,    VWall(),   None,         None,     None,     None,    None,     None,     None,     None,     None,    None,        None,    None,    VWall()],
                          [VWall(),   None,          None,    None,    None,    None,    None,    None,    None,    None,    None,     None,     None,     None,     None,    None,    None,    None,    None,    None,    None,    None,    VWall(),   None,         None,     None,     None,    None,     None,     None,     None,     None,    None,        None,    None,    VWall()],
                          [VWall(),   None,          None,    None,    None,    None,    None,    None,    None,    None,    None,     None,     None,     None,     None,    None,    None,    None,    None,    None,    None,    None,    VWall(),   None,         None,     None,     None,    None,     None,     None,     None,     None,    None,        None,    None,    VWall()],
                          [VWall(),   None,          None,    None,    None,    None,    None,    None,    None,    None,    None,     None,     None,     None,     None,    None,    None,    None,    None,    None,    None,    None,    VWall(),   None,         None,     None,     None,    None,     None,     None,     None,     None,    None,        None,    None,    VWall()],
                          [VWall(),   None,          None,    None,    None,    None,    None,    None,    Enemy(main.all_sprites, main.enemies, main.all_not_hero),    None,    None,     None,     None,     None,     None,    None,    None,    None,    None,    None,    None,    None,    NESWall(), HWall(),      HWall(),  HWall(),  HWall(), None,     None,     None,     None,     HWall(), HWall(),     HWall(), HWall(), SWNWall()],
                          [VWall(),   None,          None,    None,    None,    None,    None,    None,    None,    None,    None,     None,     None,     None,     None,    None,    None,    None,    None,    None,    None,    None,    VWall(),   GardenRoom(), None,     None,     Enemy(main.all_sprites, main.enemies, main.all_not_hero),    None,     None,     None,     None,     Enemy(main.all_sprites, main.enemies, main.all_not_hero),    None,        None,    None,    VWall()],
                          [VWall(),   None,          None,    None,    None,    None,    None,    None,    None,    None,    None,     None,     None,     None,     None,    None,    None,    None,    None,    None,    None,    None,    VWall(),   None,         None,     None,     None,    None,     None,     None,     None,     None,    None,        None,    None,    VWall()],
                          [VWall(),   None,          None,    None,    None,    None,    None,    None,    None,    None,    None,     None,     None,     None,     None,    None,    None,    None,    None,    None,    None,    None,    VWall(),   None,         None,     None,     None,    None,     None,     None,     None,     None,    None,        None,    None,    VWall()],
                          [VWall(),   None,          None,    None,    None,    None,    None,    None,    None,    None,    None,     None,     None,     None,     None,    None,    None,    None,    None,    None,    None,    None,    VWall(),   None,         None,     None,     None,    None,     None,     None,     None,     None,    None,        None,    None,    VWall()],
                          [VWall(),   None,          None,    None,    Enemy(main.all_sprites, main.enemies, main.all_not_hero),    None,    None,    None,    None,    None,    None,     None,     None,     None,     None,    None,    None,    None,    None,    None,    None,    None,    VWall(),   None,         None,     Shrub1(), None,    None,     None,     None,     None,     None,    Shrub1(),    None,    None,    VWall()],
                          [VWall(),   None,          None,    None,    None,    None,    None,    None,    None,    None,    None,     None,     None,     None,     None,    None,    None,    None,    None,    None,    None,    None,    VWall(),   None,         None,     None,     None,    None,     None,     None,     None,     None,    None,        None,    None,    VWall()],
                          [VWall(),   None,          None,    None,    None,    None,    None,    None,    None,    None,    None,     None,     None,     None,     None,    None,    Enemy(main.all_sprites, main.enemies, main.all_not_hero),    None,    None,    None,    None,    None,    VWall(),   None,         None,     None,     None,    None,     None,     None,     None,     None,    None,        None,    None,    VWall()],
                          [VWall(),   None,          None,    None,    None,    None,    None,    None,    None,    None,    None,     None,     None,     None,     None,    None,    None,    None,    None,    None,    None,    None,    VWall(),   None,         None,     None,     None,    None,     None,     None,     None,     None,    None,        None,    None,    VWall()],
                          [VWall(),   None,          None,    None,    None,    None,    None,    None,    None,    None,    None,     None,     None,     None,     None,    None,    None,    None,    None,    None,    None,    None,    VWall(),   None,         None,     None,     None,    None,     None,     None,     None,     None,    None,        None,    None,    VWall()],
                          [VWall(),   None,          None,    Enemy(main.all_sprites, main.enemies, main.all_not_hero),    None,    None,    None,    None,    None,    None,    None,     None,     None,     None,     None,    None,    None,    None,    None,    None,    None,    None,    VWall(),   None,         None,     None,     None,    None,     None,     None,     None,     None,    None,        None,    None,    VWall()],
                          [VWall(),   None,          None,    None,    None,    None,    None,    None,    None,    None,    None,     None,     None,     None,     None,    None,    None,    None,    None,    None,    None,    None,    VWall(),   None,         None,     None,     None,    None,     None,     None,     None,     None,    None,        None,    None,    VWall()],
                          [VWall(),   None,          None,    None,    None,    None,    None,    None,    None,    None,    None,     None,     None,     None,     None,    None,    None,    None,    None,    None,    None,    None,    VWall(),   None,         None,     None,     None,    None,     None,     None,     None,     None,    None,        None,    None,    VWall()],
                          [VWall(),   None,          None,    None,    None,    None,    None,    None,    None,    None,    None,     None,     None,     None,     Enemy(main.all_sprites, main.enemies, main.all_not_hero),    None,    None,    None,    None,    None,    None,    None,    VWall(),   None,         None,     None,     None,    None,     None,     None,     None,     None,    None,        None,    None,    VWall()],
                          [VWall(),   None,          None,    None,    None,    None,    None,    None,    None,    None,    None,     None,     None,     None,     None,    None,    None,    None,    None,    None,    None,    None,    VWall(),   None,         None,     None,     None,    None,     None,     None,     None,     None,    None,        None,    None,    VWall()],
                          [VWall(),   None,          None,    None,    None,    None,    None,    None,    None,    None,    None,     None,     None,     None,     None,    None,    None,    None,    None,    None,    None,    None,    VWall(),   None,         None,     None,     None,    None,     None,     None,     None,     None,    None,        None,    None,    VWall()],
                          [VWall(),   None,          None,    None,    None,    Enemy(main.all_sprites, main.enemies, main.all_not_hero),    None,    None,    None,    None,    None,     None,     None,     None,     None,    None,    None,    None,    None,    None,    None,    None,    VWall(),   None,         None,     None,     None,    None,     None,     None,     None,     None,    None,        None,    None,    VWall()],
                          [VWall(),   None,          None,    None,    None,    None,    None,    None,    None,    None,    None,     None,     None,     None,     None,    None,    None,    None,    None,    None,    None,    None,    VWall(),   None,         None,     None,     None,    None,     None,     None,     None,     None,    None,        None,    None,    VWall()],
                          [SWWall(),  HWall(),       HWall(), HWall(), HWall(), HWall(), HWall(), HWall(), HWall(), HWall(), HWall(),  HWall(),  HWall(),  HWall(),  HWall(), HWall(), HWall(), HWall(), HWall(), HWall(), HWall(), HWall(), SWNWall(),   None,         Shrub2(), None,     None,    None,     None,     None,     None,     None,    Shrub2(),    None,    None,    VWall()],
                          [None,      None,          None,    None,    None,    None,    None,    None,    None,    None,    None,     None,     None,     None,     None,    None,    None,    None,    None,    None,    None,    None,    VWall(),   None,         None,     None,     None,    None,     None,     None,     None,     None,    None,        None,    None,    VWall()],
                          [None,      None,          None,    None,    None,    None,    None,    None,    None,    None,    None,     None,     None,     None,     None,    None,    None,    None,    None,    None,    None,    None,    VWall(),   None,         None,     None,     None,    None,     None,     None,     None,     None,    None,        None,    None,    VWall()],
                          [None,      None,          None,    None,    None,    None,    None,    None,    None,    None,    None,     None,     None,     None,     None,    None,    None,    None,    None,    None,    None,    None,    VWall(),   None,         None,     None,     None,    None,     None,     None,     None,     None,    None,        None,    None,    VWall()],
                          [None,      None,          None,    None,    None,    None,    None,    None,    None,    None,    None,     None,     None,     None,     None,    None,    None,    None,    None,    None,    None,    None,    VWall(),   None,         None,     None,     None,    None,     None,     None,     None,     None,    None,        None,    None,    VWall()],
                          [None,      None,          None,    None,    None,    None,    None,    None,    None,    None,    None,     None,     None,     None,     None,    None,    None,    None,    None,    None,    None,    None,    VWall(),   None,         None,     None,     None,    None,     None,     None,     None,     None,    None,        None,    None,    VWall()],
                          [None,      None,          None,    None,    None,    None,    None,    None,    None,    None,    None,     None,     None,     None,     None,    None,    None,    None,    None,    None,    None,    None,    VWall(),   None,         None,     None,     None,    None,     None,     None,     None,     None,    None,        None,    None,    VWall()],
                          [None,      None,          None,    None,    None,    None,    None,    None,    None,    None,    None,     None,     None,     None,     None,    None,    None,    None,    None,    None,    None,    None,    VWall(),   None,         None,     None,     None,    None,     None,     None,     None,     None,    None,        None,    None,    VWall()],
                          [None,      None,          None,    None,    None,    None,    None,    None,    None,    None,    None,     None,     None,     None,     None,    None,    None,    None,    None,    None,    None,    None,    VWall(),   None,         None,     None,     None,    None,     None,     None,     None,     None,    None,        None,    None,    VWall()],
                          [None,      None,          None,    None,    None,    None,    None,    None,    None,    None,    None,     None,     None,     None,     None,    None,    None,    None,    None,    None,    None,    None,    VWall(),   None,         None,     None,     None,    None,     None,     None,     None,     None,    None,        None,    None,    VWall()],
                          [None,      None,          None,    None,    None,    None,    None,    None,    None,    None,    None,     None,     None,     None,     None,    None,    None,    None,    None,    None,    None,    None,    VWall(),   None,         None,     None,     None,    None,     None,     None,     None,     None,    None,        None,    None,    VWall()],
                          [None,      None,          None,    None,    None,    None,    None,    None,    None,    None,    None,     None,     None,     None,     None,    None,    None,    None,    None,    None,    None,    None,    VWall(),   None,         None,     None,     None,    None,     None,     None,     None,     None,    None,        None,    None,    VWall()],
                          [None,      None,          None,    None,    None,    None,    None,    None,    None,    None,    None,     None,     None,     None,     None,    None,    None,    None,    None,    None,    None,    None,    VWall(),   None,         None,     None,     None,    None,     None,     None,     None,     None,    None,        None,    None,    VWall()],
                          [None,      None,          None,    None,    None,    None,    None,    None,    None,    None,    None,     None,     None,     None,     None,    None,    None,    None,    None,    None,    None,    None,    SWWall(),  HWall(),      HWall(),  HWall(),  HWall(), HWall(),  HWall(),  HWall(),  HWall(),  HWall(), HWall(),     HWall(), HWall(), ESWall()]]
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
            for el in main.all_not_hero:
                el.rect.y += value_px
            self.render()
            crossing = pygame.sprite.spritecollideany(hero, main.barriers)
            if crossing is not None and \
                    ('Wall' in crossing.__class__.__name__ or
                     pygame.sprite.collide_mask(hero, crossing)) or \
                    pygame.sprite.spritecollideany(hero, main.enemies):
                self.starty += -value_px
                for el in main.all_not_hero:
                    el.rect.y -= value_px

        if pygame.key.get_pressed()[pygame.K_DOWN]:
            self.starty -= value_px
            for el in main.all_not_hero:
                el.rect.y -= value_px
            self.render()
            crossing = pygame.sprite.spritecollideany(hero, main.barriers)
            if crossing is not None and \
                    ('Wall' in crossing.__class__.__name__ or
                     pygame.sprite.collide_mask(hero, crossing)) or \
                    pygame.sprite.spritecollideany(hero, main.enemies):
                self.starty -= -value_px
                for el in main.all_not_hero:
                    el.rect.y -= -value_px

        if pygame.key.get_pressed()[pygame.K_RIGHT]:
            self.startx -= value_px
            for el in main.all_not_hero:
                el.rect.x -= value_px
            self.render()
            crossing = pygame.sprite.spritecollideany(hero, main.barriers)
            if crossing is not None and \
                    ('Wall' in crossing.__class__.__name__ or
                     pygame.sprite.collide_mask(hero, crossing)) or \
                    pygame.sprite.spritecollideany(hero, main.enemies):
                self.startx -= -value_px
                for el in main.all_not_hero:
                    el.rect.x -= -value_px

        if pygame.key.get_pressed()[pygame.K_LEFT]:
            self.startx += value_px
            for el in main.all_not_hero:
                el.rect.x += value_px
            self.render()
            crossing = pygame.sprite.spritecollideany(hero, main.barriers)
            if crossing is not None and \
                    ('Wall' in crossing.__class__.__name__ or
                     pygame.sprite.collide_mask(hero, crossing)) or \
                    pygame.sprite.spritecollideany(hero, main.enemies):
                self.startx += -value_px
                for el in main.all_not_hero:
                    el.rect.x -= value_px
