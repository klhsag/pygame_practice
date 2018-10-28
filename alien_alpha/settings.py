from pygame import image

class Settings():
    """ 所有设置 """

    def __init__(self):
        """ 初始化游戏设置 """
        # screen
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (204, 204, 255)

        # ship
        self.ship_limit = 3

        # bullet
        self.bullet_width = 5
        self.bullet_height = 24
        self.bullet_color = 51, 51, 51
        self.bullet_allowed = 6

        # alien
        self.alien_image = image.load('img/alien.png') # 由于始终没有刷新，这张图是隐藏的
        self.fleet_drop_speed = 30

        self.speedup_scale = 1.1

        self.initialize_dynamic_settings()


    def initialize_dynamic_settings(self):
        # ship
        self.ship_speed_factor = 1.5
        # bullet
        self.bullet_speed_factor = 2.0
        # alien
        self.alien_speed_factor = 1.0
        # 1 right | -1 left
        self.fleet_direction = 1

        # score
        self.alien_points = 50


    def increase_speed(self):
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
        # score
        self.alien_points += 10
