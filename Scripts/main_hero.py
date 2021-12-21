from constants import *
from platforms import *


class Hero(pygame.sprite.Sprite):
    def __init__(self, pos, gravity, program, platforms):
        super().__init__()
        self.program = program
        self.image = pygame.Surface((40, 40))
        self.image.fill('red')
        self.image.convert_alpha()
        self.rect = self.image.get_rect(topleft=pos)
        #               ФИЗИКА
        self.platforms = platforms
        self.speed_x = 0  # Скорость по горизонтали
        self.speed_y = 0  # Скорость по вертикали
        self.gravity = gravity  # Направление гравитации
        self.jump = False  # Прыжок персонажа
        # Задаем границы для подсчета колизий главного игрока
        self.top_border = pygame.sprite.GroupSingle()
        self.down_border = pygame.sprite.GroupSingle()
        self.left_border = pygame.sprite.GroupSingle()
        self.right_border = pygame.sprite.GroupSingle()
        self.set_borders()

    def set_borders(self):
        if self.gravity == "down":
            self.top_border.add(
                Border(self.rect.x + 15, self.rect.y - 1, self.rect.x + self.rect.width - 15, self.rect.y - 3, 1))
            self.down_border.add(
                Border(self.rect.x + 5, self.rect.y + self.rect.height, self.rect.x + self.rect.width - 5,
                       self.rect.y + self.rect.height, 1))
            self.left_border.add(
                Border(self.rect.x - 1, self.rect.y + 15, self.rect.x - 1, self.rect.y + self.rect.height - 15, 1))
            self.right_border.add(
                Border(self.rect.x + self.rect.width, self.rect.y + 10, self.rect.x + self.rect.width,
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
        if value and not self.is_ground():
            # Если герой находится в воздухе, то мы не можем прыгать
            value = False
        self.jump = value

    def move_border(self, x, y):
        self.top_border.update(x, y)
        self.down_border.update(x, y)
        self.left_border.update(x, y)
        self.right_border.update(x, y)
        self.top_border.draw(SCREEN)
        self.down_border.draw(SCREEN)
        self.left_border.draw(SCREEN)
        self.right_border.draw(SCREEN)

    def update(self, direction, brightness, finish, enemies):
        self.image.set_alpha(brightness)  # Установка яркости
        if brightness < 255:  # Если мы в процессе отрисовки то больше ничего не делаем
            return
        if pygame.sprite.spritecollide(self, finish, False):
            self.program.set_state("menu_level")  # Если дошли до финиша то выходим в главное меню
        if enemy := pygame.sprite.spritecollideany(self, enemies) or self.rect.y > HEIGHT:
            # Если погибли то отображаем окно проигрыша с причиной смерти,
            message = "None"
            if type(enemy) == Ground or self.rect.y > HEIGHT:
                message = "Вы упали на землю"
            self.program.set_state("menu_lose", message)
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
