# -------------КЛАСС ДЛЯ ГЛАВНОГО ГЕРОЯ---------------
"""Может быть протестирую чуть чуть, но врятли, пока просто набросаю"""
from field_all.field_class import *
from bullet_all.bullet_class import *


class Hero(pygame.sprite.Sprite):

    def __init__(self, *group):
        super().__init__(*group)
        self.image = load_image("hero/test_img.png")
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

        self.step = 1   # один шаг

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

    # метод смены местоположения(используется для центрирования)
    def change_place(self, dx, dy):
        self.rect.x += dx
        self.rect.y += dy

    # метод для создания объекта пули| args: позиция мыши в момент стрельбы
    def fire(self, mouse_xy):
        bullet = Bullet((self.rect.x, self.rect.y), mouse_xy)
        bullet.set_group(main.bullets)

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

    game = Field()

    pygame.init()
    size = width, height = 700, 600
    pygame.display.set_caption('Игровое поле')
    screen = pygame.display.set_mode(size)
    screen.fill((255, 255, 255))

    hero_group = pygame.sprite.Group()
    hero = Hero(main.all_sprites, hero_group)
    hero.set_place(343, 293)
    MOVING = pygame.USEREVENT + 1
    pygame.time.set_timer(MOVING, 10)
    screen.fill(pygame.Color('white'))

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == MOVING:
                hero.move()
                main.bullets.update()
                screen.fill(pygame.Color('white'))

            if event.type == pygame.MOUSEBUTTONDOWN:
                hero.fire(event.pos)

            if event.type == pygame.QUIT:
                running = False

        main.all_sprites.draw(screen)
        game.render()


        pygame.display.flip()
    pygame.quit()
