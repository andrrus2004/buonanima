import os
import pygame


def load_image(name, colorkey=None):
    fullname = os.path.join('assets/', name)
    if not os.path.isfile(fullname):
        return False
    image = pygame.image.load(fullname)
    return image


class Crosshair(pygame.sprite.Sprite):
    def __init__(self, group):
        super().__init__(group)

        self.add(group)

        pygame.mouse.set_visible(False)

        # Ширина и высота каждого объекта по умолчанию 20px
        self.width = 20
        self.height = 20

        # По умолчанию у объектов нет изображения
        self.image = None
        if self.image is not None:
            self.rect = self.image.get_rect()

    def set_size(self, width, height):
        try:
            self.image = pygame.transform.scale(self.image, (width, height))
            return True
        except Exception:
            return False

    def set_image(self, image_name):
        if type(image_name) == str:
            img = load_image(image_name)
            if type(img) != bool:
                self.image = img
                self.rect = self.image.get_rect()
                return True
        return False

    def update(self, pos):
        self.rect.x, self.rect.y = pos