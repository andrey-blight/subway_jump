import pygame

FPS = 120
WIDTH = 1920  # Ширина окна
HEIGHT = 1080  # Высота окна
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))  # Экран
G = 20 / FPS  # Ускарение свободного падения
JUMP_HEIGHT = 350  # Высота прыжка
