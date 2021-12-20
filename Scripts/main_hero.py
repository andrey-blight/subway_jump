from constants import *
from platforms import Ground


class Hero(pygame.sprite.Sprite):
    def __init__(self, pos, gravity, program):
        super().__init__()
        self.program = program
        self.image = pygame.Surface((25, 50))
        self.image.fill('red')
        self.image.convert_alpha()
        self.rect = self.image.get_rect(topleft=pos)
        #               ФИЗИКА
        self.speed_x = 0  # Скорость по горизонтали
        self.speed_y = 0  # Скорость по вертикали
        self.gravity = gravity  # Направление гравитации
        self.jump = False  # Прыжок персонажа

    def get_cords(self):
        return self.rect.x, self.rect.y

    def get_collide_borders(self, platforms):
        """Метод который возвращает платформы, на которых стоит главный герой"""
        if self.gravity == "down":
            # Если гравитация направлена вниз, то формируем все границы платформ
            borders = pygame.sprite.Group()
            for border in platforms.sprites():
                borders.add(border.get_top_border().sprite)
            borders_collide = pygame.sprite.spritecollide(self, borders, False)
            return borders_collide if borders_collide else False

    def set_jump(self, value, platforms):
        """Метод который устанавливает герою значение прыжка"""
        if not self.get_collide_borders(platforms) and value:
            # Если герой находится в воздухе, то мы не можем прыгать
            value = False
        self.jump = value

    def update(self, direction, brightness, platforms, finish, enemies):
        self.image.set_alpha(brightness)
        if brightness < 255:
            return
        if pygame.sprite.spritecollide(self, finish, False):
            self.program.set_state("menu_level")  # Если дошли до финиша
        if enemy := pygame.sprite.spritecollide(self, enemies, False) or self.rect.y > HEIGHT:
            message = "None"
            if type(enemy[0]) == Ground or self.rect.y > HEIGHT:
                message = "Вы упали на землю"
            self.program.set_state("menu_lose", message)  # Если погибли
        self.rect.move_ip(self.speed_x, self.speed_y)  # Перемещение по с заданными скоростями
        # Получаем список всех границ на которых стоит главный герой
        collide_border = self.get_collide_borders(platforms)
        if self.gravity == "down":
            if collide_border:
                if self.jump:
                    # Если игрок столкнулся с землей и нажал пробел то отталкиваемся от земли
                    # Формула расчета скорости для заданного ускорения свободного падения и высоты прыжка
                    self.speed_y = -(2 * G * JUMP_HEIGHT) ** 0.5
                    self.set_jump(False, platforms)  # Убираем прыжок у персонажа
                else:
                    # Иначе убираем скорость и смещение от падения
                    self.rect.y = collide_border[0].get_block().rect.y - self.rect.height
                    self.speed_y = 0
            else:
                # Добавляем ускорение свободного падения если нет опоры
                self.speed_y += G
            if direction == 1:  # Движение направо
                self.speed_x = SIDE_SPEED
            elif direction == -1:  # Движение налево
                self.speed_x = -SIDE_SPEED
            else:
                self.speed_x = 0
