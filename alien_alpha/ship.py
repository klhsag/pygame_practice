import pygame

class Ship():

    def __init__(self, ai_settings, screen):
        self.screen = screen
        self.ai_settings = ai_settings

        self.image = pygame.image.load('img/ship.png') # .convert_alpha() may be bug
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        self.center_ship()

        # flag
        self.moving_up = False
        self.moving_right = False
        self.moving_down = False
        self.moving_left = False

    def center_ship(self):
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        self.centerx = float(self.rect.centerx)
        self.centery = float(self.rect.centery)


    def update(self):
        # boarder
        if self.moving_up and self.rect.top > self.screen_rect.bottom - 2*(self.rect.bottom - self.rect.top):
            self.centery -= self.ai_settings.ship_speed_factor
        if self.moving_right and self.rect.centerx < self.screen_rect.right:
            self.centerx += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.centerx > self.screen_rect.left:
            self.centerx -= self.ai_settings.ship_speed_factor
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.centery += self.ai_settings.ship_speed_factor

        self.rect.centerx = self.centerx
        self.rect.centery = self.centery

    def blitme(self):
        """ 指定位置绘制 """
        self.screen.blit(self.image, self.rect)
        
