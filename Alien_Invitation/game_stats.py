class GameStats:
	"""Track the statistics of the game"""
	def __init__(self, ai_game):
		"""initialize statistics"""
		self.settings = ai_game.settings
		self.reset_stats()
		self.game_active = False
		self.high_score = 0

	def reset_stats(self):
		"""stats that can change during game"""
		self.ships_left = self.settings.ship_limit
		self.score = 0
		self.level = 1
