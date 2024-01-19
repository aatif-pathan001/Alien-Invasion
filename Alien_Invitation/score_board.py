import pygame.font
from pygame.sprite import Group
from ship import Ship
class Scoreboard:
	""" scoring information"""
	def __init__(self,ai_game):
		"""initiallize scorekeeping attributes."""
		self.ai_game = ai_game
		self.screen = ai_game.screen
		self.screen_rect = ai_game.screen.get_rect()
		self.settings = ai_game.settings
		self.stats = ai_game.stats


		# font settings for scoring innformation
		self.text_color = (250,250,250)
		#//// to write the text on the screen 
		self.font = pygame.font.SysFont(None, 48)
		self.prep_score()
		self.prep_high_score()
		self.prep_level()
		self.prep_ships()

	def prep_score(self):
		""" turn the score into rendered image"""
		#//// str function converts no. into string
		#/// render funtion converts the string into image
		round_score = round(self.stats.score, -1)
		score_str = "{:,}".format(round_score)
		self.score_image = self.font.render(score_str, True, self.text_color, self.settings.bg_color)

		self.score_rect = self.score_image.get_rect()
		self.score_rect.right = self.screen_rect.right - 20
		self.score_rect.top = 20

	def show_score(self):
		"""display the score on the screen"""
		self.screen.blit(self.score_image, self.score_rect) 
		self.screen.blit(self.high_score_image, self.high_score_rect)
		self.screen.blit(self.level_image, self.level_rect)
		self.ships.draw(self.screen)
		

	def prep_high_score(self):
		"""turn the high score into rended image"""
		high_score = round(self.stats.high_score, -1)
		high_score_str = "{:,}".format(high_score)
		self.high_score_image = self.font.render(high_score_str, True, 
			self.text_color, self.settings.bg_color)

		self.high_score_rect = self.high_score_image.get_rect()
		self.high_score_rect.centerx = self.screen_rect.centerx
		self.high_score_rect.top = self.screen_rect.top

	def check_high_score(self):
		"""check for a new high score"""
		if self.stats.score >self.stats.high_score:
			self.stats.high_score = self.stats.score
			self.prep_high_score()

	def prep_level(self):
		"""Turn the level into rended image"""
		level_str = str(self.stats.level)
		self.level_image = self.font.render(level_str, True, self.text_color, self.settings.bg_color)

		#//position level below the score"""
		self.level_rect = self.level_image.get_rect()
		self.level_rect.right = self.score_rect.right
		self.level_rect.top = self.score_rect.bottom +10

	def prep_ships(self):
		"""show the remaining ships"""
		self.ships = Group()
		for ship_num in range(self.stats.ships_left):
			ship = Ship(self.ai_game)
			ship.rect.x = 10+ ship_num * ship.rect.width
			ship.rect.y = 10
			self.ships.add(ship)
