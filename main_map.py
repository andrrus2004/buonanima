from hero_all.hero_class import *
from field_all.field_class import *
from centrirovanie2 import *
from enemies_class import *

all_sprites = pygame.sprite.Group()
hero_group = pygame.sprite.Group()
barriers = pygame.sprite.Group()
walls = pygame.sprite.Group()
rooms = pygame.sprite.Group()
floor = pygame.sprite.Group()
furniture = pygame.sprite.Group()
bullets = pygame.sprite.Group()
enemies = pygame.sprite.Group()
all_not_hero = pygame.sprite.Group()

pygame.init()
# size = width, height = 700, 600
size = width, height = 2000, 1000
absolute_centre = (width // 2, height // 2)
pygame.display.set_caption('Игровое поле')
screen = pygame.display.set_mode(size)

if __name__ == '__main__':

    game = Field()

    hero_group = pygame.sprite.Group()
    hero = Hero(main.all_sprites, hero_group)
    hero.set_place(343, 293)
    fire = False

    # enemy = Enemy(main.all_sprites, main.enemies, main.all_not_hero)
    # enemy.set_place(310, 200)

    MOVING = pygame.USEREVENT + 1
    pygame.time.set_timer(MOVING, 10)

    RELOAD = pygame.USEREVENT + 2
    pygame.time.set_timer(RELOAD, 3000)
    pygame.event.set_blocked(RELOAD)

    crosshair = pygame.sprite.Group()
    arrow = Crosshair(crosshair)
    arrow.set_image('crosshair/crosshair.png')
    arrow.set_size(20, 20)

    screen.fill(pygame.Color('white'))
    running = True
    while running:
        for event in pygame.event.get():

            if pygame.mouse.get_focused():
                arrow.update(pygame.mouse.get_pos())
                centrirovanye(game, arrow, hero, absolute_centre)

            if event.type == MOVING:
                game.move(hero, 1)
                main.bullets.update()
                main.enemies.update()
                screen.fill(pygame.Color('white'))

            if event.type == RELOAD:
                hero.ammo = 6
                pygame.event.set_blocked(RELOAD)

            if event.type == pygame.MOUSEBUTTONDOWN and hero.ammo > 0:
                hero.fire(pygame.mouse.get_pos())
                if hero.ammo == 0:
                    pygame.event.set_allowed(RELOAD)
                    pygame.time.set_timer(RELOAD, 3000)

            if event.type == pygame.QUIT:
                running = False

        game.render()

        main.all_sprites.draw(screen)

        crosshair.draw(screen)

        pygame.display.flip()
    pygame.quit()
