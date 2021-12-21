from platforms import *
from main_hero import Hero


class Game:
    def __init__(self, program):
        self.program = program
        self.background = pygame.image.load(r"..\Images\background.jpg").convert_alpha()
        self.move = ""  # Направление движения
        self.world_direction = 0  # Направление изменения мира (0 на месте, 1 направо, -1 налево)
        self.player_direction = 0  # Направление движения игрока по оси x (0 на месте, 1 направо, -1 налево)
        self.platforms = pygame.sprite.Group()  # Платформы на которых прыгает герой
        self.enemies = pygame.sprite.Group()  # Все что убивает игрока при касании
        self.main_hero = pygame.sprite.GroupSingle()  # Главный герой
        self.finish = pygame.sprite.GroupSingle()  # Финиш уровня
        self.gravity = "down"  # Направление гравитации

    def _clear_game(self):
        """Метод который очищает все группы и движения"""
        self.platforms = pygame.sprite.Group()  # Платформы на которых прыгает герой
        self.enemies = pygame.sprite.Group()  # Платформы земли
        self.main_hero = pygame.sprite.GroupSingle()  # Главный герой
        self.finish = pygame.sprite.GroupSingle()  # Финиш уровня
        self.world_direction = 0  # Направление изменения мира (0 на месте, 1 направо, -1 налево)
        self.player_direction = 0  # Направление движения игрока по оси x (0 на месте, 1 направо, -1 налево)
        self.move = ""  # Направление движения

    def set_level(self, level):
        if level == '1':  # Генерация первого уровня
            self._clear_game()
            for x in range(100, 301, 50):
                self.platforms.add(SnowPlatform((x, 600)))
            self.platforms.add(SnowPlatform((520, 800)))
            self.platforms.add(SnowPlatform((-100, 900)))
            for x in range(150, 300, 50):
                self.platforms.add(SnowPlatform((x, 900)))
            for x in range(470, 650, 50):
                self.platforms.add(SnowPlatform((x, 400)))
            for x in range(1000, 1150, 50):
                self.platforms.add(SnowPlatform((x, 800)))
            for x in range(1250, 1251, 50):
                self.platforms.add(SnowPlatform((x, 600)))
            for x in range(1400, 1501, 50):
                self.platforms.add(SnowPlatform((x, 450)))
            for x in range(1700, 1900, 50):
                self.platforms.add(SnowPlatform((x, 850)))
            for x in range(-500, 2500, 50):
                self.enemies.add(Ground((x, 1030)))
            self.finish.add(Finish((1850, 800)))
            self.main_hero.add(Hero((150, 550), self.gravity, self.program, self.platforms))

    def _groups_update(self, brightness):
        """Метод который обновляет все группы спрайтов"""
        self.platforms.update(self.world_direction, brightness)
        self.enemies.update(self.world_direction, brightness)
        self.finish.update(self.world_direction, brightness)
        self.main_hero.update(self.player_direction, brightness, self.finish, self.enemies)
        self.platforms.draw(SCREEN)
        self.enemies.draw(SCREEN)
        self.finish.draw(SCREEN)
        self.main_hero.draw(SCREEN)

    def render(self, events, brightness):
        if brightness >= 255:
            for event in events:
                if self.gravity == "down":
                    if event.type == pygame.KEYDOWN and event.key in [pygame.K_d, pygame.K_RIGHT]:
                        self.move = "right"  # Если нажата стрелочка направо или d то движемся направо
                    if event.type == pygame.KEYDOWN and event.key in [pygame.K_a, pygame.K_LEFT]:
                        self.move = "left"  # Если нажата стрелка влево или a то движемся влево
                    if event.type == pygame.KEYUP and event.key in [pygame.K_d, pygame.K_RIGHT, pygame.K_a,
                                                                    pygame.K_LEFT]:
                        self.move = ""  # Если отпустили кнопку то не движемся
                    if event.type == pygame.KEYDOWN and (event.key in [pygame.K_SPACE, pygame.K_w, pygame.K_UP]):
                        self.main_hero.sprite.set_jump(True)  # Устанавливаем главному герою прыжок
            if self.move == "right":
                if self.main_hero.sprite.get_cords()[0] <= 1440:
                    # Если движимся направо и игрок не дошел до определенной границы то перемещаем персонажа
                    self.player_direction = 1
                    self.world_direction = 0
                else:
                    # Если игрок перешел границу то двигаем мир
                    self.player_direction = 0
                    self.world_direction = 1
            elif self.move == "left":
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
                self.player_direction = 0
                self.world_direction = 0
        self.background.set_alpha(brightness)
        SCREEN.blit(self.background, self.background.get_rect())
        self._groups_update(brightness)
