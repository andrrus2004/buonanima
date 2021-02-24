import pygame
import sys
import os
from hero_class import *
from field_class import *
from bullet_class import *


all_sprites = pygame.sprite.Group()
hero_group = pygame.sprite.Group()
barriers = pygame.sprite.Group()
walls = pygame.sprite.Group()
rooms = pygame.sprite.Group()
floor = pygame.sprite.Group()
furniture = pygame.sprite.Group()
bullets = pygame.sprite.Group()

pygame.init()
size = width, height = 700, 600
pygame.display.set_caption('Игровое поле')
screen = pygame.display.set_mode(size)

if __name__ == '__main__':

    game = Field()

    hero_group = pygame.sprite.Group()
    hero = Hero(main.all_sprites, hero_group)
    hero.set_place(343, 293)
    MOVING = pygame.USEREVENT + 1
    pygame.time.set_timer(MOVING, 1)
    screen.fill(pygame.Color('white'))

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == MOVING:
                game.move(hero, 1)
                main.bullets.update()
                screen.fill(pygame.Color('white'))

            if event.type == pygame.MOUSEBUTTONDOWN:
                hero.fire(event.pos)

            if event.type == pygame.QUIT:
                running = False

        game.render()

        main.all_sprites.draw(screen)

        pygame.display.flip()
    pygame.quit()
