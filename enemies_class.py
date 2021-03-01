import pygame
from pygame.math import Vector2
from useful_functions import load_image
import bullet_class
import main


class Enemy(pygame.sprite.Sprite):
    enemy_image = load_image("hero/gg1.png")

    def __init__(self, *group):
        super().__init__(*group)
        self.image = Enemy.enemy_image
        self.health = 2
        self.rect = self.image.get_rect()
        self.area_w = 100
        self.area_h = 100
        self.orig = self.image

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

    def set_attack_area(self, width, height):
        self.area_w = width
        self.area_h = height

    def fire(self, mouse_xy):
        bullet = bullet_class.Bullet((self.rect.center[0], self.rect.center[1]), mouse_xy, self, -20)
        bullet.rotate()
        bullet.set_group(main.bullets)
        bullet.set_group(main.all_not_hero)

    def update(self):
        if self.health <= 0:
            pygame.sprite.Sprite.kill(self)

    def attack_check(self, hero):
        x1, y1, w1, h1 = hero.rect.x, hero.rect.y, hero.rect.size[0], hero.rect.size[1]
        x2, y2, w2, h2 = self.rect.center[0] - self.area_w, self.rect.center[1] - self.area_h,\
                         2 * self.area_w, 2 * self.area_h
        if x1 + w1 < x2 or y1 + h1 < y2 or y1 > y2 + h2:
            return False
        return True

    def rotate(self, dest):
        x, y, w, h = self.rect
        direction = dest - Vector2(x + w//2, y + h//2)
        radius, angle = direction.as_polar()
        self.image = pygame.transform.rotate(self.orig, -angle - 90)
        self.rect = self.image.get_rect(center=self.rect.center)
        self.mask = pygame.mask.from_surface(self.image)
