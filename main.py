import pygame
import sys
import os


def load_image(name, colorkey=None):
    fullname = os.path.join('assets', name)
    if not os.path.isfile(fullname):
        return False
    image = pygame.image.load(fullname)
    return image


class Hero(pygame.sprite.Sprite):
    image_standart = load_image("hero/test_img.png")

    def __init__(self, *group):
        super().__init__(*group)
        self.image = Hero.image_standart
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0

        self.health_max = 100
        self.health_proc = 1
        self.health_current = self.health_max * self.health_proc

        self.hands = None

    def set_place(self, x, y):
        self.rect.x = x
        self.rect.y = y

    def set_health(self, health, procents=1):
        self.health = health
        self.health_proc = procents
        self.health_current = self.health_max * self.health_proc

    def set_hands(self, item, sprite_path):
        self.hands = item
        self.image = load_image(sprite_path)

    def fire(self, mouse_xy):
        bullet = Bullet((self.rect.x, self.rect.y), mouse_xy)
        bullet.set_group(bullets)


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


class Bullet(Object):
    def __init__(self, creator_pos, mouse_pos):
        super().__init__()
        self.image = load_image("hero/test_img.png")
        self.rect = self.image.get_rect()
        self.rect.x = creator_pos[0]
        self.rect.y = creator_pos[1]

        self.delta_x = mouse_pos[0] - self.rect.x
        self.delta_y = mouse_pos[1] - self.rect.y

        self.speed = 10
        self.sin_x = abs(self.delta_x) / (self.delta_x ** 2 + self.delta_y ** 2) ** 0.5
        self.sin_y = abs(self.delta_y) / (self.delta_x ** 2 + self.delta_y ** 2) ** 0.5

        self.speed_x = int(self.speed * self.sin_x)
        self.speed_y = int(self.speed * self.sin_y)

        self.exist = True

    def update(self):
        if self.exist:
            try:
                self.rect.x += self.speed_x * self.delta_x / abs(self.delta_x)
                self.rect.y += self.speed_y * self.delta_y / abs(self.delta_y)
            except ZeroDivisionError:
                pass


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

    def move(self, value_px):
        if pygame.key.get_pressed()[pygame.K_UP]:
            self.starty += value_px
            self.render(screen)
            if pygame.sprite.spritecollideany(hero, barriers) is not None:
                self.starty += -value_px

        if pygame.key.get_pressed()[pygame.K_DOWN]:
            self.starty -= value_px
            self.render(screen)
            if pygame.sprite.spritecollideany(hero, barriers) is not None:
                self.starty -= -value_px

        if pygame.key.get_pressed()[pygame.K_RIGHT]:
            self.startx -= value_px
            self.render(screen)
            if pygame.sprite.spritecollideany(hero, barriers) is not None:
                self.startx -= -value_px

        if pygame.key.get_pressed()[pygame.K_LEFT]:
            self.startx += value_px
            self.render(screen)
            if pygame.sprite.spritecollideany(hero, barriers) is not None:
                self.startx += -value_px


all_sprites = pygame.sprite.Group()
hero_group = pygame.sprite.Group()
barriers = pygame.sprite.Group()
walls = pygame.sprite.Group()
rooms = pygame.sprite.Group()
floor = pygame.sprite.Group()
furniture = pygame.sprite.Group()

if __name__ == '__main__':
    pygame.init()
    size = width, height = 700, 600
    pygame.display.set_caption('Игровое поле')
    screen = pygame.display.set_mode(size)

    game = Field()

    hero_group = pygame.sprite.Group()
    hero = Hero(all_sprites, hero_group)
    hero.set_place(343, 293)

    MOVING = pygame.USEREVENT + 1
    pygame.time.set_timer(MOVING, 1)
    screen.fill(pygame.Color('white'))

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == MOVING:
                game.move(1)
                screen.fill(pygame.Color('white'))

            if event.type == pygame.QUIT:
                running = False
        game.render(screen)
        all_sprites.draw(screen)
        pygame.display.flip()
    pygame.quit()
