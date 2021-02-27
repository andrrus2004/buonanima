import pygame
from useful_functions import load_image
from hero_all.hero_class import *
import main


class Hero(pygame.sprite.Sprite):
    image_standart = load_image("hero/test_img.png")

    def __init__(self, *group):
        super().__init__(*group)
        self.image = Hero.image_standart
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0
        self.mask = pygame.mask.from_surface(self.image)

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

    def set_size(self, wide, high):
        self.image = pygame.transform.scale(self.image, (wide, high))

    def change_place(self, dx, dy):
        self.rect.x += dx
        self.rect.y += dy

    def fire(self, mouse_xy):
        bullet = Bullet((self.rect.x, self.rect.y), mouse_xy)
        bullet.set_group(main.bullets)
        bullet.set_group(main.all_not_hero)


class Enemy(pygame.sprite.Sprite):
    enemy_image = load_image("hero/test_img.png")

    def __init__(self, *group):
        super().__init__(*group)
        self.image = Enemy.enemy_image
        self.health = 20
        self.rect = self.image.get_rect()
        self.attack_area_r = 10

    def set_place(self, x, y):
        self.rect.x = x
        self.rect.y = y

    def set_hands(self, item, sprite_path):
        self.hands = item
        self.image = load_image(sprite_path)

    def set_size(self, wide, high):
        self.image = pygame.transform.scale(self.image, (wide, high))

    def taking_damage(self, damage):
        self.health -= damage

    def set_attack_area(self, radius):
        self.attack_area_r = radius

    def fire(self, mouse_xy):
        bullet = Bullet((self.rect.x, self.rect.y), mouse_xy)
        bullet.set_group(main.bullets)
        bullet.set_group(main.all_not_hero)

    def update(self):
        if self.health <= 0:
            pygame.sprite.Sprite.kill(self)


class Field:
    def __init__(self, file=None):
        self.cell_size = 20
        self.startx, self.starty = 50, 50

        if file is None:
            self.board = [[WNWall(), HWall(),      HWall(),    HWall(), HWall(),  HWall(), HWall(), HWall(), NEWall(),  None,    WNWall(),  HWall(),       HWall(), HWall(), HWall(), HWall(), HWall(), HWall(), HWall(), HWall(), HWall(), HWall(), HWall(), NEWall()],
                          [VWall(),  WoodenRoom(), None,       None,    None,     None,    None,    None,    VWall(),   None,    VWall(),  ParquetRoom(), None,    None,    None,    None,    None,    None,    None,    None,    None,    None,    None,    VWall()],
                          [VWall(),  None,         None,       None,    None,     None,    None,    None,    VWall(),   None,    VWall(),   None,          None,    None,    None,    None,    None,    None,    None,    None,    None,    None,    None,    VWall()],
                          [VWall(),  None,         Billiard(), None,    None,     None,    None,    None,    VWall(),   None,    VWall(),   None,          None,    None,    None,    None,    None,    None,    None,    None,    None,    None,    None,    VWall()],
                          [VWall(),  None,         None,       None,    None,     None,    None,    None,    VWall(),   None,    VWall(),   None,          None,    None,    None, None,    None,    None,    None,    None,    None,    None,    None,    VWall()],
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
            for el in main.all_not_hero:
                el.rect.y += value_px
            self.render()
            crossing = pygame.sprite.spritecollideany(hero, main.barriers)
            if crossing is not None and \
                    ('Wall' in crossing.__class__.__name__ or pygame.sprite.collide_mask(hero, crossing)):
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
                    ('Wall' in crossing.__class__.__name__ or pygame.sprite.collide_mask(hero, crossing)):
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
                    ('Wall' in crossing.__class__.__name__ or pygame.sprite.collide_mask(hero, crossing)):
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
                    ('Wall' in crossing.__class__.__name__ or pygame.sprite.collide_mask(hero, crossing)):
                self.startx += -value_px
                for el in main.all_not_hero:
                    el.rect.x -= value_px


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
        self.bullet_damage = 5
        self.sin_x = abs(self.delta_x) / (self.delta_x ** 2 + self.delta_y ** 2) ** 0.5
        self.sin_y = abs(self.delta_y) / (self.delta_x ** 2 + self.delta_y ** 2) ** 0.5

        self.speed_x = self.speed * self.sin_x
        self.speed_y = self.speed * self.sin_y

        self.exist = True

    def update(self):
        try:
            self.rect.x += round(self.speed_x * self.delta_x / abs(self.delta_x))
            self.rect.y += round(self.speed_y * self.delta_y / abs(self.delta_y))
        except ZeroDivisionError:
            pass
        if pygame.sprite.spritecollideany(self, main.walls):
            pygame.sprite.Sprite.kill(self)
        elif pygame.sprite.spritecollideany(self, main.enemies):
            for el in pygame.sprite.spritecollide(self, main.enemies, False):
                el.taking_damage(self.bullet_damage)
            pygame.sprite.Sprite.kill(self)


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
                self.rect.x = 0
                self.rect.y = 0
                self.mask = pygame.mask.from_surface(self.image)
                return True
        return False


pygame.init()
size = width, height = 700, 600
pygame.display.set_caption('Игровое поле')
screen = pygame.display.set_mode(size)

if __name__ == '__main__':

    game = Field()

    hero = Hero(main.all_sprites, main.hero_group)
    hero.set_place(343, 293)
    enemy = Enemy(main.all_sprites, main.enemies, main.all_not_hero)
    enemy.set_place(343, 200)
    MOVING = pygame.USEREVENT + 1
    pygame.time.set_timer(MOVING, 10)
    screen.fill(pygame.Color('white'))

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == MOVING:
                game.move(hero, 1)
                main.bullets.update()
                main.enemies.update()
                screen.fill(pygame.Color('white'))

            if event.type == pygame.MOUSEBUTTONDOWN:
                hero.fire(event.pos)

            if event.type == pygame.QUIT:
                running = False

        game.render()
        main.all_sprites.draw(screen)

        pygame.display.flip()
    pygame.quit()
