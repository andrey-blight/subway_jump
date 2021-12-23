from platforms import *
from program import *
from database import Database


class AbstractMenu:
    """Класс абстактного меню"""

    def __init__(self, program):
        self.program = program
        self.background = pygame.image.load(r"..\Images\menu_background.jpg").convert_alpha()
        self.buttons = pygame.sprite.Group()

    def render(self, events, brightness):
        # Проверяем нажатия только после полной отрисовки меню
        if brightness >= 255:
            for event in events:
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    for el in self.buttons.sprites():
                        # Если мышка попала на уровень, то получаем название режима и передаем его в программу
                        state = el.clicked(*pygame.mouse.get_pos())
                        if state:
                            self.program.set_state(state)
        self.background.set_alpha(brightness)  # Ставим прозрачность
        SCREEN.blit(self.background, self.background.get_rect())  # Отображение заднего фона
        # обновляем все что есть на экране и рисуем
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
        SCREEN.blit(self.text, (WIDTH // 2 - self.text.get_width() // 2, 75))  # Отображение текста ровно посередине


class GameOverMenu(AbstractMenu):
    """Класс главного меню"""

    def __init__(self, program):
        super(GameOverMenu, self).__init__(program)
        self.font = pygame.font.SysFont("Roboto", 100)
        self.text = self.font.render('', True, (255, 36, 0)).convert_alpha()
        self._set_buttons()  # размещаем кнопки

    def set_message(self, message):
        """Метод, который устанавливает заголовок проигрыша"""
        self.text = self.font.render(message, True, (255, 36, 0)).convert_alpha()

    def _set_buttons(self):
        self.buttons.add(TextButton(275, "Начать заново", "restart"))
        self.buttons.add(TextButton(425, "Выбрать уровень", "menu_level"))
        self.buttons.add(TextButton(575, "Выйти в главное меню", "menu_main"))
        self.buttons.add(TextButton(725, "Выйти из игры", "quite"))

    def render(self, events, brightness):
        super(GameOverMenu, self).render(events, brightness)
        # Настройки шрифта
        self.text.set_alpha(brightness)
        SCREEN.blit(self.text, (WIDTH // 2 - self.text.get_width() // 2, 75))  # Отображение текста ровно посередине


class GamePassMenu(AbstractMenu):
    """Класс меню прохода уровня"""
    OK_IMAGE = pygame.image.load(r"..\Images\ok.png").convert_alpha()
    BAD_IMAGE = pygame.image.load(r"..\Images\bad.png").convert_alpha()

    def __init__(self, program, ):
        super(GamePassMenu, self).__init__(program)
        self.header_font = pygame.font.SysFont("Roboto", 100)
        self.message_font = pygame.font.SysFont("Roboto", 70)
        self.text_header = self.header_font.render('', True, (34, 139, 34)).convert_alpha()
        self.text_level_pass = self.message_font.render('Пройти уровень', True, (71, 74, 81)).convert_alpha()
        self.text_time = self.message_font.render('', True, (71, 74, 81)).convert_alpha()
        self.text_money = self.message_font.render('Собрать все монеты', True, (71, 74, 81)).convert_alpha()
        self.money_img = None
        self.time_img = None
        self.pass_img = None
        self._set_buttons()  # размещаем кнопки

    def set_message(self, time, b_money, b_time, level):
        """Метод, который устанавливает текста уровня"""
        db = Database()
        stars = 1
        if b_time:
            stars += 1
        if b_money:
            stars += 1
        db.set_stars(level, stars)
        self.text_header = self.header_font.render(f"Вы прошли уровень {level}", True, (34, 139, 34)).convert_alpha()
        self.text_time = self.message_font.render(f'Пройти уровень за {time} секунд', True,
                                                  (71, 74, 81)).convert_alpha()
        self.money_img = self.OK_IMAGE if b_money else self.BAD_IMAGE
        self.time_img = self.OK_IMAGE if b_time else self.BAD_IMAGE
        self.pass_img = self.OK_IMAGE

    def _set_buttons(self):
        self.buttons.add(TextButton(250, "Начать заново", "restart", width=1200))
        self.buttons.add(TextButton(375, "Выбрать уровень", "menu_level", width=1200))
        self.buttons.add(TextButton(500, "Выйти в главное меню", "menu_main", width=1200))
        self.buttons.add(TextButton(625, "Выйти из игры", "quite", width=1200))

    def render(self, events, brightness):
        super(GamePassMenu, self).render(events, brightness)
        # Настройки прозрачности
        self.text_header.set_alpha(brightness)
        self.text_level_pass.set_alpha(brightness)
        self.text_time.set_alpha(brightness)
        self.text_money.set_alpha(brightness)
        self.money_img.set_alpha(brightness)
        self.time_img.set_alpha(brightness)
        self.pass_img.set_alpha(brightness)
        SCREEN.blit(self.text_header,
                    (WIDTH // 2 - self.text_header.get_width() // 2, 75))  # Отображение текста ровно посередине
        SCREEN.blit(self.text_level_pass, (100, 250))
        SCREEN.blit(self.text_time, (100, 375))
        SCREEN.blit(self.text_money, (100, 500))
        SCREEN.blit(self.pass_img, (110 + self.text_level_pass.get_width(), 250))
        SCREEN.blit(self.time_img, (110 + self.text_time.get_width(), 375))
        SCREEN.blit(self.money_img, (110 + self.text_money.get_width(), 500))


class LevelMenu(AbstractMenu):
    """Класс меню с уровнями"""

    def __init__(self, program):
        super(LevelMenu, self).__init__(program)
        font = pygame.font.SysFont("Roboto", 100)
        self.text = font.render('Выберите уровень', True, (34, 139, 34)).convert_alpha()

    def update(self):
        """Метод, который создает заданное количество уровней"""
        self.buttons = pygame.sprite.Group()
        db = Database()
        x = 100
        y = 275
        for data in db.get_level_data():
            self.buttons.add(LevelSprite((x, y), *data))
            x += 200
            if data[0] % 9 == 0:
                x = 100
                y += 200
        self.buttons.add(BackButton((50, 55), "menu_main"))

    def render(self, events, brightness):
        super(LevelMenu, self).render(events, brightness)
        self.text.set_alpha(brightness)
        SCREEN.blit(self.text, (1920 // 2 - self.text.get_width() // 2, 75))  # Отображение текста ровно посередине


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
        # В апдейте просто очищаем наш surface
        self.image = pygame.Surface((self.size[0], self.size[1]), pygame.SRCALPHA, 32)


class TextButton(AbstractButton):
    """Класс кнопки с текстом"""

    def __init__(self, height, text, state, width=None):
        font = pygame.font.SysFont("Roboto", 80)
        self.text = font.render(text, True, (211, 255, 94)).convert_alpha()
        # Вызываем родительский инициализатор так чтобы он разместил image ровно по центру экрана
        if width is None:
            super().__init__((WIDTH // 2 - self.text.get_width() // 2, height), self.text.get_size())
        else:
            super().__init__((width, height), self.text.get_size())
        self.image.blit(self.text, (0, 0))
        self.state = state  # Состояние игры на которое переносит эта кнопка

    def clicked(self, x, y):
        if super(TextButton, self).clicked(x, y):
            return self.state

    def update(self, brightness):
        super(TextButton, self).update(brightness)
        self.text.set_alpha(brightness)  # Установка яркости
        self.image.blit(self.text, (0, 0))


class LevelSprite(AbstractButton):
    """Класс иконки с уровнем"""
    SIZE = 200  # Размер одного блока
    IMAGE_SNOWFLAKE = pygame.image.load(r"..\Images\snowflake_level.png").convert_alpha()
    IMAGE_GOOD = pygame.image.load(r"..\Images\star_good.png").convert_alpha()
    IMAGE_BAD = pygame.image.load(r"..\Images\star_bad.png").convert_alpha()

    def __init__(self, pos, number, stars):
        super().__init__(pos, (self.SIZE, self.SIZE))
        self.level = number  # Номер уровня
        font = pygame.font.SysFont("Roboto", 60)
        self.text = font.render(f'{number}', True, (211, 255, 94)).convert_alpha()
        self.f_star = self.IMAGE_GOOD if stars > 0 else self.IMAGE_BAD
        self.s_star = self.IMAGE_GOOD if stars > 1 else self.IMAGE_BAD
        self.t_star = self.IMAGE_GOOD if stars > 2 else self.IMAGE_BAD

    def clicked(self, x, y):
        if super(LevelSprite, self).clicked(x, y):
            return f"level_{self.level}"

    def update(self, brightness):
        super(LevelSprite, self).update(brightness)
        # Задаем яркость и заново отображаем
        self.IMAGE_SNOWFLAKE.set_alpha(brightness)
        self.text.set_alpha(brightness)
        self.f_star.set_alpha(brightness)
        self.s_star.set_alpha(brightness)
        self.t_star.set_alpha(brightness)
        self.image.blit(self.IMAGE_SNOWFLAKE, (10, 0))
        self.image.blit(self.f_star, (0, 115))
        self.image.blit(self.s_star, (40, 100))
        self.image.blit(self.t_star, (75, 115))
        self.image.blit(self.text, (110 // 2 - self.text.get_width() // 2,
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
