import pygame
from platforms import StandardBlock


class Money(StandardBlock):
    IMAGE = pygame.image.load(r"..\Images\money.png").convert_alpha()

    def __init__(self, pos):
        self.BLOCK_SIZE = 31
        super(Money, self).__init__(pos)
        self.image = self.IMAGE
