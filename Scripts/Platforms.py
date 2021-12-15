import pygame
from constans import *


class PlatformBorder(pygame.sprite.Sprite):
    pass


class StandardPlatform(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.image = pygame.Surface((BLOCK_SIZE, BLOCK_SIZE))
        self.image.fill('grey')
        self.rect = self.image.get_rect(topleft=pos)

    def update(self, x_shift):
        self.rect.x -= x_shift
