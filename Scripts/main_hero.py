import time
from constants import *
from platforms import *
from bonuses import *


class Hero(pygame.sprite.Sprite):
    STAND_IMG_DOWN = pygame.image.load(r"../Images/MainHeroStand/1.png").convert_alpha()
    STAND_IMG_UP = pygame.transform.rotate(STAND_IMG_DOWN, 180)
    RIGHT_IMGS_DOWN = [pygame.image.load(r"../Images/MainHeroGoRight/1.png").convert_alpha(),
                       pygame.image.load(r"../Images/MainHeroGoRight/2.png").convert_alpha(),
                       pygame.image.load(r"../Images/MainHeroGoRight/3.png").convert_alpha(),
                       pygame.image.load(r"../Images/MainHeroGoRight/4.png").convert_alpha(),
                       pygame.image.load(r"../Images/MainHeroGoRight/5.png").convert_alpha(),
                       pygame.image.load(r"../Images/MainHeroGoRight/6.png").convert_alpha(),
                       pygame.image.load(r"../Images/MainHeroGoRight/7.png").convert_alpha(),
                       pygame.image.load(r"../Images/MainHeroGoRight/8.png").convert_alpha()]
    RIGHT_IMGS_UP = [pygame.transform.rotate(image, 180) for image in RIGHT_IMGS_DOWN]
    LEFT_IMGS_DOWN = [pygame.image.load(r"../Images/MainHeroGoLeft/1.png").convert_alpha(),
                      pygame.image.load(r"../Images/MainHeroGoLeft/2.png").convert_alpha(),
                      pygame.image.load(r"../Images/MainHeroGoLeft/3.png").convert_alpha(),
                      pygame.image.load(r"../Images/MainHeroGoLeft/4.png").convert_alpha(),
                      pygame.image.load(r"../Images/MainHeroGoLeft/5.png").convert_alpha(),
                      pygame.image.load(r"../Images/MainHeroGoLeft/6.png").convert_alpha(),
                      pygame.image.load(r"../Images/MainHeroGoLeft/7.png").convert_alpha(),
                      pygame.image.load(r"../Images/MainHeroGoLeft/8.png").convert_alpha()]
    LEFT_IMGS_UP = [pygame.transform.rotate(image, 180) for image in LEFT_IMGS_DOWN]
    RIGHT_JUMP_IMGS_DOWN = [pygame.image.load(r"../Images/MainHeroRightJump/1.png").convert_alpha(),
                            pygame.image.load(r"../Images/MainHeroRightJump/2.png").convert_alpha(),
                            pygame.image.load(r"../Images/MainHeroRightJump/3.png").convert_alpha(),
                            pygame.image.load(r"../Images/MainHeroRightJump/4.png").convert_alpha(),
                            pygame.image.load(r"../Images/MainHeroRightJump/5.png").convert_alpha(),
                            pygame.image.load(r"../Images/MainHeroRightJump/6.png").convert_alpha()]
    RIGHT_JUMP_IMGS_UP = [pygame.transform.rotate(image, 180) for image in RIGHT_JUMP_IMGS_DOWN]
    LEFT_JUMP_IMGS_DOWN = [pygame.image.load(r"../Images/MainHeroLeftJump/1.png").convert_alpha(),
                           pygame.image.load(r"../Images/MainHeroLeftJump/2.png").convert_alpha(),
                           pygame.image.load(r"../Images/MainHeroLeftJump/3.png").convert_alpha(),
                           pygame.image.load(r"../Images/MainHeroLeftJump/4.png").convert_alpha(),
                           pygame.image.load(r"../Images/MainHeroLeftJump/5.png").convert_alpha(),
                           pygame.image.load(r"../Images/MainHeroLeftJump/6.png").convert_alpha()]
    LEFT_JUMP_IMGS_UP = [pygame.transform.rotate(image, 180) for image in LEFT_JUMP_IMGS_DOWN]
    JUMP_IMGS_DOWN = [pygame.image.load(r"../Images/MainHeroJump/1.png").convert_alpha(),
                      pygame.image.load(r"../Images/MainHeroJump/2.png").convert_alpha(),
                      pygame.image.load(r"../Images/MainHeroJump/3.png").convert_alpha(),
                      pygame.image.load(r"../Images/MainHeroJump/4.png").convert_alpha(),
                      pygame.image.load(r"../Images/MainHeroJump/5.png").convert_alpha(),
                      pygame.image.load(r"../Images/MainHeroJump/6.png").convert_alpha()]
    JUMP_IMGS_UP = [pygame.transform.rotate(image, 180) for image in JUMP_IMGS_DOWN]

    def __init__(self, pos, game):
        super().__init__()
        self.animation = 0
        self.clear = True
        self.game = game
        self.program = game.program
        self.image = self.STAND_IMG_DOWN
        self.rect = self.image.get_rect(topleft=pos)
        #               ФИЗИКА
        self.platforms = game.platforms
        self.speed_x = 0  # Скорость по горизонтали
        self.speed_y = 0  # Скорость по вертикали
        self.gravity = game.gravity  # Направление гравитации
        self.jump = False  # Прыжок персонажа
        # Задаем границы для подсчета колизий главного игрока
        self.top_border = pygame.sprite.GroupSingle()
        self.down_border = pygame.sprite.GroupSingle()
        self.left_border = pygame.sprite.GroupSingle()
        self.right_border = pygame.sprite.GroupSingle()
        self.set_borders()

    def move(self, direction):
        self.animation += 1
        if self.animation > 119:
            self.animation = 0
        if direction == "right":
            if self.gravity == "down":
                if self.is_ground():
                    self.image = self.RIGHT_IMGS_DOWN[self.animation // 15]
                else:
                    if self.clear:
                        self.animation = 0
                        self.clear = False
                    self.image = self.RIGHT_JUMP_IMGS_DOWN[self.animation // 20]
            if self.gravity == "up":
                if self.is_ceiling():
                    self.image = self.LEFT_IMGS_UP[self.animation // 15]
                else:
                    if self.clear:
                        self.animation = 0
                        self.clear = False
                    self.image = self.LEFT_JUMP_IMGS_UP[self.animation // 20]
        elif direction == "left":
            if self.gravity == "down":
                if self.is_ground():
                    self.image = self.LEFT_IMGS_DOWN[self.animation // 15]
                else:
                    if self.clear:
                        self.animation = 0
                        self.clear = False
                    self.image = self.LEFT_JUMP_IMGS_DOWN[self.animation // 20]
            if self.gravity == "up":
                if self.is_ceiling():
                    self.image = self.RIGHT_IMGS_UP[self.animation // 15]
                else:
                    if self.clear:
                        self.animation = 0
                        self.clear = False
                    self.image = self.RIGHT_JUMP_IMGS_UP[self.animation // 20]
        elif direction == "stand":
            if self.gravity == "down":
                if self.is_ground():
                    self.image = self.STAND_IMG_DOWN
                else:
                    if self.clear:
                        self.animation = 0
                        self.clear = False
                    self.image = self.JUMP_IMGS_DOWN[self.animation // 20]
            elif self.gravity == "up":
                if self.is_ceiling():
                    self.image = self.STAND_IMG_UP
                else:
                    if self.clear:
                        self.animation = 0
                        self.clear = False
                    self.image = self.JUMP_IMGS_UP[self.animation // 20]

    def set_borders(self):
        if self.gravity == "down":
            self.top_border.add(
                Border(self.rect.x + 15, self.rect.y - 1, self.rect.x + self.rect.width - 15, self.rect.y - 3, 1))
            self.down_border.add(
                Border(self.rect.x + 5, self.rect.y + self.rect.height, self.rect.x + self.rect.width - 5,
                       self.rect.y + self.rect.height, 1))
            self.left_border.add(
                Border(self.rect.x - 1, self.rect.y + 10, self.rect.x - 1, self.rect.y + self.rect.height - 25, 1))
            self.right_border.add(
                Border(self.rect.x + self.rect.width, self.rect.y + 10, self.rect.x + self.rect.width,
                       self.rect.y + self.rect.height - 25, 1))
        elif self.gravity == "up":
            self.top_border.add(
                Border(self.rect.x + 5, self.rect.y - 1, self.rect.x + self.rect.width - 15, self.rect.y - 3, 1))
            self.down_border.add(
                Border(self.rect.x + 15, self.rect.y + self.rect.height, self.rect.x + self.rect.width - 5,
                       self.rect.y + self.rect.height, 1))
            self.left_border.add(
                Border(self.rect.x - 1, self.rect.y + 12, self.rect.x - 1, self.rect.y + self.rect.height - 25, 1))
            self.right_border.add(
                Border(self.rect.x + self.rect.width, self.rect.y + 12, self.rect.x + self.rect.width,
                       self.rect.y + self.rect.height - 25, 1))

    def get_cords(self):
        return self.rect.x, self.rect.y

    def is_ground(self):
        """Метод который возвращает платформу снизу игрока"""
        return pygame.sprite.spritecollideany(self.down_border.sprite, self.platforms)

    def is_ceiling(self):
        """Метод который возвращает платформу сверху игрока"""
        return pygame.sprite.spritecollideany(self.top_border.sprite, self.platforms)

    def is_left(self):
        """Метод который возвращает блатформу левее игрока"""
        return pygame.sprite.spritecollideany(self.left_border.sprite, self.platforms)

    def is_right(self):
        """Метод который возвращает блатформу правее игрока"""
        return pygame.sprite.spritecollideany(self.right_border.sprite, self.platforms)

    def set_jump(self, value):
        """Метод который устанавливает герою значение прыжка"""
        if value:
            # Если герой находится в воздухе, то мы не можем прыгать
            if self.gravity == "down" and not self.is_ground():
                value = False
            elif self.gravity == "up" and not self.is_ceiling():
                value = False
        self.jump = value
        self.clear = value

    def move_border(self, x, y):
        self.top_border.update(x, y)
        self.down_border.update(x, y)
        self.left_border.update(x, y)
        self.right_border.update(x, y)

    def update(self, direction, brightness):
        self.image.set_alpha(brightness)  # Установка яркости
        if brightness < 255:  # Если мы в процессе отрисовки то больше ничего не делаем
            return
        if pygame.sprite.spritecollide(self, self.game.finish, False):
            # Если дошли до финиша то подсчитываем результат и ставим меню выйгрыша
            if self.game.level == 1:
                money = self.game.money_count >= 5
                b_time = int(time.time() - self.game.start_time) <= 10
                self.program.set_state("menu_win", ["10", money, b_time, 1])
            elif self.game.level == 2:
                money = self.game.money_count >= 5
                b_time = int(time.time() - self.game.start_time) <= 15
                self.program.set_state("menu_win", ["15", money, b_time, 2])
        if enemy := pygame.sprite.spritecollideany(self, self.game.enemies) or self.rect.y > HEIGHT or self.rect.y < 0:
            # Если погибли то отображаем окно проигрыша с причиной смерти,
            message = "None"
            if type(enemy) == Ground or self.rect.y > HEIGHT:
                message = "Вы упали на землю"
            elif self.rect.y < 0:
                message = "Вы улетели в небо"
            self.program.set_state("menu_lose", message)
        if bonus := pygame.sprite.spritecollideany(self, self.game.bonuses):
            if type(bonus) == Money:
                self.game.add_money()  # Если взяли бонус то добавляем монетку
            elif type(bonus) == GravityUp:
                self.game.gravity = "up"  # Если взяли бонус то добавляем монетку
                self.gravity = "up"
                self.set_borders()
            elif type(bonus) == GravityDown:
                self.game.gravity = "down"  # Если взяли бонус то добавляем монетку
                self.gravity = "down"
                self.set_borders()
            bonus.kill()  # Удаляем монетку
        self.rect.move_ip(self.speed_x, self.speed_y)  # Перемещение по с заданными скоростями
        self.move_border(self.speed_x, self.speed_y)  # Двигаем невидимую рамку вслед за персонажем
        # Получаем объекты в которые мы попали с каждой стороны
        ground_block = self.is_ground()
        ceiling_block = self.is_ceiling()
        left_block = self.is_left()
        right_block = self.is_right()
        if self.gravity == "down":
            if ceiling_block:
                # Если попали на блок всерху то не даем прыгнуть выше
                y = self.rect.y
                self.rect.y = ceiling_block.get_coords()[1] + StandardBlock.BLOCK_SIZE + 1
                self.speed_y = 0
                if self.rect.y != y:
                    self.set_borders()
            if ground_block:
                if self.jump:
                    # Если игрок столкнулся с землей и нажал пробел то отталкиваемся от земли
                    # Формула расчета скорости для заданного ускорения свободного падения и высоты прыжка
                    self.speed_y = -(2 * G * JUMP_HEIGHT) ** 0.5
                    self.jump = False  # Убираем прыжок у персонажа
                else:
                    # Иначе убираем скорость и смещение от падения
                    y = self.rect.y
                    self.rect.y = ground_block.get_coords()[1] - self.rect.height
                    self.speed_y = 0
                    if self.rect.y != y:
                        self.set_borders()
            else:
                # Добавляем ускорение свободного падения если нет опоры
                self.speed_y += G
        elif self.gravity == "up":
            if ceiling_block:
                if self.jump:
                    # Если игрок столкнулся с землей и нажал пробел то отталкиваемся от земли
                    # Формула расчета скорости для заданного ускорения свободного падения и высоты прыжка
                    self.speed_y = (2 * G * JUMP_HEIGHT) ** 0.5
                    self.jump = False  # Убираем прыжок у персонажа
                else:
                    # Иначе убираем скорость и смещение от падения
                    y = self.rect.y
                    self.rect.y = ceiling_block.get_coords()[1] + StandardBlock.BLOCK_SIZE
                    self.speed_y = 0
                    if self.rect.y != y:
                        self.set_borders()
            else:
                # Добавляем ускорение свободного падения если нет опоры
                self.speed_y -= G
                # Если попали на блок всерху то не даем прыгнуть выше
            if ground_block:
                y = self.rect.y
                self.rect.y = ground_block.get_coords()[1] - self.rect.height - 1
                self.speed_y = 0
                if self.rect.y != y:
                    self.set_borders()
        if right_block:
            # Не даем пройти дальше вправо если там блок
            x = self.rect.x
            self.rect.x = right_block.get_coords()[0] - self.rect.width
            self.speed_x = 0
            if self.rect.x != x:
                self.set_borders()
        if left_block:
            # Не даем пройти дальше влево если там блок
            x = self.rect.x
            self.rect.x = left_block.get_coords()[0] + StandardBlock.BLOCK_SIZE
            self.speed_x = 0
            if self.rect.x != x:
                self.set_borders()
        if direction == 1:  # Движение направо
            self.speed_x = SIDE_SPEED
        elif direction == -1:  # Движение налево
            self.speed_x = -SIDE_SPEED
        else:
            self.speed_x = 0  # Стоим на месте
