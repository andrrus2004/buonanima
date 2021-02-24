# from objects import *
import pygame
import sys
import os


def load_image(name, colorkey=None):
    fullname = os.path.join('assets', name)
    if not os.path.isfile(fullname):
        return False
    image = pygame.image.load(fullname)
    return image


class Object(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__(all_sprites)
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
                self.rect.x = 0
                self.rect.y = 0
                return True
        return False


class VWall(Object):
    def __init__(self):
        super().__init__()
        self.set_group(barriers)
        self.set_image('field/vertical_wall.png')
        self.set_group(walls)


class HWall(Object):
    def __init__(self):
        super().__init__()
        self.set_group(barriers)
        self.set_image('field/horizontal_wall.png')
        self.set_group(walls)


class WNWall(Object):
    def __init__(self):
        super().__init__()
        self.set_group(barriers)
        self.set_image('field/wn_wall.png')
        self.set_group(walls)


class NEWall(Object):
    def __init__(self):
        super().__init__()
        self.set_group(barriers)
        self.set_image('field/ne_wall.png')
        self.set_group(walls)


class ESWall(Object):
    def __init__(self):
        super().__init__()
        self.set_group(barriers)
        self.set_image('field/es_wall.png')
        self.set_group(walls)


class SWWall(Object):
    def __init__(self):
        super().__init__()
        self.set_group(barriers)
        self.set_image('field/sw_wall.png')
        self.set_group(walls)


class ESWWall(Object):
    def __init__(self):
        super().__init__()
        self.set_group(barriers)
        self.set_image('field/esw_wall.png')
        self.set_group(walls)


class NESWall(Object):
    def __init__(self):
        super().__init__()
        self.set_group(barriers)
        self.set_image('field/nes_wall.png')
        self.set_group(walls)


class SWNWall(Object):
    def __init__(self):
        super().__init__()
        self.set_group(barriers)
        self.set_image('field/swn_wall.png')
        self.set_group(walls)


class WNEWall(Object):
    def __init__(self):
        super().__init__()
        self.set_group(barriers)
        self.set_image('field/wne_wall.png')
        self.set_group(walls)


class NESWWall(Object):
    def __init__(self):
        super().__init__()
        self.set_group(barriers)
        self.set_image('field/nesw_wall.png')
        self.set_group(walls)


class BPanel(Object):
    def __init__(self):
        super().__init__()
        self.set_image('field/black_panel.png')
        self.set_group(floor)


class WoodenRoom(Object):
    def __init__(self):
        super().__init__()
        self.set_size(140, 140)
        self.set_image('field/wooden_room.png')
        self.set_group(rooms)


class StoneRoom(Object):
    def __init__(self):
        super().__init__()
        self.set_size(180, 80)
        self.set_image('field/stone_room.png')
        self.set_group(rooms)


class ParquetRoom(Object):
    def __init__(self):
        super().__init__()
        self.set_size(240, 340)
        self.set_image('field/parquet_room.png')
        self.set_group(rooms)


class Billiard(Object):
    def __init__(self):
        super().__init__()
        self.set_group(barriers)
        self.set_size(100, 61)
        self.set_image('field/billiard.png')
        self.set_group(furniture)


class Poker(Object):
    def __init__(self):
        super().__init__()
        self.set_group(barriers)
        self.set_size(152, 146)
        self.set_image('field/poker_table.png')
        self.set_group(furniture)


class Field:
    def __init__(self, file=None):
        self.width = 9
        self.height = 9
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

    def render(self, screen):
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


if __name__ == '__main__':
    pygame.init()
    size = width, height = 1200, 600
    screen = pygame.display.set_mode(size)

    all_sprites = pygame.sprite.Group()
    barriers = pygame.sprite.Group()
    walls = pygame.sprite.Group()
    rooms = pygame.sprite.Group()
    floor = pygame.sprite.Group()
    furniture = pygame.sprite.Group()

    game = Field()

    running = True
    screen.fill((255, 255, 255))
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        game.render(screen)
        all_sprites.draw(screen)
        pygame.display.flip()
    pygame.quit()
