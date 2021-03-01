import pygame
import os
import sys


def load_image(name, colorkey=None):
    fullname = os.path.join('assets', name)
    if not os.path.isfile(fullname):
        return False
    image = pygame.image.load(fullname)
    return image


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


def end_game():
    global shade
    shade = pygame.Surface((800, 550))
    shade.fill(pygame.Color(50, 50, 50))
    shade.set_alpha(100)
    inter.update()
    color = pygame.Color('white')
    font = pygame.font.Font(None, 100)
    text = font.render('Конец игры', True, color)
    text_x = width // 2 - text.get_width() // 2
    text_y = height // 2 - text.get_height() // 2
    return text, (text_x, text_y)
