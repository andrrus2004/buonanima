# --------------------КЛАСС С ИГРОВЫМ ПОЛЕМ--------------------

"""Класс Field это класс игрового поля, а класс Object это объекты на этом игровом поле.
На то, что тут куча отдельных классов для каждого объекта можете не обращать внимание,
у меня есть идея как это всё в конце убрать и оставить только класс Object"""


import pygame
import sys
import os


def load_image(name, colorkey=None):
    fullname = os.path.join('assets', name)
    if not os.path.isfile(fullname):
        return False
    image = pygame.image.load(fullname)
    return image


class Hero(pygame.sprite.Sprite):

    image_standart = load_image("hero/test_img.png")

    def __init__(self, *group):
        super().__init__(*group)
        self.image = Hero.image_standart
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
        # создаем объект класса Bullet
        '''его пока не существует)'''
        pass

    def move(self):
        if pygame.key.get_pressed()[pygame.K_UP] and self.move_up:
            self.rect.y -= self.step
        if pygame.key.get_pressed()[pygame.K_DOWN] and self.move_down:
            self.rect.y += self.step
        if pygame.key.get_pressed()[pygame.K_RIGHT] and self.move_right:
            self.rect.x += self.step
        if pygame.key.get_pressed()[pygame.K_LEFT] and self.move_left:
            self.rect.x -= self.step


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
                return True
        return False


""" Далее идут отдельные классы для каждого определённого объекта,
где каждый наследуется от класса Object и задаёт параметры под себя"""

# Классы для стен
class VWall(Object):
    def __init__(self):
        super().__init__()
        self.set_group(barriers)
        self.set_image('field/vertical_wall.png')
        self.set_group(walls)


class HWall(Object):
    def __init__(self):
        super().__init__()
        self.set_group(barriers)
        self.set_image('field/horizontal_wall.png')
        self.set_group(walls)


class WNWall(Object):
    def __init__(self):
        super().__init__()
        self.set_group(barriers)
        self.set_image('field/wn_wall.png')
        self.set_group(walls)


class NEWall(Object):
    def __init__(self):
        super().__init__()
        self.set_group(barriers)
        self.set_image('field/ne_wall.png')
        self.set_group(walls)


class ESWall(Object):
    def __init__(self):
        super().__init__()
        self.set_group(barriers)
        self.set_image('field/es_wall.png')
        self.set_group(walls)


class SWWall(Object):
    def __init__(self):
        super().__init__()
        self.set_group(barriers)
        self.set_image('field/sw_wall.png')
        self.set_group(walls)


class ESWWall(Object):
    def __init__(self):
        super().__init__()
        self.set_group(barriers)
        self.set_image('field/esw_wall.png')
        self.set_group(walls)


class NESWall(Object):
    def __init__(self):
        super().__init__()
        self.set_group(barriers)
        self.set_image('field/nes_wall.png')
        self.set_group(walls)


class SWNWall(Object):
    def __init__(self):
        super().__init__()
        self.set_group(barriers)
        self.set_image('field/swn_wall.png')
        self.set_group(walls)


class WNEWall(Object):
    def __init__(self):
        super().__init__()
        self.set_group(barriers)
        self.set_image('field/wne_wall.png')
        self.set_group(walls)


class NESWWall(Object):
    def __init__(self):
        super().__init__()
        self.set_group(barriers)
        self.set_image('field/nesw_wall.png')
        self.set_group(walls)


class BPanel(Object):
    def __init__(self):
        super().__init__()
        self.set_image('field/black_panel.png')
        self.set_group(floor)


# Классы для комнат
class WoodenRoom(Object):
    def __init__(self):
        super().__init__()
        self.set_size(140, 140)
        self.set_image('field/wooden_room.png')
        self.set_group(rooms)


class StoneRoom(Object):
    def __init__(self):
        super().__init__()
        self.set_size(180, 80)
        self.set_image('field/stone_room.png')
        self.set_group(rooms)


class ParquetRoom(Object):
    def __init__(self):
        super().__init__()
        self.set_size(240, 340)
        self.set_image('field/parquet_room.png')
        self.set_group(rooms)


