import sys
import pygame
from settings import Settings
from ship import Ship
from bullets import Bullet
from alien import Alien
from time import sleep
from game_stats import GameStats
from button import Button
from score_board import Scoreboard 


class AlienInvitation:
	"""Set the swindow of the game and run the it"""
	def __init__(self):
		"""making the screen of the game"""
		#\\\\\ pygame.init() initiate the background settings to work pygame module properly
		pygame.init()
		
		# \\\\ pygame.display is class having methods set_mode() & set_caption() to set screen size and the title
		# \\\\\ we made a tuple inside the set_mode and bg_colour
		self.settings = Settings()
		self.screen = pygame.display.set_mode(
			(0, 0), pygame.FULLSCREEN)
		self.settings.screen_weidth = self.screen.get_rect().width
		self.settings.screen_height = self.screen.get_rect().height
		self.bg_color=(self.settings.bg_color)
		pygame.display.set_caption('Alien Invitation')
		self.ship = Ship(self)
		
		#\\\\ using .Group function  of sprite we had created a named grouped which can store multiple items
		self.bullets = pygame.sprite.Group()
		self.aliens = pygame.sprite.Group()
		self._create_fleet()

		#\\\\ storing stats of game"""
		self.stats = GameStats(self)
		self.play_button = Button(self, "Play")
		self.sb = Scoreboard(self)

	def _ship_hit(self):
		"""responds when ship is hit """
		if self.stats.ships_left > 0:
			self.stats.ships_left -= 1
			self.sb.prep_ships()
			self.aliens.empty()
			self.bullets.empty()
			self._create_fleet()
			self.ship.centre_ship()
			sleep(0.5)
		else:
			self.stats.game_active = False
			pygame.mouse.set_visible(True)

	def _check_alien_bottom(self):
		"""recente ship when alien hit the bottom """
		screen_rect = self.screen.get_rect()
		for alien in self.aliens.sprites():
			if alien.rect.bottom >= screen_rect.bottom:
				self._ship_hit()
				break

	def _update_aliens(self):
		"""updates the position of aliens in the fleet"""
		self._check_fleet_edges()
		self.aliens.update()
		if pygame.sprite.spritecollideany(self.ship,self.aliens):
			self._ship_hit()
		self._check_alien_bottom()

	def run_game(self):
		"""refresh the screen of the game and provide smooth movement"""
		#\\\\ Loop to get all the events of the user and refreshing the screen according to it
		while True:
			
			#\\\\ pygame.event class collects all the events of the user from keyboard and mouse
			self._check_events()
			if self.stats.game_active:
				self.ship.update()
				self._update_aliens()
				self._update_bullets()
	
			self._update_screen()

	# // method starts with _ cosider as helper method/// used to short other methods of the class  and can be used in other methods
	def _check_events(self):
		""" Response to user input"""
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
			elif event.type == pygame.MOUSEBUTTONDOWN:
				mouse_pos = pygame.mouse.get_pos()
				self._check_play_button(mouse_pos)

			#//// pygame.KEYDOWN get the events from keyboard"""
			#//// .KETDOWN gets event when key is pressed \\ .KEYUP gets event when key  is released
			elif event.type == pygame.KEYDOWN:
				self._check_key_down(event)
				
			elif event.type == pygame.KEYUP:
				self._check_key_up(event)

	def _check_play_button(self, mouse_pos):
		"""start the game when player click play """
		if self.play_button.rect.collidepoint(mouse_pos) and not self.stats.game_active:
			self.stats.reset_stats()
			self.settings.dynamic_settings()
			pygame.mouse.set_visible(False)
			self.stats.game_active = True
			self.sb.prep_score()
			self.sb.prep_level()
			self.sb.prep_ships()
			self.aliens.empty()
			self.bullets.empty()
			self._create_fleet()
			self.ship.centre_ship


	def _check_key_down(self,event):
		"""check which key is pressed"""
		if event.key == pygame.K_RIGHT:
			self.ship.moving_right = True
		elif event.key == pygame.K_LEFT:
			self.ship.moving_left = True
		elif event.key == pygame.K_q:
			sys.exit()
		elif event.key  == pygame.K_SPACE :
			self._fire_bullets()

	def _fire_bullets(self):
		""" create a new bullet and into bullet group"""
		if len(self.bullets) < self.settings.bullet_limit:
			new_bullet = Bullet(self)
			self.bullets.add(new_bullet)

	def _check_key_up(self,event):
		""" check which key is released"""
		if event.key == pygame.K_RIGHT:
			self.ship.moving_right =False
		elif  event.key == pygame.K_LEFT:
			self.ship.moving_left = False

	def _create_fleet(self):
		"""make the fleet of aliens"""
		alien = Alien(self)
		alien_weidth, alien_height = alien.rect.size
		ship_height = self.ship.rect.height
		free_space = self.settings.screen_weidth - 2*alien_weidth
		free_space_y = self.settings.screen_height - (3*alien_height) - ship_height
		number_of_rows = free_space_y//(2*alien_height)
		number_aliens = free_space // (2*alien_weidth)
		for number_of_row in range(number_of_rows):
			for alien_number in range(number_aliens):
				self._alien_creat(alien_number, number_of_row)
		
	def _alien_creat(self,number_aliens,number_of_row):
		alien = Alien(self)
		alien_weidth, alien_height = alien.rect.size
		alien.x = alien_weidth + 2*alien_weidth*number_aliens
		alien.rect.y = alien.rect.height + 2*alien.rect.height* number_of_row
              	
		self.aliens.add(alien)

	def _update_screen(self):
		"""update the screen of game"""
		# .fill() function is used to fill color in window screen
		self.screen.fill(self.bg_color)
		self.ship.blitme()
		for bullet in self.bullets.sprites():
			bullet.draw_bullets()
		self.aliens.draw(self.screen)
		
		if not self.stats.game_active:
			self.play_button.draw_button()
		self.sb.show_score()


		# display.flip() method display new sreen/refreshed screen coresponding to user input
		pygame.display.flip()

	def _update_bullets(self):
		"""update the bullets position and delets the old one"""
		self.bullets.update()
		#\\\\ deleting old bullets
		# making a copy of bullet list so original wont be a        ffected on remoivng bullets
		for bullet in self.bullets.copy():
			if  bullet.rect.bottom <= 0:
				self.bullets.remove(bullet)
		self._check_alien_bullet_collision()
		
	def _check_alien_bullet_collision(self):
		""" kill the alien on collision make new fleet"""
		collision = pygame.sprite.groupcollide(
					self.bullets, self.aliens, True   , True)
		
		if collision :
			for aliens in collision.values():

				self.stats.score += self.settings.alien_points * len(aliens)
				self.sb.prep_score()
				self.sb.check_high_score()
		if not self.aliens:
			self.bullets.empty()
			self._create_fleet()
			self.settings.level_up()

			self.stats.level += 1
			self.sb.prep_level()

	def _check_fleet_edges(self):
		"""check whether the alien hit the two sides or not"""
		for alien in self.aliens.sprites():
			if alien.check_edges():
				self._change_fleet_direction()
				break

	def _change_fleet_direction(self):
		"""changes the direction of the fleet"""
		for alien in self.aliens.sprites():
			alien.rect.y += alien.settings.fleet_drop_speed
		self.settings.fleet_direction *= -1



if __name__ == '__main__':

	#\\ maikg game and running it  
	ai = AlienInvitation()
	ai.run_game()
