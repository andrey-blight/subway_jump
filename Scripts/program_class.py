# Файл в котором лежит главный класс который осуществляет логику игры
import pygame


class ChristmasJumps:
    @staticmethod
    def start_game():
        """Функция которая запускает основной цикл игры"""
        pygame.init()
        screen = pygame.display.set_mode((1000, 600))
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            screen.fill((0, 0, 0))
            pygame.display.flip()
        pygame.quit()


ChristmasJumps.start_game()
