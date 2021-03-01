from field_class import *
import pygame as pg
from pygame.math import Vector2
import main
import hero_class
import enemies_class


class Bullet(Object):
    def __init__(self, creator_pos, mouse_pos, shooter, n=1):
        super().__init__()
        self.image = load_image("bullets/bullet.png")
        self.orig = self.image

        self.rect = self.image.get_rect()
        self.rect.x = creator_pos[0]
        self.rect.y = creator_pos[1]

        self.dest_x = mouse_pos[0]
        self.dest_y = mouse_pos[1]
        self.delta_x = self.dest_x - self.rect.x
        self.delta_y = self.dest_y - self.rect.y

        self.speed = 15
        self.bullet_damage = 1
        self.sin_x = abs(self.delta_x) / (self.delta_x ** 2 + self.delta_y ** 2) ** 0.5
        self.sin_y = abs(self.delta_y) / (self.delta_x ** 2 + self.delta_y ** 2) ** 0.5

        self.speed_x = self.speed * self.sin_x
        self.speed_y = self.speed * self.sin_y

        self.shooter = shooter

        self.exist = True

    def rotate(self):
        x, y, w, h = self.rect
        direction = (self.dest_x, self.dest_y) - Vector2(x + w//2, y + h//2)
        radius, angle = direction.as_polar()
        self.image = pg.transform.rotate(self.orig, -angle - 90)
        self.rect = self.image.get_rect(center=self.rect.center)

    def update(self):
        try:
            self.rect.x += round(self.speed_x * self.delta_x / abs(self.delta_x))
            self.rect.y += round(self.speed_y * self.delta_y / abs(self.delta_y))
        except ZeroDivisionError:
            pygame.sprite.Sprite.kill(self)
        if pygame.sprite.spritecollideany(self, main.walls):
            pygame.sprite.Sprite.kill(self)
        elif pygame.sprite.spritecollideany(self, main.enemies):
            for el in pygame.sprite.spritecollide(self, main.enemies, False):
                if isinstance(self.shooter, hero_class.Hero):
                    el.taking_damage(self.bullet_damage)
                    pygame.sprite.Sprite.kill(self)
        elif pygame.sprite.spritecollideany(self, main.hero_group):
            for el in pygame.sprite.spritecollide(self, main.hero_group, False):
                if isinstance(self.shooter, enemies_class.Enemy):
                    el.taking_damage(self.bullet_damage)
                    pygame.sprite.Sprite.kill(self)

