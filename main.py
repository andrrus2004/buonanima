import pygame
from useful_functions import load_image
from field_moving import Field, Hero

all_sprites = pygame.sprite.Group()
barriers = pygame.sprite.Group()
walls = pygame.sprite.Group()
rooms = pygame.sprite.Group()
floor = pygame.sprite.Group()
furniture = pygame.sprite.Group()
if __name__ == '__main__':
    # Создание окна
    pygame.init()
    size = width, height = 700, 600
    pygame.display.set_caption('Игровое поле')
    screen = pygame.display.set_mode(size)

    # Группы со спрайтами
    # К группе barriers относится всё, через что нельзя проходить


    # Создание игрового поля
    game = Field()

    # Создание главного героя в центре экрана
    hero_group = pygame.sprite.Group()
    hero = Hero(all_sprites, hero_group)
    hero.set_place(343, 293)

    # Создание события, которое срабатывает 1 раз в милисекунду
    MOVING = pygame.USEREVENT + 1
    pygame.time.set_timer(MOVING, 1)
    screen.fill(pygame.Color('white'))

    running = True
    while running:
        for event in pygame.event.get():
            # Условие, если прошлё время и вызвалось событие
            if event.type == MOVING:
                # Перемещение карты на 1 пиксель
                game.move(1)
                screen.fill(pygame.Color('white'))

            if event.type == pygame.QUIT:
                running = False

        # Расположение объектов карты
        game.render(screen)

        # Отрисовка объектов карты
        all_sprites.draw(screen)

        pygame.display.flip()
    pygame.quit()