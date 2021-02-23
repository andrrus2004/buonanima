import pygame
import os
import sys


def load_image(name, colorkey=None):
    fullname = os.path.join('assets', name)
    if not os.path.isfile(fullname):
        return False
    image = pygame.image.load(fullname)
    return image