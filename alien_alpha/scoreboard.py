import pygame.font

from font_info import game_font

class Scoreboard():
    """docstring for Scoreboard"""
    def __init__(self, ai_settings, screen, stats):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.ai_settings = ai_settings
        self.stats = stats

        tc = self.ai_settings.bg_color
        self.text_color = (255 - tc[0], 255 - tc[1], 255 - tc[2])
        self.font = pygame.font.Font(game_font('impact'), 30)

        self.prep_all()

    def prep_all(self):
        self.prep_score()
        self.prep_level()

    def prep_score(self):
        score_str = "score " + "{:,}".format(self.stats.score)
        self.score_image = self.font.render(score_str, True, self.text_color) #self.ai_settings.bg_color) 透明

        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right -20
        self.score_rect.top = 20

    def prep_level(self):
        level_str = "round " + "{:,}".format(self.stats.level)
        self.level_image = self.font.render(level_str, True, self.text_color) #self.ai_settings.bg_color)

        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.score_rect.right
        self.level_rect.top = self.score_rect.bottom + 10

    def show_score(self):
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.level_image, self.level_rect)
