from hero_all.hero_class import *
from field_all.field_class import *
from field_all.field_map import *
from centrirovanie2 import *
from enemies_class import Enemy
from interface_class import *


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    if colorkey is not None:
        image = image.convert()
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    else:
        image = image.convert_alpha()
    return image


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
size = width, height = 700, 600
absolute_centre = (width // 2, height // 2)
pygame.display.set_caption('Игровое поле')
screen = pygame.display.set_mode(size)

if __name__ == '__main__':

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
    enemies_pos = [(317, 3), (391, 4)]
    #for el in enemies_pos:
        #enemy = Enemy(main.all_sprites, main.enemies, main.all_not_hero)
        #enemy.set_place(el[0], el[1])

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

            if event.type == pygame.QUIT:
                running = False

        inter.update(hero)

        hero.rotate()

        game.render()

        main.all_sprites.draw(screen)

        crosshair.draw(screen)

        pygame.display.flip()
    pygame.quit()
