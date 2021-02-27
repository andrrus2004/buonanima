import pygame
from useful_functions import load_image
from bullet_all.bullet_class import *
import main


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