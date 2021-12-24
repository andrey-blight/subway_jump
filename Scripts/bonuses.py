import pygame
from platforms import StandardBlock


class Money(StandardBlock):
    IMAGE = pygame.image.load(r"..\Images\money.png").convert_alpha()

    def __init__(self, pos):
        self.BLOCK_SIZE = 31
        super(Money, self).__init__(pos)
        self.image = self.IMAGE


class GravityUp(StandardBlock):
    IMAGE = pygame.image.load(r"..\Images\gravity_up.png").convert_alpha()

    def __init__(self, pos):
        self.BLOCK_SIZE = 31
        super(GravityUp, self).__init__(pos)
        self.image = self.IMAGE


class GravityDown(StandardBlock):
    IMAGE = pygame.image.load(r"..\Images\gravity_down.png").convert_alpha()

    def __init__(self, pos):
        self.BLOCK_SIZE = 31
        super(GravityDown, self).__init__(pos)
        self.image = self.IMAGE
