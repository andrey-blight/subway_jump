import pygame
from game import Game
from menu_and_pause import *

pygame.init()  # Инициализируем pygame в начале чтобы работали шрифты во время инициализации классов меню


class ChristmasJumps:
    """Класс со всей игровой логикой"""

    def __init__(self):
        self.state = "menu_main"  # То что мы будем отображать
        self.last_level = None  # Значение последнего запущенного уровня для рестарта
        self.game = Game(self)
        self.level_menu = LevelMenu(self)
        self.main_menu = MainMenu(self)
        self.game_over = GameOverMenu(self)
        self.win_menu = GamePassMenu(self)
        self.brightness = 0  # Яркость экрана
        self.running = True  # Флаг, отвечающий за работу программы

    def set_state(self, state, message=None):
        """Метод который меняет состояние программы"""
        self.state = state
        if state.split("_")[0] == "level":
            # Если мы показываем уровень то предварительно инищиализируем
            self.game.set_level(state.split("_")[1])
            self.last_level = state  # Ставим текущий уровень для рестарта
        elif state.split("_")[0] == "menu" and state.split("_")[1] == "lose":
            # Ставим заголовок проигрыша если нужно отображать меню конца игры
            self.game_over.set_message(message)
        elif state.split("_")[0] == "menu" and state.split("_")[1] == "win":
            self.win_menu.set_message(*message)
        elif state.split("_")[0] == "menu" and state.split("_")[1] == "level":
            self.level_menu.update()
        self.brightness = 0  # Ставим яркость нулевой для плавного перехода

    def _render(self, events):
        state = self.state.split("_")
        if state[0] == "level":
            self.game.render(events, self.brightness)
        elif state[0] == "menu":
            if state[1] == "level":
                self.level_menu.render(events, self.brightness)
            elif state[1] == "main":
                self.main_menu.render(events, self.brightness)
            elif state[1] == "lose":
                self.game_over.render(events, self.brightness)
            elif state[1] == "win":
                self.win_menu.render(events, self.brightness)
        elif state[0] == "quite":
            self.running = False
        elif state[0] == "restart":
            self.set_state(self.last_level)
        if self.brightness < 255:
            # Добавляем яркость каждый фрейм пока она не станет максимальной (255)
            self.brightness += 500 / FPS
            self.brightness = min(255, self.brightness)  # это нужно чтобы яркость не стала больше 255

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
            pygame.display.flip()
        pygame.quit()
