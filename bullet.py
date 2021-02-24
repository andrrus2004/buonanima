import pygame
import sys
import os


def load_image(name, colorkey=None):
    fullname = os.path.join('assets', name)
    if not os.path.isfile(fullname):
        return False
    image = pygame.image.load(fullname)
    return image


# Класс главного героя
class Hero(pygame.sprite.Sprite):

    image_standart = load_image("hero/test_img.png")

    def __init__(self, *group):
        super().__init__(*group)
        self.image = Hero.image_standart
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0
        # self.mask = pygame.mask.from_surface(self.image)

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
    # -----------------------------------------------------------

    # метод для создания объекта пули| args: позиция мыши в момент стрельбы
    def fire(self, mouse_xy):
        bullet = Bullet((self.rect.x, self.rect.y), mouse_xy)
        bullet.set_group(bullets)


# Класс объекта на игровом поле
class Object(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__(all_sprites)

        # Ширина и высота каждого объекта по умолчанию 20px
        self.width = 20
        self.height = 20

        # По умолчанию у объектов нет изображения
        self.image = None
        if self.image is not None:
            self.rect = self.image.get_rect()
            self.rect.x = 0
            self.rect.y = 0

    # Функция для добавления объекта в группу спрайтов
    def set_group(self, group):
        if type(group) == pygame.sprite.Group:
            self.add(group)
            return True
        return False

    # Функция для изменения ширины и высоты объекта
    def set_size(self, width, height):
        try:
            if width >= 0 and height >= 0:
                self.width = width
                self.height = height
                return True
            return False
        except Exception:
            return False

    # Функция установки изображения объекту
    def set_image(self, image_name):
        if type(image_name) == str:
            img = load_image(image_name)
            if type(img) != bool:
                self.image = img
                self.rect = self.image.get_rect()
                self.rect.x = 0
                self.rect.y = 0
                # self.mask = pygame.mask.from_surface(self.image)
                return True
        return False


class Bullet(Object):
    def __init__(self, creator_pos, mouse_pos):
        super().__init__()
        self.image = load_image("hero/test_img.png")
        self.rect = self.image.get_rect()
        self.rect.x = creator_pos[0]
        self.rect.y = creator_pos[1]

        # расстояние между позицией героя и нажатием мыши
        self.delta_x = mouse_pos[0] - self.rect.x
        self.delta_y = mouse_pos[1] - self.rect.y

        self.speed = 10   # корость пули
        # синусы углов, лежащих напротив проекций скорости
        self.sin_x = abs(self.delta_x) / (self.delta_x ** 2 + self.delta_y ** 2) ** 0.5
        self.sin_y = abs(self.delta_y) / (self.delta_x ** 2 + self.delta_y ** 2) ** 0.5

        self.speed_x = int(self.speed * self.sin_x)   # скорость пули по x
        self.speed_y = int(self.speed * self.sin_y)   # скорость пули по y

        self.exist = True   # переменная существование пули

    # обновляет местоположение пули
    def update(self):
        if self.exist:
            try:
                self.rect.x += self.speed_x * self.delta_x / abs(self.delta_x)
                self.rect.y += self.speed_y * self.delta_y / abs(self.delta_y)
            except ZeroDivisionError:
                pass


if __name__ == '__main__':
    # Создание окна
    pygame.init()
    size = width, height = 700, 600
    pygame.display.set_caption('Игровое поле')
    screen = pygame.display.set_mode(size)
    clock = pygame.time.Clock()

    # Группы со спрайтами
    all_sprites = pygame.sprite.Group()
    bullets = pygame.sprite.Group()


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
                screen.fill(pygame.Color('white'))

            if event.type == pygame.QUIT:
                running = False
            # условие нажатия на кнопку мыши
            if event.type == pygame.MOUSEBUTTONDOWN:
                # создание пули
                hero.fire(event.pos)

        all_sprites.draw(screen)
        bullets.update()   # обновление координат всех пуль на карте
        pygame.display.flip()
        clock.tick(10)
    pygame.quit()