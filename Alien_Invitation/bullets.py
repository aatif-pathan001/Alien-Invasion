import pygame
from pygame.sprite import Sprite
class Bullet(Sprite):
	""" class for a bullet"""
	def __init__(self,ai_game):
		""" making a bullet"""
		super().__init__()
		self.screen = ai_game.screen
		self.settings = ai_game.settings
		self.color = self.settings.bullet_color

		#\\\\ making a bullet
		self.rect = pygame.Rect(
			0, 0, self.settings.bullet_weidth, self.settings.bullet_height )
		self.rect.midtop = ai_game.ship.rect.midtop

		self.y = float(self.rect.y)

	def update(self):
		""" update the postion of the bullet"""
		self.y -= self.settings.bullet_speed
		self.rect.y = self.y

	def draw_bullets(self):
		"""Draw bullets on the screen"""
		#\\\\ .draw.rect() finction fill the space of the rect with the color
		pygame.draw.rect(self.screen, self.color, self.rect)