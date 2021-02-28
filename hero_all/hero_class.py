import pygame as pg
from useful_functions import load_image
from pygame.math import Vector2
from bullet_all.bullet_class import *
import main


class Hero(pygame.sprite.Sprite):

    def __init__(self, *group):
        super().__init__(*group)
        self.image = load_image("hero/gg.png", -1).convert()
        colorkey = self.image.get_at((0, 0))
        self.image.set_colorkey(colorkey)
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0
        self.mask = pygame.mask.from_surface(self.image)

        self.orig = self.image

        self.health_max = 100
        self.health_proc = 1
        self.health_current = self.health_max * self.health_proc

        self.ammo = 6

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

    def set_size(self, n):
        w, h = self.rect[-2:]
        if n >= 0:
            self.image = pygame.transform.scale(self.image, (round(w * n), round(h * n)))
            return
        self.image = pygame.transform.scale(self.image, (round(w // abs(n)), round(h // abs(n))))
        self.orig = self.image

    def change_place(self, dx, dy):
        self.rect.x += dx
        self.rect.y += dy

    def rotate(self):
        x, y, w, h = self.rect
        direction = pg.mouse.get_pos() - Vector2(x + w//2, y + h//2)
        radius, angle = direction.as_polar()
        self.image = pg.transform.rotate(self.orig, -angle - 90)
        self.rect = self.image.get_rect(center=self.rect.center)

        '''mouse_x, mouse_y = pygame.mouse.get_pos()
        rel_x, rel_y = mouse_x - self.rect.center[0], mouse_y - self.rect.center[1]
        nor_x, nor_y = (self.rect.topleft[0] + self.rect.width // 2) - self.rect.center[0], (self.rect.topleft[1] + self.rect.width // 2) - self.rect.center[1]
        print([rel_x, rel_y, nor_x, nor_y])
        cursor_v = (rel_x, rel_y)
        normal_v = (nor_x, nor_y)
        t = (rel_x * nor_x + rel_y * nor_y) / (((rel_x * rel_x + rel_y * rel_y) ** 0.5) * ((nor_x * nor_x + nor_y * nor_y) * 0.5))
        if t < 0:
            t = -t
        q = 1.5707963267 - round(math.acos(t), 6)
        print(q)
        #self.image, self.rect = rot_center(self.image, self.rect, q)'''


    def fire(self, mouse_xy):
        if pygame.mouse.get_pressed(num_buttons=3)[0]:
            bullet = Bullet((self.rect.x, self.rect.y), mouse_xy, -20)
            bullet.rotate()
            bullet.set_group(main.bullets)
            bullet.set_group(main.all_not_hero)
            self.ammo -= 1
