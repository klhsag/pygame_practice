class GameStats():
    """docstring for GameStats"""
    def __init__(self, ai_settings):
        self.ai_settings = ai_settings
        self.reset_stats()

        # start
        self.game_active = False

    def reset_stats(self):
        """ """
        self.ships_left = self.ai_settings.ship_limit
        self.score = 0
        self.level = 1