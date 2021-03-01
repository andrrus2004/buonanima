from hero_all.hero_class import *
from field_all.field_map import *
from centrirovanie2 import *
from enemies_class import *


def new_game():
    global game, hero_group, hero, fire, inter, MOVING, RELOAD, ATTACK, crosshair, arrow
    game = Field()
    game.startx = -225
    game.starty = -540

    hero_group = pygame.sprite.Group()
    hero = Hero(main.all_sprites, main.hero_group)
    hero.set_size(2)
    hero.set_health(3, 100)
    hero.set_place(343, 293)
    fire = False

    inter = Interface(hero, width, height)
    inter.place_items()

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


class StartButton(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__(menu_sprites)
        self.width = 170
        self.height = 75
        img = load_image('start_button.png')
        if type(img) != bool:
            self.image = img
            self.rect = self.image.get_rect()
            self.rect.x = 50
            self.rect.y = 115
            self.mask = pygame.mask.from_surface(self.image)
        color = pygame.Color('yellow')
        font = pygame.font.Font(None, 30)
        self.text = font.render('Начать игру', True, color)
        self.text_x = 135 - self.text.get_width() // 2
        self.text_y = 152 - self.text.get_height() // 2
        # screen.blit(text, (text_x, text_y))

    def click(self, pos):
        x, y = pos
        return self.rect.x <= x <= self.rect.x + self.width and self.rect.y <= y <= self.rect.y + self.height


class ExitButton(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__(menu_sprites)
        self.width = 170
        self.height = 75
        img = load_image('exit_button.png')
        if type(img) != bool:
            self.image = img
            self.rect = self.image.get_rect()
            self.rect.x = 50
            self.rect.y = 200
            self.mask = pygame.mask.from_surface(self.image)
        color = pygame.Color('yellow')
        font = pygame.font.Font(None, 35)
        self.text = font.render('Выход', True, color)
        self.text_x = 135 - self.text.get_width() // 2
        self.text_y = 237 - self.text.get_height() // 2

    def click(self, pos):
        x, y = pos
        return self.rect.x <= x <= self.rect.x + self.width and self.rect.y <= y <= self.rect.y + self.height


class Menu(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__(menu_sprites)
        self.width = 800
        self.height = 550
        self.shade_value = False
        img = load_image('menu.png')
        if type(img) != bool:
            self.base_image = img
            self.image = self.base_image.copy()
            self.rect = self.image.get_rect()
            self.rect.x = 0
            self.rect.y = 0
            self.mask = pygame.mask.from_surface(self.image)
        self.start_button = StartButton()
        self.exit_button = ExitButton()


all_sprites = pygame.sprite.Group()
menu_sprites = pygame.sprite.Group()
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
size = width, height = 800, 550
absolute_centre = (width // 2, height // 2)
pygame.display.set_caption('Игровое поле')
screen = pygame.display.set_mode(size)

if __name__ == '__main__':
    menu = Menu()
    is_menu = True

    screen.fill(pygame.Color('white'))
    running = True
    while running:
        for event in pygame.event.get():
            if not is_menu:
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

            if is_menu and event.type == pygame.MOUSEBUTTONDOWN:
                pos = event.pos
                if menu.start_button.click(pos):
                    is_menu = False
                    new_game()
                elif menu.exit_button.click(pos):
                    exit()

            if event.type == pygame.QUIT:
                running = False

        if not is_menu:
            inter.update()
            hero.rotate()
            game.render()
            main.all_sprites.draw(screen)
            crosshair.draw(screen)
        else:
            menu_sprites.draw(screen)
            screen.blit(menu.start_button.text, (menu.start_button.text_x, menu.start_button.text_y))
            screen.blit(menu.exit_button.text, (menu.exit_button.text_x, menu.exit_button.text_y))

        # crosshair.draw(screen)

        pygame.display.flip()
    pygame.quit()
