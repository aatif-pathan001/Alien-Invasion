import pygame
from pygame.sprite import Sprite
class Alien(Sprite):
	""" make a single alien  """
	def __init__(self, ai_game):
		"""initialize an alien"""
		super().__init__()
		self.screen = ai_game.screen
		self.image = pygame.image.load("images\\alien_1.png")
		self.rect = self.image.get_rect()
		# placing alien on the screen
		self.x = self.rect.width
		self.y = self.rect.height
		# stores horizontal position
		self.x = float(self.rect.x)
		self.settings = ai_game.settings

	def check_edges(self):
		"""check if allien hit the side wall or not"""
		screen_rect = self.screen.get_rect()
		if  self.rect.right >= screen_rect.right or self.rect.left <= 0:
			return True

	def update(self):
		"""update the positon of an alien"""
		self.x += self.settings.alien_speed * self.settings.fleet_direction
		self.rect.x = self.x