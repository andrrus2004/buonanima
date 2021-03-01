import main
from useful_functions import load_image
import pygame


class Heart(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__(main.all_sprites)
        self.width = 40
        self.height = 40
        self.shade_value = False
        img = load_image('field/heart.png')
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
        img = load_image('field/charge.png')
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
        ammo_new = self.hero.ammo
        health_new = self.hero.health
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
        super().__init__(main.menu_sprites)
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

    def click(self, pos):
        x, y = pos
        return self.rect.x <= x <= self.rect.x + self.width and self.rect.y <= y <= self.rect.y + self.height


class ExitButton(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__(main.menu_sprites)
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
        super().__init__(main.menu_sprites)
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
