# Файл в котором лежит главный класс который осуществляет логику игры
import pygame


class ChristmasJumps:
    def __init__(self):
        self.state = "game"
        self.screen = None

    def start_game(self):
        """Функция которая запускает основной цикл игры"""
        pygame.init()
        self.screen = pygame.display.set_mode((1920, 1080))
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            self._render()
        pygame.quit()

    def _render(self):
        if self.state == "game":
            self.screen.fill("black")
            pygame.draw.rect(self.screen, "red", (1000, 500, 50, 50))
