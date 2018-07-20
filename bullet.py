import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    def __init__(self,ai_settngs,screen,ship):
        """Создает объект пуля в текущей позиции корабля."""
        super(Bullet,self).__init__()
        self.screen = screen

        #Создание пули в позиции (0,0) и назначение правильной позиции
        self.rect = pygame.Rect(0,0,ai_settngs.bullet_width,
                                ai_settngs.bullet_height)
        self.rect.centerx = ship.rectx.centerx
        self.rect.top = ship.rect.top

        #Позиция пули хранится в вещественном формате.
        self.y = float(self.rect.y)

        self.color = ai_settngs.bullet_color
        self.speed_factor = ai_settngs.bullet_speed_factor

    def update(self):
        """Перемещает пулю вверх по экрану."""
        #Обновление позиции пули в вещественном формате.
        self.y = -= self.speed_factor
        #обновление позиции прямоугольника.
        self.rect.y = self.y
    def draw_bullet(self):
        """Вывод пули на экран."""
        pygame.draw.rect(self.screen,self.color,self.rect)    