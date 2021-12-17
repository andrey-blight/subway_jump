import pygame
from constants import *


class Hero(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.image = pygame.Surface((25, 50))
        self.image.fill('red')
        self.rect = self.image.get_rect(topleft=pos)
        #               ФИЗИКА
        self.speed_x = 0  # Скорость по горизонтали
        self.speed_y = 0  # Скорость по вертикали
        self.gravity = "down"  # Направление гравитации

    def update(self, platforms):
        self.rect = self.rect.move(self.speed_x, self.speed_y)  # Перемещение по с заданными скоростями
        if self.gravity == "down":
            borders = pygame.sprite.Group()
            for border in platforms.sprites():
                borders.add(border.get_top_border().sprite)
            if pygame.sprite.spritecollideany(self, borders):
                self.speed_y = -(2 * G * JUMP_HEIGHT) ** 0.5
            else:
                # Добавляем ускорение свободного падения если нет опоры
                self.speed_y += G
