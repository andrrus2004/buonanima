from hero_all.hero_class import *
from field_all.field_map import *
from centrirovanie2 import *
from enemies_class import *


class Heart(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__(main.all_sprites)
        self.width = 40
        self.height = 40
        self.shade_value = False
        img = load_image('field/result/heart.png')
        if type(img) != bool:
            self.base_image = img
            self.image = self.base_image.copy()
            self.rect = self.image.get_rect()
            self.rect.x = 0
            self.rect.y = 0
            self.mask = pygame.mask.from_surface(self.image)


class Charge(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__(main.all_sprites)
        self.width = 15
        self.height = 40
        self.shade_value = False
        img = load_image('field/result/charge.png')
        if type(img) != bool:
            self.base_image = img
            self.image = self.base_image.copy()
            self.rect = self.image.get_rect()
            self.rect.x = 0
            self.rect.y = 0
            self.mask = pygame.mask.from_surface(self.image)


class Interface:
    def __init__(self, hero, width, height):
        self.hero = hero
        self.health = list()
        for _ in range(hero.health_max):
            self.health.append(Heart())
        self.ammo = list()
        for _ in range(hero.ammo):
            self.ammo.append(Charge())
        self.width = width
        self.height = height

    def place_items(self):
        startx = 10
        starty = 10
        for i in range(len(self.health)):
            self.health[i].rect.x = startx + i * 50
            self.health[i].rect.y = starty

        for i in range(len(self.ammo)):
            self.ammo[i].rect.x = self.width - 15 - startx - i * 20
            self.ammo[i].rect.y = starty

    def update(self):
        ammo_new = hero.ammo
        health_new = hero.health
        for i in range(len(self.ammo) - 1, ammo_new - 1, -1):
            self.shade(self.ammo[i], True)
        for j in range(ammo_new - 1, -1, -1):
            self.shade(self.ammo[j], False)

        for i in range(len(self.health) - 1, health_new - 1, -1):
            self.shade(self.health[i], True)
        for j in range(health_new - 1, -1, -1):
            self.shade(self.health[j], False)

    def shade(self, item, value):
        if type(value) == bool:
            if value and not item.shade_value:
                item.image.fill(pygame.Color(100, 100, 100), special_flags=pygame.BLEND_RGB_MULT)
                item.mask = pygame.mask.from_surface(item.image)
            elif not value:
                item.image = item.base_image.copy()
                item.mask = pygame.mask.from_surface(item.image)
            item.shade_value = value
            return True
        return False


all_sprites = pygame.sprite.Group()
hero_group = pygame.sprite.Group()
barriers = pygame.sprite.Group()
walls = pygame.sprite.Group()
rooms = pygame.sprite.Group()
floor = pygame.sprite.Group()
furniture = pygame.sprite.Group()
bullets = pygame.sprite.Group()
enemies = pygame.sprite.Group()
all_not_hero = pygame.sprite.Group()

pygame.init()
size = width, height = 700, 600
absolute_centre = (width // 2, height // 2)
pygame.display.set_caption('Игровое поле')
screen = pygame.display.set_mode(size)

if __name__ == '__main__':

    game = Field()
    game.startx = -225
    game.starty = -540

    hero_group = pygame.sprite.Group()
    hero = Hero(main.all_sprites, main.hero_group)
    hero.set_size(2)
    hero.set_place(343, 293)
    fire = False

    inter = Interface(hero, width, height)
    inter.place_items()

    # enemy = Enemy(main.all_sprites, main.enemies, main.all_not_hero)
    # enemy.set_place(310, 200)

    MOVING = pygame.USEREVENT + 1
    pygame.time.set_timer(MOVING, 10)

    RELOAD = pygame.USEREVENT + 2
    pygame.time.set_timer(RELOAD, 3000)
    pygame.event.set_blocked(RELOAD)

    ATTACK = pygame.USEREVENT + 3
    pygame.time.set_timer(ATTACK, 1500)

    crosshair = pygame.sprite.Group()
    arrow = Crosshair(crosshair)
    arrow.set_image('crosshair/crosshair.png')
    arrow.set_size(20, 20)

    screen.fill(pygame.Color('white'))
    running = True
    while running:
        for event in pygame.event.get():

            if pygame.mouse.get_focused():
                arrow.update(pygame.mouse.get_pos())
                centrirovanye(game, arrow, hero, absolute_centre)

            if event.type == MOVING:
                game.move(hero, 1)
                main.bullets.update()
                main.enemies.update()
                screen.fill(pygame.Color('white'))

            if event.type == RELOAD:
                hero.ammo = 6
                pygame.event.set_blocked(RELOAD)

            if event.type == ATTACK:
                for el in main.enemies:
                    if el.attack_check(hero):
                        el.rotate(hero.get_pose())
                        el.fire(hero.rect.center)

            if event.type == pygame.MOUSEBUTTONDOWN and hero.ammo > 0:
                hero.fire(pygame.mouse.get_pos())
                if hero.ammo == 0:
                    pygame.event.set_allowed(RELOAD)
                    pygame.time.set_timer(RELOAD, 3000)

            if event.type == pygame.QUIT:
                running = False

        hero.rotate()

        game.render()

        main.all_sprites.draw(screen)

        crosshair.draw(screen)

        pygame.display.flip()
    pygame.quit()
