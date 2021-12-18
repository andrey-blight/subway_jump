import pygame
from Scripts.game import Game
from menu_and_pause import *


class ChristmasJumps:
    """Класс со всей игровой логикой"""

    def __init__(self):
        self.state = "level"  # То что мы будем отображать
        self.game = Game()  # Игра
        self.level_menu = LevelMenu(self)

    def set_state(self, state):
        self.state = state

    def _render(self, events):
        state = self.state.split("_")
        if state[0] == "level":  # Если состояние игра то запускаем игру
            # TODO добавить отрисовку уровня
            self.game.render(events)
        elif state[0] == "menu":
            if state[1] == "level":
                self.level_menu.render(events)  # Отрисовка меню с уровнями

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
