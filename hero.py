# -------------КЛАСС ДЛЯ ГЛАВНОГО ГЕРОЯ---------------
"""Может быть протестирую чуть чуть, но врятли, пока просто набросаю"""


import pygame
import os
import sys
from useful_functions import load_image


class Hero(pygame.sprite.Sprite):

    image_standart = load_image("hero/car2.png")

    def __init__(self, *group):
        super().__init__(*group)
        self.image = Hero.image_standart
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0

        self.health_max = 100   # максимальное здоровье в уе
        self.health_proc = 1     # здоровье в частях от целого(роцентах) от 0 до 1
        self.health_current = self.health_max * self.health_proc   # здоровье в настоящем времени

        self.hands = None   # предмет в руках


    # -------МЕТОДЫ НАСТРОЙКИ ГЕРОЯ ПРИ ГЕНЕРАЦИИ---------

    # метод смены координат(можно использовать для генерации на карте)
    def set_place(self, x, y):
        self.rect.x = x
        self.rect.y = y

    # метод для изменения информации о здоровье ГГ
    def set_health(self, health, procents=1):
        self.health = health
        self.health_proc = procents
        self.health_current = self.health_max * self.health_proc

    # помещает предмет в руки ГГ и заменяет спрайт
    def set_hands(self, item, sprite_path):
        self.hands = item
        self.image = load_image(sprite_path)
    # -----------------------------------------------------------


    # метод для создания объекта пули| args: позиция мыши в момент стрельбы
    def fire(self, mouse_xy):
        # создаем объект класса Bullet
        '''его пока не существует)'''
        pass


if __name__ == "__main__":
    pygame.init()
    pygame.display.set_caption('ТЕСТ')
    size = width, height = 400, 400
    screen = pygame.display.set_mode(size)
    screen.fill((255, 255, 255))

    hero_group = pygame.sprite.Group()
    hero = Hero(hero_group)
    hero.set_place(50, 50)

    clock = pygame.time.Clock()

    running = True
    while running:
        pygame.time.delay(100)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.fill((255, 255, 255))
        hero_group.draw(screen)
        pygame.display.flip()
        clock.tick(10)
pygame.quit()
