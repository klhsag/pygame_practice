import pygame.font

from font_info import game_font

class Button():
    """docstring for Button"""
    def __init__(self, ai_settings, screen, msg):
        super().__init__()
        self.screen = screen
        self.screen_rect = screen.get_rect()

        self.width, self.height = 200, 50
        self.button_color = (204, 102, 102)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.Font(game_font('calibri'), 48)
        #self.font = pygame.font.SysFont('callibri', 48)

        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        self.prep_msg(msg)

    def prep_msg(self, msg):
        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)
