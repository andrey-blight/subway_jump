import pygame
from constans import *
from Platforms import StandardPlatform
from main_hero import Hero


class Game:
    def __init__(self):
        self.background = pygame.image.load(r"..\Images\background.jpg")
        # Скорость перемещения мира для того чтобы следовать за играком
        self.world_speed = 0
        self.platforms = pygame.sprite.Group()
        self.main_hero = pygame.sprite.GroupSingle()
        self.set_blocks()

    def set_blocks(self):
        for i in range(0, 1920, 50):
            self.platforms.add(StandardPlatform((i, 800)))
        self.main_hero.add(Hero((100, 0)))

    def render(self):
        SCREEN.fill("black")
        SCREEN.blit(self.background, self.background.get_rect())
        self.platforms.update(self.world_speed)
        self.main_hero.update(self.platforms)
        self.platforms.draw(SCREEN)
        self.main_hero.draw(SCREEN)
