import pygame
from useful_functions import load_image
from bullet_all.bullet_class import Bullet
import main


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
        bullet.set_group(main.bullets)
