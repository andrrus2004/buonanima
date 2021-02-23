import pygame
import sys
import os


def load_image(name, colorkey=None):
    fullname = os.path.join('assets', name)
    if not os.path.isfile(fullname):
        return False
    image = pygame.image.load(fullname)
    return image


class Creature(pygame.sprite.Sprite):
    image = load_image("field/gg.png")

    def __init__(self, group):
        super().__init__(group)
        self.image = Creature.image
        self.rect = self.image.get_rect()
        self.rect.x = 250
        self.rect.y = 250
        self.press = False

    def update(self, x, y):
        if not pygame.sprite.spritecollideany(self, walls):
            self.rect = self.rect.move(x, y)


class Object(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__(all_sprites)
        self.width = 20
        self.height = 20
        self.image = None
        self.barrier = False
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

    def set_barrier(self, barrier_value):
        if type(barrier_value) == bool:
            self.barrier = barrier_value
            return True
        return False


class VWall(Object):
    def __init__(self):
        super().__init__()
        self.set_barrier(True)
        self.set_image('field/vertical_wall.png')
        self.set_group(walls)


class HWall(Object):
    def __init__(self):
        super().__init__()
        self.set_barrier(True)
        self.set_image('field/horizontal_wall.png')
        self.set_group(walls)


class WNWall(Object):
    def __init__(self):
        super().__init__()
        self.set_barrier(True)
        self.set_image('field/wn_wall.png')
        self.set_group(walls)


class NEWall(Object):
    def __init__(self):
        super().__init__()
        self.set_barrier(True)
        self.set_image('field/ne_wall.png')
        self.set_group(walls)


class ESWall(Object):
    def __init__(self):
        super().__init__()
        self.set_barrier(True)
        self.set_image('field/es_wall.png')
        self.set_group(walls)


class SWWall(Object):
    def __init__(self):
        super().__init__()
        self.set_barrier(True)
        self.set_image('field/sw_wall.png')
        self.set_group(walls)


class WoodenRoom(Object):
    def __init__(self):
        super().__init__()
        self.set_size(140, 140)
        self.set_image('field/wooden_room.png')
        self.set_group(rooms)


class Field:
    def __init__(self, file=None):
        self.width = 9
        self.height = 9
        self.cell_size = 20
        self.startx, self.starty = 50, 50
        if file is None:
            self.board = [[WNWall(), HWall(),      HWall(), HWall(), HWall(), HWall(), HWall(), HWall(), NEWall()],
                          [VWall(),  WoodenRoom(), None,    None,    None,    None,    None,    None,    VWall()],
                          [VWall(),  None,         None,    None,    None,    None,    None,    None,    VWall()],
                          [VWall(),  None,         None,    None,    None,    None,    None,    None,    VWall()],
                          [VWall(),  None,         None,    None,    None,    None,    None,    None,    VWall()],
                          [VWall(),  None,         None,    None,    None,    None,    None,    None,    VWall()],
                          [VWall(),  None,         None,    None,    None,    None,    None,    None,    VWall()],
                          [VWall(),  None,         None,    None,    None,    None,    None,    None,    VWall()],
                          [SWWall(), HWall(),      HWall(), HWall(), None,    HWall(), HWall(), HWall(), ESWall()]]
        else:
            pass

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
    walls = pygame.sprite.Group()
    rooms = pygame.sprite.Group()
    hero = pygame.sprite.Group()
    gg = Creature(hero)

    game = Field()
    running = True
    TIMER = pygame.USEREVENT + 1
    pygame.time.set_timer(TIMER, 1)
    screen.fill((255, 255, 255))
    x, y = 0, 0
    right, left, up, down = False, False, False, False
    while running:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEMOTION:
                coords = event.pos
                deltax = (coords[0] - gg.rect.x) // 2
                deltay = (coords[1] - gg.rect.y) // 2
                game.startx = 50 - deltax
                game.starty = 50 - deltay
                gg.rect.x = gg.rect.x - deltax
                gg.rect.y = gg.rect.y - deltay
                print(gg.rect.x)
            if event.type == pygame.KEYDOWN:
                if event.key == 273:
                    down = True
                elif event.key == 274:
                    up = True
                elif event.key == 275:
                    right = True
                elif event.key == 276:
                    left = True
            if event.type == pygame.KEYUP:
                if event.key == 273:
                    down = False
                elif event.key == 274:
                    up = False
                elif event.key == 275:
                    right = False
                elif event.key == 276:
                    left = False
            if event.type == TIMER:
                if right:
                    game.startx -= 1
                if left:
                    game.startx += 1
                if up:
                    game.starty -= 1
                if down:
                    game.starty += 1
                screen.fill(pygame.Color('white'))
            if event.type == pygame.QUIT:
                running = False
        game.render(screen)
        all_sprites.draw(screen)
        hero.draw(screen)
        pygame.display.flip()
    pygame.quit()
