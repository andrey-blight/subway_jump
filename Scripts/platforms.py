from constants import *


class Border(pygame.sprite.Sprite):
    """Празрачная линия для подсчета колизий"""

    def __init__(self, x1, y1, x2, y2, width):
        super().__init__()
        if x1 == x2:  # вертикальная стенка
            self.image = pygame.Surface((width, y2 - y1))
            self.rect = pygame.Rect(x1, y1, width, y2 - y1)
        else:  # горизонтальная стенка
            self.image = pygame.Surface((x2 - x1, width))
            self.rect = pygame.Rect(x1, y1, x2 - x1, width)

    def update(self, x, y):
        self.rect.move_ip(x, y)


class StandardBlock(pygame.sprite.Sprite):
    """Абстрактный класс блока"""
    BLOCK_SIZE = 50  # Размер одного блока

    def __init__(self, pos):
        super().__init__()
        self.image = pygame.surface.Surface((self.BLOCK_SIZE, self.BLOCK_SIZE))
        self.rect = pygame.rect.Rect(pos[0], pos[1], StandardBlock.BLOCK_SIZE, StandardBlock.BLOCK_SIZE)

    def get_coords(self):
        return self.rect.x, self.rect.y

    def update(self, x_direction, brightness):
        self.image.set_alpha(brightness)
        if x_direction == 1:
            self.rect.move_ip(-SIDE_SPEED, 0)
        elif x_direction == -1:
            self.rect.move_ip(SIDE_SPEED, 0)


class SnowPlatform(StandardBlock):
    """Обычная платформа на которой может находиться герой"""
    IMAGE = pygame.image.load(r"..\Images\standard_platform.png").convert_alpha()

    def __init__(self, pos):
        super().__init__(pos)
        self.image = self.IMAGE


class Ground(StandardBlock):
    """Класс земли которого нельзя касаться"""
    IMAGE = pygame.image.load(r"..\Images\ground.jpg").convert_alpha()

    def __init__(self, pos):
        super().__init__(pos)
        self.image = self.IMAGE


class Finish(StandardBlock):
    """Класс финиша при касание которого уровень проходится"""
    IMAGE = pygame.image.load(r"..\Images\finish.png").convert_alpha()

    def __init__(self, pos):
        super().__init__(pos)
        self.image = self.IMAGE
