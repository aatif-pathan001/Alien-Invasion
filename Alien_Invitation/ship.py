import pygame
from pygame.sprite import Sprite

class Ship(Sprite):
	""" Make a ship """
	def __init__(self,ai_game):
		"""initialize the ship and fix it's position on screen"""
		super().__init__()
		#//// connecting ship screen with game screen 
		#/// get_rect() it make a rectangle starting from top left corner which covers  the whole screen 
		self.screen = ai_game.screen
		# making a  rectangle covering the  display window
		self.screen_rect = ai_game.screen.get_rect()
		# load the image from folder
		self.image = pygame.image.load('images\\shuttle.png')
		# replacing the image with rectangle\\ so it can easly move on screen
		self.rect = self.image.get_rect()
		# placing rectangle on rectagle screen
		self.rect.midbottom = self.screen_rect.midbottom
		# moving flags
		self.moving_right = False
		self.moving_left = False
		self.settings = ai_game.settings
		# take float value of the postion of the ship"""
		self.x = float(self.rect.x)

	def blitme(self):
		""" display the ship at its location """
		
		#//// .blit() is used to draw  thew image on screen and position is specified by  self.rect
		self.screen.blit(self.image,self.rect)

	def update(self):
		""" update the movement of ship"""

		#//// rect.right give the last x coordinate of the rectangle
		if self.moving_right and self.rect.right < self.screen_rect.right :
			self.x += self.settings.ship_speed

		if self.moving_left and self.rect.x > 0 :
			self.x -= self.settings.ship_speed

		self.rect.x = self.x

	def centre_ship(self):
		"""recentren the ship when hitted"""
		self.rect.midbottom = self.screen_rect.midbottom
		self.x = float(self.rect.x)
