from constants import *


class BlockBorder(pygame.sprite.Sprite):
    """Граница для блока"""

    def __init__(self, x1, y1, x2, y2, block):
        super().__init__()
        if x1 == x2:  # вертикальная стенка
            self.image = pygame.Surface((3, y2 - y1))
            self.rect = pygame.Rect(x1, y1, 3, y2 - y1)
        else:  # горизонтальная стенка
            self.image = pygame.Surface((x2 - x1, 3))
            self.rect = pygame.Rect(x1, y1, x2 - x1, 3)
        self.x = x1
        self.y = y1
        self.block = block  # Блок которому принадлежит стенка

    def get_block(self):
        return self.block

    def update(self, x_direction, y_direction):
        if x_direction == 1:
            self.rect.move_ip(-SIDE_SPEED, 0)
        elif x_direction == -1:
            self.rect.move_ip(SIDE_SPEED, 0)


class StandardBlock(pygame.sprite.Sprite):
    """Абстрактный класс блока"""
    BLOCK_SIZE = 50  # Размер одного блока

    def __init__(self, pos):
        super().__init__()
        self.rect = pygame.rect.Rect(pos[0], pos[1], StandardBlock.BLOCK_SIZE, StandardBlock.BLOCK_SIZE)
        self.x = pos[0]
        self.y = pos[1]

    def update(self, x_direction, brightness):
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
        # Добавляем верхнюю границу для блока
        self.top_border = pygame.sprite.GroupSingle()
        self.top_border.add(
            BlockBorder(self.x + 1, self.y - 1, self.x + StandardBlock.BLOCK_SIZE - 1, self.y - 1, self))

    def get_top_border(self):
        return self.top_border

    def update(self, x_direction, brightness):
        super(SnowPlatform, self).update(x_direction, brightness)
        self.top_border.update(x_direction, 0)
        self.image.set_alpha(brightness)
        self.top_border.draw(SCREEN)


class Ground(StandardBlock):
    """Класс земли которого нельзя касаться"""
    IMAGE = pygame.image.load(r"..\Images\ground.jpg").convert_alpha()

    def __init__(self, pos):
        super().__init__(pos)
        self.image = self.IMAGE

    def update(self, x_direction, brightness):
        super(Ground, self).update(x_direction, brightness)
        self.image.set_alpha(brightness)


class Finish(StandardBlock):
    """Класс финиша при касание которого уровень проходится"""
    IMAGE = pygame.image.load(r"..\Images\finish.png").convert_alpha()

    def __init__(self, pos):
        super().__init__(pos)
        self.image = self.IMAGE

    def update(self, x_direction, brightness):
        super(Finish, self).update(x_direction, brightness)
        self.image.set_alpha(brightness)
