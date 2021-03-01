from hero_class import *
from field_class import *
from crosshair_class import *
import main


def centrirovanye(field, arrow, hero, absolute_centre):
    perenos_centre = (((arrow.rect.x + 2 * hero.rect.x) // 3), (arrow.rect.y + 2 * hero.rect.y) // 3)
    delta = (int((absolute_centre[0] - perenos_centre[0]) * 0.1), int((absolute_centre[1] - perenos_centre[1]) * 0.1))
    hero.change_place(*delta)
    for el in main.all_not_hero:
        el.rect.x += delta[0]
        el.rect.y += delta[1]
    field.startx += delta[0]
    field.starty += delta[1]


all_sprites = pygame.sprite.Group()
hero_group = pygame.sprite.Group()
barriers = pygame.sprite.Group()
walls = pygame.sprite.Group()
rooms = pygame.sprite.Group()
floor = pygame.sprite.Group()
furniture = pygame.sprite.Group()
bullets = pygame.sprite.Group()
