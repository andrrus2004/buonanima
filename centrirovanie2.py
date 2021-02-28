from hero_all.hero_class import *
from field_all.field_class import *
from field_all.crosshair_class import *
import main


def centrirovanye(field, arrow, hero, absolute_centre):
    # perenos_centre = (((arrow.rect.x + hero.rect.x) // 2), (arrow.rect.y + hero.rect.y) // 2)
    perenos_centre = (((arrow.rect.x + 2 * hero.rect.x) // 3), (arrow.rect.y + 2 * hero.rect.y) // 3)
    # print('m', pygame.mouse.get_pos())
    # print('a', absolute_centre)
    # print('p', perenos_centre)
    delta = (int((absolute_centre[0] - perenos_centre[0]) * 0.1), int((absolute_centre[1] - perenos_centre[1]) * 0.1))
    # print('d', delta)
    # print(hero.rect.x + delta[0], hero.rect.y + delta[1])
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


if __name__ == '__main__':

    pygame.init()
    size = width, height = 700, 600
    absolute_centre = (width // 2, height // 2)
    pygame.display.set_caption('Игровое поле')
    screen = pygame.display.set_mode(size)

    game = Field()

    crosshair = pygame.sprite.Group()
    arrow = Crosshair(crosshair)
    print(arrow.set_image('crosshair/crosshair.png'))
    arrow.set_size(20, 20)

    hero_group = pygame.sprite.Group()
    hero = Hero(main.all_sprites, hero_group)
    hero.set_size(30, 45)
    hero.set_place(343, 293)
    MOVING = pygame.USEREVENT + 1
    pygame.time.set_timer(MOVING, 10)
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
                screen.fill(pygame.Color('white'))

            if event.type == pygame.MOUSEBUTTONDOWN:
                hero.fire(event.pos)

            if event.type == pygame.QUIT:
                running = False

            # центровка камеры по середине отрезка между прицелом и игроком(пока не работает корректно)
            '''perenos_centre = (abs((arrow.rect.x - hero.rect.x) // 2), abs((arrow.rect.y - hero.rect.y) // 2))
            new_centre = [abs(absolute_centre[i] - perenos_centre[i]) for i in range(2)]
            hero.set_place(new_centre[0], new_centre[1])'''

            '''perenos_centre = ((arrow.rect.x - hero.rect.x // 2), (arrow.rect.y - hero.rect.y) // 2)
            print('a', absolute_centre)
            print('p', perenos_centre)
            delta = (absolute_centre[0] - perenos_centre[0], absolute_centre[1] - perenos_centre[1])
            print('d', delta)
            print(hero.rect.x + delta[0], hero.rect.y + delta[1])
            hero.change_place(*delta)'''

        game.render()

        main.all_sprites.draw(screen)
        crosshair.draw(screen)

        pygame.display.flip()
    pygame.quit()
