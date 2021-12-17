from Platforms import *
from program import *


class LevelMenu:
    def __init__(self, program):
        self.program = program
        self.background = pygame.image.load(r"..\Images\level_background.jpg")
        self.levels = pygame.sprite.Group()
        self.set_levels(30)

    def set_levels(self, count):
        x = 100
        y = 200
        for i in range(1, count + 1):
            self.levels.add(LevelSprite((x, y), i))
            x += 200
            if i % 9 == 0:
                x = 100
                y += 200

    def render(self, events):
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                for el in self.levels.sprites():
                    if el.clicked(*pygame.mouse.get_pos()):
                        self.program.set_state("game")

        font = pygame.font.SysFont("Roboto", 100)
        text = font.render('Главное меню', True, (154, 206, 235))
        SCREEN.blit(self.background, self.background.get_rect())
        SCREEN.blit(text, (675, 75))
        self.levels.draw(SCREEN)


class LevelSprite(pygame.sprite.Sprite):
    SIZE = 100  # Размер одного блока
    IMAGE = pygame.image.load(r"..\Images\snowflake_level.png")

    def __init__(self, pos, number):
        super().__init__()
        self.level = number
        pygame.font.init()
        self.image = pygame.Surface((self.SIZE, self.SIZE), pygame.SRCALPHA, 32)
        self.image.blit(self.IMAGE, (0, 0))
        font = pygame.font.SysFont("Roboto", 60)
        text = font.render(f'{number}', True, (252, 252, 238))
        if number >= 10:
            self.image.blit(text, (25, 35))
        else:
            self.image.blit(text, (35, 35))
        self.rect = pygame.rect.Rect(pos[0], pos[1], self.SIZE, self.SIZE)
        self.x = pos[0]
        self.y = pos[1]

    def clicked(self, x, y):
        if self.rect.x <= x <= self.rect.x + self.SIZE and self.rect.y <= y <= self.rect.y + self.SIZE:
            print(self.level)
            return True
