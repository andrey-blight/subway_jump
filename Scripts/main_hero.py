import pygame
from constans import *


class Hero(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.image = pygame.Surface((25, 50))
        self.image.fill('red')
        self.rect = self.image.get_rect(topleft=pos)
        #               ФИЗИКА
        self.speed_x = 0  # Скорость по горизонтали
        self.speed_y = 0  # Скорость по вертикали

    def update(self, platforms):
        self.rect = self.rect.move(self.speed_x, self.speed_y)  # Перемещение по с заданными скоростями
        if pygame.sprite.spritecollideany(self, platforms):
            # Если мы столкнулись с землей, то рассчитываем скорость и отталкиваемся
            self.speed_y = -(2 * G * JUMP_HEIGHT) ** 0.5
        else:
            # Добавляем ускорение свободного падения если нет опоры
            self.speed_y += G
