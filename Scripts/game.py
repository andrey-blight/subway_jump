from Platforms import *
from main_hero import Hero


class Game:
    def __init__(self):
        self.background = pygame.image.load(r"..\Images\background.jpg")
        self.move = ""  # Направление движения
        self.world_direction = 0  # Направление изменения мира (0 на месте, 1 направо, -1 налево)
        self.player_direction = 0  # Направление движения игрока по оси x (0 на месте, 1 направо, -1 налево)
        self.platforms = pygame.sprite.Group()  # Платформы на которых прыгает герой
        self.ground = pygame.sprite.Group()  # Платформы земли
        self.main_hero = pygame.sprite.GroupSingle()  # Главный герой
        self.gravity = "down"

    def set_level(self, level):
        if level == '1':
            # self.platforms.clear()
            # self.ground.clear()
            # self.main_hero.clear()
            for x in range(100, 301, 50):
                self.platforms.add(SnowPlatform((x, 600)))
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
                self.ground.add(Ground((x, 1030)))
            self.main_hero.add(Hero((150, 600), self.gravity))

    def render(self, events):
        for event in events:
            if self.gravity == "down":
                if event.type == pygame.KEYDOWN and event.key in [pygame.K_d, pygame.K_RIGHT]:
                    self.move = "right"  # Если нажата стрелочка направо или d то движемся направо
                if event.type == pygame.KEYDOWN and event.key in [pygame.K_a, pygame.K_LEFT]:
                    self.move = "left"  # Если нажата стрелка влево или a то движемся влево
                if event.type == pygame.KEYUP and event.key in [pygame.K_d, pygame.K_RIGHT, pygame.K_a, pygame.K_LEFT]:
                    self.move = ""  # Если отпустили кнопку то не движемся
                if event.type == pygame.KEYDOWN and (event.key in [pygame.K_SPACE, pygame.K_w, pygame.K_UP]):
                    self.main_hero.sprite.set_jump(True, self.platforms)  # Устанавливаем главному герою прыжок
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
            if 480 <= self.main_hero.sprite.get_cords()[0]:
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
        SCREEN.blit(self.background, self.background.get_rect())
        self.platforms.update(self.world_direction)
        self.ground.update(self.world_direction)
        self.main_hero.update(self.player_direction, self.platforms)
        self.platforms.draw(SCREEN)
        self.ground.draw(SCREEN)
        self.main_hero.draw(SCREEN)
