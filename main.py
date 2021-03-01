from hero_class import *
from field_class import *
from enemies_class import *
from interface_class import *
from centrirovanie import *
from useful_functions import *


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


all_sprites = pygame.sprite.Group()
menu_sprites = pygame.sprite.Group()
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
size = width, height = 800, 550
absolute_centre = (width // 2, height // 2)
pygame.display.set_caption('Buonanima')
screen = pygame.display.set_mode(size)

if __name__ == '__main__':
    menu = Menu()
    is_menu = True
    is_end = False

    screen.fill(pygame.Color('white'))
    running = True
    while running:
        for event in pygame.event.get():
            if not is_menu and not is_end:
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

                if event.type == ATTACK:
                    for el in main.enemies:
                        if el.attack_check(hero):
                            el.rotate(hero.get_pose())
                            el.fire(hero.rect.center)

                if event.type == pygame.MOUSEBUTTONDOWN and hero.ammo > 0:
                    hero.fire(pygame.mouse.get_pos())
                    if hero.ammo == 0:
                        pygame.event.set_allowed(RELOAD)
                        pygame.time.set_timer(RELOAD, 3000)

            if is_menu and event.type == pygame.MOUSEBUTTONDOWN:
                pos = event.pos
                if menu.start_button.click(pos):
                    is_menu = False
                    new_game()
                elif menu.exit_button.click(pos):
                    exit()

            if event.type == pygame.QUIT:
                running = False
        if not is_menu:
            if hero.health <= 0:
                is_end = True
                res = end_game()
                main.all_sprites.draw(screen)
                screen.blit(shade, (0, 0), special_flags=pygame.BLEND_RGB_MULT)
                screen.blit(*res)
            else:
                inter.update()
                hero.rotate()
                game.render()
                main.all_sprites.draw(screen)
                crosshair.draw(screen)
        else:
            main.menu_sprites.draw(screen)
            screen.blit(menu.start_button.text, (menu.start_button.text_x, menu.start_button.text_y))
            screen.blit(menu.exit_button.text, (menu.exit_button.text_x, menu.exit_button.text_y))

        pygame.display.flip()
    pygame.quit()
