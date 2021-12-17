from Platforms import *
from main_hero import Hero


class Game:
    def __init__(self):
        self.background = pygame.image.load(r"..\Images\background.jpg")
        # Скорость перемещения мира для того чтобы следовать за играком
        self.world_off_cet = 0
        self.platforms = pygame.sprite.Group()  # Платформы на которых прыгает герой
        self.ground = pygame.sprite.Group()  # Платформы земли
        self.main_hero = pygame.sprite.GroupSingle()  # Сам главный герой
        self.set_blocks()
        self.move_world = False

    def set_blocks(self):
        for i in range(0, 1920, 50):
            self.ground.add(Ground((i, 1030)))
            self.platforms.add(SnowPlatform((i, 800)))
        self.main_hero.add(Hero((100, 0)))

    def render(self, events):
        for event in events:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_d:
                self.move_world = True
            if event.type == pygame.KEYUP and event.key == pygame.K_d:
                self.move_world = False
            if event.type == pygame.KEYDOWN and (event.key in [pygame.K_SPACE, pygame.K_w, pygame.K_UP]):
                self.main_hero.sprite.set_jump(True, self.platforms)  # Устанавливаем главному герою прыжок
        if self.move_world:
            self.world_off_cet += 2
        SCREEN.blit(self.background, self.background.get_rect())
        self.platforms.update(self.world_off_cet)
        self.ground.update(self.world_off_cet)
        self.main_hero.update(self.platforms)
        self.platforms.draw(SCREEN)
        self.ground.draw(SCREEN)
        self.main_hero.draw(SCREEN)
