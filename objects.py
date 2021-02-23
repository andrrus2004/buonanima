"""Классы для объектов игрового поля"""

import pygame
import sys
import os


def load_image(name, colorkey=None):
    fullname = os.path.join('assets', name)
    if not os.path.isfile(fullname):
        return False
    image = pygame.image.load(fullname)
    return image


class Object(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__(all_sprites)
        self.width = 20
        self.height = 20
        self.image = None
        self.barrier = False
        if self.image is not None:
            self.rect = self.image.get_rect()
            self.rect.x = 0
            self.rect.y = 0

    def set_group(self, group):
        if type(group) == pygame.sprite.Group:
            self.add(group)
            return True
        return False

    def set_size(self, width, height):
        try:
            if width >= 0 and height >= 0:
                self.width = width
                self.height = height
                return True
            return False
        except Exception:
            return False

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

    def set_barrier(self, barrier_value):
        if type(barrier_value) == bool:
            self.barrier = barrier_value
            return True
        return False


class VWall(Object):
    def __init__(self):
        super().__init__()
        self.set_barrier(True)
        self.set_image('field/vertical_wall.png')
        self.set_group(walls)


class HWall(Object):
    def __init__(self):
        super().__init__()
        self.set_barrier(True)
        self.set_image('field/horizontal_wall.png')
        self.set_group(walls)


class WNWall(Object):
    def __init__(self):
        super().__init__()
        self.set_barrier(True)
        self.set_image('field/wn_wall.png')
        self.set_group(walls)


class NEWall(Object):
    def __init__(self):
        super().__init__()
        self.set_barrier(True)
        self.set_image('field/ne_wall.png')
        self.set_group(walls)


class ESWall(Object):
    def __init__(self):
        super().__init__()
        self.set_barrier(True)
        self.set_image('field/es_wall.png')
        self.set_group(walls)


class SWWall(Object):
    def __init__(self):
        super().__init__()
        self.set_barrier(True)
        self.set_image('field/sw_wall.png')
        self.set_group(walls)


class ESWWall(Object):
    def __init__(self):
        super().__init__()
        self.set_barrier(True)
        self.set_image('field/esw_wall.png')
        self.set_group(walls)


class NESWall(Object):
    def __init__(self):
        super().__init__()
        self.set_barrier(True)
        self.set_image('field/nes_wall.png')
        self.set_group(walls)


class SWNWall(Object):
    def __init__(self):
        super().__init__()
        self.set_barrier(True)
        self.set_image('field/swn_wall.png')
        self.set_group(walls)


class WNEWall(Object):
    def __init__(self):
        super().__init__()
        self.set_barrier(True)
        self.set_image('field/wne_wall.png')
        self.set_group(walls)


class NESWWall(Object):
    def __init__(self):
        super().__init__()
        self.set_barrier(True)
        self.set_image('field/nesw_wall.png')
        self.set_group(walls)


class WoodenRoom(Object):
    def __init__(self):
        super().__init__()
        self.set_size(140, 140)
        self.set_image('field/wooden_room.png')
        self.set_group(rooms)
