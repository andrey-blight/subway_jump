# Файл из которого импортируется главный класс и запускается игра
from program import ChristmasJumps

if __name__ == '__main__':
    game = ChristmasJumps()
    game.start_game()
