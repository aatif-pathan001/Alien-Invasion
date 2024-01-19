class Settings:
	""" settings of the game """
	def __init__(self):
		""" display settings"""
		self.screen_weidth = 600
		self.screen_height = 800
		self.bg_color = (0,0,0)
		
		self.ship_limit = 3

		#/// bullet settings
		self.bullet_weidth = 1
		self.bullet_height = 15
		
		self.bullet_color = (250,0,0)
		self.bullet_limit = 3

		#/// alien seettings
		
		self.fleet_drop_speed = 1
		

		self.speedup_scale = 1.5
		self.score_scale = 1.5
		self.dynamic_settings()

	def dynamic_settings(self):
		"""initialize settings that will change in game"""
		self.ship_speed = 3
		self.bullet_speed = 3.0
		self.alien_speed = 1.5
		self.fleet_direction = 2
		self.alien_points = 50

	def level_up(self):
		"""level the speed up"""
		self.ship_speed *= self.speedup_scale
		self.bullet_speed *= self.speedup_scale
		self.alien_speed *= self.speedup_scale
		self.alien_points = int(self.alien_points * self.score_scale)
	
		
