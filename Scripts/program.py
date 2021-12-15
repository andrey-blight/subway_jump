import pygame
from game import Game
from constans import *


class ChristmasJumps:
    """Класс со всей игровой логикой"""

    def __init__(self):
        self.state = "game"  # То что мы будем отображать
        self.game = Game()  # Игра

    def _render(self):
        if self.state == "game":  # Если состояние игра то запускаем игру
            self.game.render()

    def start_game(self):
        clock = pygame.time.Clock()
        pygame.init()
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            self._render()
            pygame.display.flip()
            clock.tick(FPS)
        pygame.quit()
