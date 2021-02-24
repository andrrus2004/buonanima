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

        self.move_up = True    # можно ли пойти вверх
        self.move_down = True    # можно ли пойти вниз
        self.move_right = True    # можно ли пойти вправо
        self.move_left = True    # можно ли пойти влево

        self.step = 10    # один шаг

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

    # зменение размера спрайта
    def set_size(self, wide, high):
        self.image = pygame.transform.scale(self.image, (wide, high))

    # -----------------------------------------------------------

    # метод для создания объекта пули| args: позиция мыши в момент стрельбы
    def fire(self, mouse_xy):
        # создаем объект класса Bullet
        '''его пока не существует)'''
        pass

    def move(self):
        if pygame.key.get_pressed()[pygame.K_UP] and self.move_up:
            self.rect.y -= self.step
        if pygame.key.get_pressed()[pygame.K_DOWN] and self.move_down:
            self.rect.y += self.step
        if pygame.key.get_pressed()[pygame.K_RIGHT] and self.move_right:
            self.rect.x += self.step
        if pygame.key.get_pressed()[pygame.K_LEFT] and self.move_left:
            self.rect.x -= self.step


if __name__ == "__main__":
    pygame.init()
    pygame.display.set_caption('ТЕСТ')
    size = width, height = 400, 400
    screen = pygame.display.set_mode(size)
    screen.fill((255, 255, 255))

    hero_group = pygame.sprite.Group()
    hero = Hero(hero_group)
    hero.set_place(50, 50)
    hero.set_size(200, 300)

    clock = pygame.time.Clock()

    running = True
    while running:
        pygame.time.delay(100)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.fill((255, 255, 255))
        hero.move()
        hero_group.draw(screen)
        pygame.display.flip()
        clock.tick(10)
pygame.quit()
