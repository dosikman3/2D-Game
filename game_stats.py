class GameStats:
    # Отслеживает статистику для игры
    def __init__(self, ai_game):
        self.high_score = 0
        # Инициализирует статистику
        self.settings = ai_game.settings
        self.reset_stats()

        # Игра запускается в активном состоянии.
        self.game_active = False

    def reset_stats(self):
        # Инициализирует статистику, изменяющуюся в ходе игры
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1
