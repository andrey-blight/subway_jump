import pygame
from Scripts.game import Game
from menu_and_pause import *


class ChristmasJumps:
    """Класс со всей игровой логикой"""

    def __init__(self):
        self.state = "menu_level"  # То что мы будем отображать
        self.game = Game(self)  # Игра
        self.level_menu = LevelMenu(self)  # Меню выбора уровня
        self.brightness = 0  # Яркость

    def set_state(self, state):
        """Метод который меняет состояние программы"""
        self.state = state
        if state.split("_")[0] == "level":
            # Если мы показываем уровень то составляем уровень
            self.game.set_level(state.split("_")[1])
        self.brightness = 0

    def _render(self, events):
        state = self.state.split("_")
        if state[0] == "level":  # Если состояние игра то запускаем игру
            self.game.render(events)
        elif state[0] == "menu":
            if state[1] == "level":
                self.level_menu.render(events, self.brightness)  # Отрисовка меню с уровнями
        if self.brightness < 255:
            self.brightness += 765 / FPS
            self.brightness = min(255, self.brightness)

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
