import pygame

FPS = 120
WIDTH = 1920  # Ширина окна
HEIGHT = 1080  # Высота окна
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))  # Экран
G = 30 / FPS  # Ускарение свободного падения
JUMP_HEIGHT = 250  # Высота прыжка
SIDE_SPEED = 450 / FPS  # Скорость передвижения влево и вправо
