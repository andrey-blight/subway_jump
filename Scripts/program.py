import pygame
from Scripts.game import Game
from menu_and_pause import *

pygame.init()  # Инициализируем pygame в начале чтобы работали шрифты во время инициализации классов меню


class ChristmasJumps:
    """Класс со всей игровой логикой"""

    def __init__(self):
        self.state = "menu_main"  # То что мы будем отображать
        self.game = Game(self)  # Игра
        self.level_menu = LevelMenu(self)  # Меню выбора уровня
        self.main_menu = MainMenu(self)
        self.brightness = 0  # Яркость
        self.running = True

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
            elif state[1] == "main":
                self.main_menu.render(events, self.brightness)  # Отрисовка главного меню
        elif state[0] == "quite":
            self.running = False
        if self.brightness < 255:
            self.brightness += 1500 / FPS
            self.brightness = min(255, self.brightness)

    def start_game(self):
        """Главный игровой цикл"""
        clock = pygame.time.Clock()
        while self.running:
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    self.running = False
            self._render(events)
            clock.tick(FPS)
            print(clock.get_fps())
            pygame.display.flip()
        pygame.quit()
