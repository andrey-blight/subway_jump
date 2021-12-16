import pygame

FPS = 200
WIDTH = 1920  # Ширина окна
HEIGHT = 1080  # Высота окна
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))  # Экран
G = 20 / FPS  # Ускарение свободного падения
JUMP_HEIGHT = 200  # Высота прыжка
