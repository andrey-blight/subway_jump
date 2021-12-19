from platforms import *
from program import *


class LevelMenu:
    """Класс главного меню"""

    def __init__(self, program):
        self.program = program
        self.background = pygame.image.load(r"..\Images\level_background.jpg")
        self.levels = pygame.sprite.Group()
        self._set_levels(2)

    def _set_levels(self, count):
        """Метод, который создает заданное количество уровней"""
        x = 100
        y = 200
        for i in range(1, count + 1):
            self.levels.add(LevelSprite((x, y), i))
            x += 200
            if i % 9 == 0:
                x = 100
                y += 200

    def render(self, events, brightness):
        if brightness >= 255:  # Реагируем только когда прошла полная анимация
            for event in events:
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    for el in self.levels.sprites():
                        # Если мышка попала на уровень, то получаем название режима
                        state = el.clicked(*pygame.mouse.get_pos())
                        if state:
                            self.program.set_state(state)  # Меняем режим игры
        # Настройки шрифта
        font = pygame.font.SysFont("Roboto", 100)
        text = font.render('Выберете уровень', True, (154, 206, 235))
        text.set_alpha(brightness)
        self.background.set_alpha(brightness)
        SCREEN.blit(self.background, self.background.get_rect())  # Отображение заднего фона
        SCREEN.blit(text, (675, 75))  # Отображение текста
        self.levels.update(brightness)
        self.levels.draw(SCREEN)


class LevelSprite(pygame.sprite.Sprite):
    """Класс иконки с уровнем"""
    SIZE = 100  # Размер одного блока
    IMAGE = pygame.image.load(r"..\Images\snowflake_level.png")

    def __init__(self, pos, number):
        super().__init__()
        self.level = number  # Номер уровня
        pygame.font.init()  # Инициализируем шрифт
        self.image = pygame.Surface((self.SIZE, self.SIZE), pygame.SRCALPHA, 32)  # Прозрачный surface
        self.image.blit(self.IMAGE, (0, 0))  # Добавляем изображение
        font = pygame.font.SysFont("Roboto", 60)
        self.text = font.render(f'{number}', True, (234, 230, 202))
        # Если число двузначное то смещаем левее
        if number >= 10:
            self.image.blit(self.text, (25, 35))
        else:
            self.image.blit(self.text, (35, 35))
        self.rect = pygame.rect.Rect(pos[0], pos[1], self.SIZE, self.SIZE)
        self.x = pos[0]
        self.y = pos[1]

    def clicked(self, x, y):
        """Метод который проверяет нажали ли на иконку с уровнем"""
        if self.rect.x <= x <= self.rect.x + self.SIZE and self.rect.y <= y <= self.rect.y + self.SIZE:
            return f"level_{self.level}"
        return False

    def update(self, brightness):
        self.IMAGE.set_alpha(brightness)
        self.text.set_alpha(brightness)
        self.image = pygame.Surface((self.SIZE, self.SIZE), pygame.SRCALPHA, 32)
        self.image.blit(self.IMAGE, (0, 0))
        if self.level >= 10:
            self.image.blit(self.text, (25, 35))
        else:
            self.image.blit(self.text, (35, 35))
