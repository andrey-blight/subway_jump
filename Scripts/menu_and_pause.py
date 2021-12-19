from platforms import *
from program import *


class AbstractMenu:
    """Класс абстактного меню"""

    def __init__(self, program):
        self.program = program
        self.background = pygame.image.load(r"..\Images\menu_background.jpg").convert_alpha()
        self.buttons = pygame.sprite.Group()

    def render(self, events, brightness):
        if brightness >= 255:  # Реагируем только когда прошла полная анимация
            for event in events:
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    for el in self.buttons.sprites():
                        # Если мышка попала на уровень, то получаем название режима
                        state = el.clicked(*pygame.mouse.get_pos())
                        if state:
                            self.program.set_state(state)  # Меняем режим игры
        self.background.set_alpha(brightness)
        SCREEN.blit(self.background, self.background.get_rect())  # Отображение заднего фона
        self.buttons.update(brightness)
        self.buttons.draw(SCREEN)


class MainMenu(AbstractMenu):
    """Класс главного меню """

    def __init__(self, program):
        super(MainMenu, self).__init__(program)
        font = pygame.font.SysFont("Roboto", 100)
        self.text = font.render('Christmas jumps', True, (34, 139, 34)).convert_alpha()
        self._set_buttons()  # размещаем кнопки

    def _set_buttons(self):
        self.buttons.add(TextButton(275, "Уровни", "menu_level"))
        self.buttons.add(TextButton(425, "О разработчиках", "menu_level"))
        self.buttons.add(TextButton(575, "Выйти из игры", "quite"))

    def render(self, events, brightness):
        super(MainMenu, self).render(events, brightness)
        # Настройки шрифта
        self.text.set_alpha(brightness)
        SCREEN.blit(self.text, (1920 // 2 - self.text.get_width() // 2, 75))  # Отображение текста ровно посередине


class LevelMenu(AbstractMenu):
    """Класс меню с уровнями"""

    def __init__(self, program):
        super(LevelMenu, self).__init__(program)
        font = pygame.font.SysFont("Roboto", 100)
        self.text = font.render('Выберите уровень', True, (34, 139, 34)).convert_alpha()
        self._set_buttons(2)  # Задаем количество уровней в программе

    def _set_buttons(self, count):
        """Метод, который создает заданное количество уровней"""
        x = 100
        y = 275
        for i in range(1, count + 1):
            self.buttons.add(LevelSprite((x, y), i))
            x += 200
            if i % 9 == 0:
                x = 100
                y += 200
        self.buttons.add(BackButton((50, 55), "menu_main"))

    def render(self, events, brightness):
        super(LevelMenu, self).render(events, brightness)
        # Настройки шрифта
        self.text.set_alpha(brightness)
        SCREEN.blit(self.text, (1920 // 2 - self.text.get_width() // 2, 75))  # Отображение текста


class AbstractButton(pygame.sprite.Sprite):
    """Класс абстрактной кнопки на которую можно нажать"""

    def __init__(self, pos, size):
        super().__init__()
        self.size = size
        self.image = pygame.Surface((size[0], size[1]), pygame.SRCALPHA, 32)  # Прозрачный surface
        self.rect = pygame.rect.Rect(pos[0], pos[1], size[0], size[1])

    def clicked(self, x, y):
        """Метод который проверяет нажали ли на ячейку"""
        if self.rect.x <= x <= self.rect.x + self.size[0] and self.rect.y <= y <= self.rect.y + self.size[1]:
            return True
        return False

    def update(self, brightness):
        self.image = pygame.Surface((self.size[0], self.size[1]), pygame.SRCALPHA, 32)


class TextButton(AbstractButton):
    """Класс текстовой кнопки"""

    def __init__(self, height, text, state):
        font = pygame.font.SysFont("Roboto", 80)
        self.text = font.render(text, True, (211, 255, 94)).convert_alpha()
        super().__init__((1920 // 2 - self.text.get_width() // 2, height), self.text.get_size())
        self.image.blit(self.text, (0, 0))
        self.state = state

    def clicked(self, x, y):
        if super(TextButton, self).clicked(x, y):
            return self.state

    def update(self, brightness):
        super(TextButton, self).update(brightness)
        self.text.set_alpha(brightness)
        self.image.blit(self.text, (0, 0))


class LevelSprite(AbstractButton):
    """Класс иконки с уровнем"""
    SIZE = 100  # Размер одного блока
    IMAGE = pygame.image.load(r"..\Images\snowflake_level.png").convert_alpha()

    def __init__(self, pos, number):
        super().__init__(pos, (self.SIZE, self.SIZE))
        self.level = number  # Номер уровня
        self.image.blit(self.IMAGE, (0, 0))  # Добавляем изображение
        font = pygame.font.SysFont("Roboto", 60)
        self.text = font.render(f'{number}', True, (211, 255, 94)).convert_alpha()
        # Размещаем номер уровня ровно по центру снежинки
        self.image.blit(self.text, (100 // 2 - self.text.get_width() // 2,
                                    100 // 2 - self.text.get_height() // 2))

    def clicked(self, x, y):
        if super(LevelSprite, self).clicked(x, y):
            return f"level_{self.level}"

    def update(self, brightness):
        super(LevelSprite, self).update(brightness)
        # Задаем яркость и заново отображаем
        self.IMAGE.set_alpha(brightness)
        self.text.set_alpha(brightness)
        self.image.blit(self.IMAGE, (0, 0))
        self.image.blit(self.text, (100 // 2 - self.text.get_width() // 2,
                                    100 // 2 - self.text.get_height() // 2))


class BackButton(AbstractButton):
    """Класс кнопки назад"""
    SIZE = 100  # Размер одного блока
    IMAGE = pygame.image.load(r"..\Images\back.png").convert_alpha()

    def __init__(self, pos, state):
        super().__init__(pos, (self.SIZE, self.SIZE))
        self.state = state
        self.image.blit(self.IMAGE, (0, 0))  # Добавляем изображение

    def clicked(self, x, y):
        if super(BackButton, self).clicked(x, y):
            return self.state

    def update(self, brightness):
        super(BackButton, self).update(brightness)
        # Задаем яркость и заново отображаем
        self.IMAGE.set_alpha(brightness)
        self.image.blit(self.IMAGE, (0, 0))
