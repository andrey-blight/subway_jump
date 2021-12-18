from constants import *


class Hero(pygame.sprite.Sprite):
    def __init__(self, pos, gravity):
        super().__init__()
        self.image = pygame.Surface((25, 50))
        self.image.fill('red')
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

    def update(self, direction, platforms):
        self.rect = self.rect.move(self.speed_x, self.speed_y)  # Перемещение по с заданными скоростями
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
            if direction == 1:
                self.rect.move_ip(SIDE_SPEED, 0)
            elif direction == -1:
                self.rect.move_ip(-SIDE_SPEED, 0)
