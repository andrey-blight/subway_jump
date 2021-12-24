import time
from platforms import *
from bonuses import *
from main_hero import Hero


class Game:
    def __init__(self, program):
        self.level = None
        self.program = program  # Программа, в которой мы будем менять состояние
        self.background = pygame.image.load(r"..\Images\background.jpg").convert_alpha()
        self.font = pygame.font.SysFont("Roboto", 100)
        self.start_time = None
        self.time_text = self.font.render('0', True, (34, 139, 34)).convert_alpha()
        self.money = pygame.image.load(r"..\Images\money_count.png").convert_alpha()
        self.money_count = 0
        self.money_count_text = self.font.render(f'{self.money_count}/5', True, (34, 139, 34)).convert_alpha()
        self.move = ""  # Направление движения
        self.world_direction = 0  # Направление изменения мира (0 на месте, 1 направо, -1 налево)
        self.player_direction = 0  # Направление движения игрока по оси x (0 на месте, 1 направо, -1 налево)
        self.platforms = pygame.sprite.Group()  # Платформы на которых прыгает герой
        self.enemies = pygame.sprite.Group()  # Все что убивает игрока при касании
        self.main_hero = pygame.sprite.GroupSingle()  # Главный герой
        self.finish = pygame.sprite.GroupSingle()  # Финиш уровня
        self.bonuses = pygame.sprite.Group()  # Все бонусы которые может всять гг
        self.gravity = "down"  # Направление гравитации

    def add_money(self):
        self.money_count += 1
        self.money_count_text = self.font.render(f'{self.money_count}/5', True, (34, 139, 34)).convert_alpha()

    def _clear_game(self):
        """Метод который очищает все группы и движения"""
        self.gravity = "down"
        self.start_time = None
        self.time_text = self.font.render('0', True, (34, 139, 34)).convert_alpha()
        self.bonuses = pygame.sprite.Group()  # Все бонусы которые может всять гг
        self.platforms = pygame.sprite.Group()  # Платформы на которых прыгает герой
        self.enemies = pygame.sprite.Group()  # Платформы земли
        self.main_hero = pygame.sprite.GroupSingle()  # Главный герой
        self.finish = pygame.sprite.GroupSingle()  # Финиш уровня
        self.world_direction = 0  # Направление изменения мира (0 на месте, 1 направо, -1 налево)
        self.player_direction = 0  # Направление движения игрока по оси x (0 на месте, 1 направо, -1 налево)
        self.move = ""  # Направление движения
        self.money_count = 0
        self.money_count_text = self.font.render(f'{self.money_count}/5', True, (34, 139, 34)).convert_alpha()

    def set_level(self, level):
        self.level = int(level)
        self._clear_game()
        if level == '1':  # Генерация первого уровня
            for x in range(100, 301, 50):
                self.platforms.add(SnowPlatform((x, 600)))
            self.platforms.add(SnowPlatform((520, 800)))
            self.bonuses.add(Money((-100, 870)))
            self.platforms.add(SnowPlatform((-100, 900)))
            for x in range(150, 300, 50):
                self.platforms.add(SnowPlatform((x, 900)))
            self.bonuses.add(Money((150, 870)))
            for x in range(470, 650, 50):
                self.platforms.add(SnowPlatform((x, 400)))
            for x in range(1000, 1150, 50):
                self.platforms.add(SnowPlatform((x, 800)))
            self.bonuses.add(Money((1100, 770)))
            for x in range(1250, 1251, 50):
                self.platforms.add(SnowPlatform((x, 600)))
            for x in range(1400, 1501, 50):
                self.platforms.add(SnowPlatform((x, 450)))
            for x in range(1700, 1900, 50):
                self.platforms.add(SnowPlatform((x, 850)))
            self.bonuses.add(Money((1700, 820)))
            self.bonuses.add(Money((1800, 600)))
            for x in range(-500, 2500, 50):
                self.enemies.add(Ground((x, 1030)))
            self.finish.add(Finish((1850, 800)))
            self.main_hero.add(Hero((150, 540), self))
        elif level == "2":
            for x in range(900, 1200, 50):
                self.platforms.add(SnowPlatform((x, 800)))
            self.platforms.add(SnowPlatform((1350, 900)))
            self.bonuses.add(Money((1360, 870)))
            self.platforms.add(SnowPlatform((1350, 700)))
            self.bonuses.add(Money((1360, 670)))
            for x in range(1600, 1800, 50):
                self.platforms.add(SnowPlatform((x, 800)))
            self.bonuses.add(Money((1750, 770)))
            self.bonuses.add(GravityUp((1650, 750)))
            for x in range(1400, 1601, 50):
                self.platforms.add(SnowPlatform((x, 300)))
            self.platforms.add(SnowPlatform((1750, 150)))
            self.bonuses.add(Money((1760, 200)))
            for x in range(1000, 1250, 50):
                self.platforms.add(SnowPlatform((x, 150)))
            for x in range(600, 850, 50):
                self.platforms.add(SnowPlatform((x, 300)))
            for x in range(200, 400, 50):
                self.platforms.add(SnowPlatform((x, 100)))
            self.bonuses.add(GravityDown((200, 150)))
            for x in range(300, 500, 50):
                self.platforms.add(SnowPlatform((x, 800)))
            self.bonuses.add(Money((310, 770)))
            self.finish.add(Finish((450, 750)))
            for x in range(-500, 2500, 50):
                self.enemies.add(Ground((x, 1030)))
            self.main_hero.add(Hero((900, 740), self))

    def _groups_update(self, brightness):
        """Метод который обновляет все группы спрайтов"""
        self.bonuses.update(self.world_direction, brightness)
        self.platforms.update(self.world_direction, brightness)
        self.enemies.update(self.world_direction, brightness)
        self.finish.update(self.world_direction, brightness)
        self.main_hero.update(self.player_direction, brightness)
        self.platforms.draw(SCREEN)
        self.bonuses.draw(SCREEN)
        self.enemies.draw(SCREEN)
        self.finish.draw(SCREEN)
        self.main_hero.draw(SCREEN)

    def render(self, events, brightness):
        # Реагируем на нажатия клавиш только в случае если меню полностью прогрузилось
        if brightness >= 255:
            if self.start_time is None:
                self.start_time = time.time()
            for event in events:
                if event.type == pygame.KEYDOWN and event.key in [pygame.K_d, pygame.K_RIGHT]:
                    self.move = "right"  # Если нажата стрелочка направо или d то движемся направо
                if event.type == pygame.KEYDOWN and event.key in [pygame.K_a, pygame.K_LEFT]:
                    self.move = "left"  # Если нажата стрелка влево или a то движемся влево
                if event.type == pygame.KEYUP and event.key in [pygame.K_d, pygame.K_RIGHT, pygame.K_a,
                                                                pygame.K_LEFT]:
                    self.move = ""  # Если отпустили кнопку то не движемся
                if self.gravity == "down":
                    if event.type == pygame.KEYDOWN and (event.key in [pygame.K_SPACE, pygame.K_w, pygame.K_UP]):
                        self.main_hero.sprite.set_jump(True)  # Устанавливаем главному герою прыжок
                elif self.gravity == "up":
                    if event.type == pygame.KEYDOWN and (event.key in [pygame.K_SPACE, pygame.K_s, pygame.K_DOWN]):
                        self.main_hero.sprite.set_jump(True)  # Устанавливаем главному герою прыжок
            if self.move == "right":
                self.main_hero.sprite.move("right")
                if self.main_hero.sprite.get_cords()[0] <= 1440:
                    # Если движимся направо и игрок не дошел до определенной границы то перемещаем персонажа
                    self.player_direction = 1
                    self.world_direction = 0
                else:
                    # Если игрок перешел границу то двигаем мир
                    self.player_direction = 0
                    self.world_direction = 1
            elif self.move == "left":
                self.main_hero.sprite.move("left")
                if 400 <= self.main_hero.sprite.get_cords()[0]:
                    # Если движимся налево и игрок не дошел до определенной границы то перемещаем персонажа
                    self.player_direction = -1
                    self.world_direction = 0
                else:
                    # Если игрок перешел границу то двигаем мир
                    self.player_direction = 0
                    self.world_direction = -1
            else:
                # Если не движимся то убрать все направления
                self.main_hero.sprite.move("stand")
                self.player_direction = 0
                self.world_direction = 0
        if self.start_time is not None:
            self.time_text = self.font.render(f'{int(time.time() - self.start_time)}', True,
                                              (34, 139, 34)).convert_alpha()
        self.background.set_alpha(brightness)  # Устанавливаем яркость
        self.money.set_alpha(brightness)
        self.money_count_text.set_alpha(brightness)
        self.time_text.set_alpha(brightness)
        SCREEN.blit(self.background, self.background.get_rect())
        SCREEN.blit(self.money, (20, 20, self.money.get_width(), self.money.get_height()))
        SCREEN.blit(self.money_count_text, (120, 30, self.money_count_text.get_width(),
                                            self.money_count_text.get_height()))
        SCREEN.blit(self.time_text, (1700, 30, self.time_text.get_width(), self.time_text.get_height()))
        self._groups_update(brightness)