# Классы для мебели
class Billiard(Object):
    def __init__(self):
        super().__init__()
        self.set_group(barriers)
        self.set_size(100, 61)
        self.set_image('field/billiard.png')
        self.set_group(furniture)


class Poker(Object):
    def __init__(self):
        super().__init__()
        self.set_group(barriers)
        self.set_size(152, 146)
        self.set_image('field/poker_table.png')
        self.set_group(furniture)


# Класс игрового поля
class Field:
    def __init__(self, file=None):
        # По умолчанию размер одной клетки 20px
        self.cell_size = 20

        # Значиния, которые показывают от какого x и y начть отрисовку карты
        # Далее эти значения могут использоваться для движения всей карты
        self.startx, self.starty = 50, 50

        # Матрица с объектами карты задаётся пока в ручную, в будущем сделаю загрузку из файла
        # и заменю каждый отдельный класс с объектом на словать с параметрами.
        if file is None:
            self.board = [[WNWall(), HWall(),      HWall(),    HWall(), HWall(),  HWall(), HWall(), HWall(), NEWall(),  None,    WNWall(),  HWall(),       HWall(), HWall(), HWall(), HWall(), HWall(), HWall(), HWall(), HWall(), HWall(), HWall(), HWall(), NEWall()],
                          [VWall(),  WoodenRoom(), None,       None,    None,     None,    None,    None,    VWall(),   None,    VWall(),   ParquetRoom(), None,    None,    None,    None,    None,    None,    None,    None,    None,    None,    None,    VWall()],
                          [VWall(),  None,         None,       None,    None,     None,    None,    None,    VWall(),   None,    VWall(),   None,          None,    None,    None,    None,    None,    None,    None,    None,    None,    None,    None,    VWall()],
                          [VWall(),  None,         Billiard(), None,    None,     None,    None,    None,    VWall(),   None,    VWall(),   None,          None,    None,    None,    None,    None,    None,    None,    None,    None,    None,    None,    VWall()],
                          [VWall(),  None,         None,       None,    None,     None,    None,    None,    VWall(),   None,    VWall(),   None,          None,    None,    Poker(), None,    None,    None,    None,    None,    None,    None,    None,    VWall()],
                          [VWall(),  None,         None,       None,    None,     None,    None,    None,    VWall(),   None,    VWall(),   None,          None,    None,    None,    None,    None,    None,    None,    None,    None,    None,    None,    VWall()],
                          [VWall(),  None,         None,       None,    None,     None,    None,    None,    VWall(),   None,    VWall(),   None,          None,    None,    None,    None,    None,    None,    None,    None,    None,    None,    None,    VWall()],
                          [VWall(),  None,         None,       None,    None,     None,    None,    None,    VWall(),   None,    VWall(),   None,          None,    None,    None,    None,    None,    None,    None,    None,    None,    None,    None,    VWall()],
                          [NESWall(), HWall(),     HWall(),    HWall(), BPanel(), HWall(), HWall(), HWall(), WNEWall(), HWall(), SWNWall(), None,          None,    None,    None,    None,    None,    None,    None,    None,    None,    None,    None,    VWall()],
                          [VWall(),  StoneRoom(),  None,       None,    None,     None,    None,    None,    None,      None,    VWall(),   None,          None,    None,    None,    None,    None,    None,    None,    None,    None,    None,    None,    VWall()],
                          [VWall(),  None,         None,       None,    None,     None,    None,    None,    None,      None,    BPanel(),  None,          None,    None,    None,    None,    None,    None,    None,    None,    None,    None,    None,    VWall()],
                          [VWall(),  None,         None,       None,    None,     None,    None,    None,    None,      None,    BPanel(),  None,          None,    None,    None,    None,    None,    None,    None,    None,    None,    None,    None,    VWall()],
                          [VWall(),  None,         None,       None,    None,     None,    None,    None,    None,      None,    VWall(),   None,          None,    None,    None,    None,    None,    None,    None,    None,    None,    None,    None,    VWall()],
                          [SWWall(), HWall(),      HWall(),    HWall(), HWall(),  HWall(), HWall(), HWall(), HWall(),   HWall(), SWNWall(), None,          None,    None,    None,    None,    None,    None,    None,    None,    None,    None,    None,    VWall()],
                          [None,     None,         None,       None,    None,     None,    None,    None,    None,      None,    VWall(),   None,          None,    None,    None,    None,    None,    None,    None,    None,    None,    None,    None,    VWall()],
                          [None,     None,         None,       None,    None,     None,    None,    None,    None,      None,    VWall(),   None,          None,    None,    None,    None,    None,    None,    None,    None,    None,    None,    None,    VWall()],
                          [None,     None,         None,       None,    None,     None,    None,    None,    None,      None,    VWall(),   None,          None,    None,    None,    None,    None,    None,    None,    None,    None,    None,    None,    VWall()],
                          [None,     None,         None,       None,    None,     None,    None,    None,    None,      None,    VWall(),   None,          None,    None,    None,    None,    None,    None,    None,    None,    None,    None,    None,    VWall()],
                          [None,     None,         None,       None,    None,     None,    None,    None,    None,      None,    SWWall(),  HWall(),       HWall(), HWall(), HWall(), HWall(), HWall(), HWall(), HWall(), HWall(), HWall(), HWall(), HWall(), ESWall()]]
        else:
            pass

        # Ширина и высота карты в количестве клеток
        self.width = len(self.board[0])
        self.height = len(self.board)

    # Функция для получения клетки по её координатам
    def get_cell(self, cell_x, cell_y):
        try:
            x = (cell_x - self.startx) // self.cell_size
            y = (cell_y - self.starty) // self.cell_size
            cell = self.board[y][x]
            return cell
        except Exception:
            return False

    # Функция для расположения всех объектов карты в нужном порядке.
    # Она используется в главном игровом цикле, но после неё
    # всё равно нужно использвать all_sprites.draw(screen)
    def render(self, screen):
        pixel_w = self.width * self.cell_size + self.startx
        pixel_h = self.height * self.cell_size + self.starty
        for y in range(self.starty, pixel_h, self.cell_size):
            for x in range(self.startx, pixel_w, self.cell_size):
                cell = self.get_cell(x, y)
                if type(cell) == bool and cell is False:
                    return False
                if cell is not None:
                    cell.rect.x = x
                    cell.rect.y = y

    def move_up(self, value_px):
        self.starty -= value_px

    def move_down(self, value_px):
        self.starty += value_px

    def move_right(self, value_px):
        self.startx += value_px

    def move_left(self, value_px):
        self.startx -= value_px


