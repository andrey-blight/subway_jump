import pygame

FPS = 200
WIDTH = 1920  # Ширина окна
HEIGHT = 1080  # Высота окна
BLOCK_SIZE = 50  # Размер одного блока
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))  # Экран
G = 9.8 / FPS  # Ускарение свободного падения
JUMP_HEIGHT = 150  # Высота прыжка
