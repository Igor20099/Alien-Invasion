import pygame

class Ship():
    def __init__(self,screen,ai_settings):
        """Инициализирует корабль и задает его начальную позицию."""
        self.screen = screen

        #Загрузка изображения корабля и получение прямоугольника.
        self.image = pygame.image.load('images/ship.bmp')
        self.image = pygame.transform.scale(self.image,(100,100))
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.ai_settings = ai_settings
        #Каждый новый корабль появляется у нижнего края экрана.
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        #Флаги перемещения.
        self.moving_right = False
        self.moving_left = False
        self.center = float(self.rect.centerx)

    def update(self):
        """Обновляет позицию корабля с учетом флага."""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center-= self.ai_settings.ship_speed_factor  
        self.rect.centerx = self.center
    def blitme(self):
        """рисует корабль в текущей позиции."""
        self.screen.blit(self.image,self.rect)    