if __name__ == '__main__':
    # Создание окна
    pygame.init()
    size = width, height = 700, 600
    pygame.display.set_caption('Игровое поле')
    screen = pygame.display.set_mode(size)

    # Группы со спрайтами
    # К группе barriers относится всё, через что нельзя проходить
    all_sprites = pygame.sprite.Group()
    barriers = pygame.sprite.Group()
    walls = pygame.sprite.Group()
    rooms = pygame.sprite.Group()
    floor = pygame.sprite.Group()
    furniture = pygame.sprite.Group()

    # Создание игрового поля
    game = Field()

    hero_group = pygame.sprite.Group()
    hero = Hero(hero_group)
    hero.set_place(300, 300)

    TIMER = pygame.USEREVENT + 1
    pygame.time.set_timer(TIMER, 1)
    x, y = 0, 0
    right, left, up, down = False, False, False, False
    screen.fill(pygame.Color('white'))

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == 273:
                    down = True
                elif event.key == 274:
                    up = True
                elif event.key == 275:
                    right = True
                elif event.key == 276:
                    left = True

            if event.type == pygame.KEYUP:
                if event.key == 273:
                    down = False
                elif event.key == 274:
                    up = False
                elif event.key == 275:
                    right = False
                elif event.key == 276:
                    left = False

            if event.type == TIMER:
                if right:
                    game.move_left(1)
                if left:
                    game.move_right(1)
                if up:
                    game.move_up(1)
                if down:
                    game.move_down(1)
                screen.fill(pygame.Color('white'))

            if event.type == pygame.QUIT:
                running = False

        # Расположение объектов карты
        game.render(screen)

        # Отрисовка объектов карты
        all_sprites.draw(screen)
        hero_group.draw(screen)

        pygame.display.flip()
    pygame.quit()
