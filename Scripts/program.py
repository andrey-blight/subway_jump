import pygame
from game import Game
from constants import *


class ChristmasJumps:
    """Класс со всей игровой логикой"""

    def __init__(self):
        self.state = "game"  # То что мы будем отображать
        self.game = Game()  # Игра

    def _render(self, events):
        if self.state == "game":  # Если состояние игра то запускаем игру
            self.game.render(events)

    def start_game(self):
        """Главный игровой цикл"""
        pygame.init()
        clock = pygame.time.Clock()
        running = True
        while running:
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    running = False
            self._render(events)
            clock.tick(FPS)
            pygame.display.flip()
        pygame.quit()
