# Character class
import pygame

class Character():
	def __init__(self, name, screen, imgPath, speed_factor, control_scheme):
		# Initialize character name, screen, and settings
		self.name = name
		self.screen = screen
		self.imgPath = imgPath
		self.speed_factor = speed_factor
		self.control_scheme = control_scheme

		# Load image and position it
		self.image = pygame.image.load(self.imgPath)
		self.rect = self.image.get_rect()
		self.centerx = float(self.rect.centerx)
		self.centery = float(self.rect.centery)
		self.screen_rect = self.screen.get_rect()
		self.rect.centerx = self.screen_rect.centerx
		self.rect.centery = self.screen_rect.centery


		# Initialize movement flags
		self.moving_right = False
		self.moving_left = False
		self.moving_up = False
		self.moving_down = False

	# update
	# Updates the character based on movement flags
	def update(self):
		# Update the character's position based on the movement flag
		if self.moving_right and self.rect.right < self.screen_rect.right:
			self.centerx += self.speed_factor
			
		elif self.moving_left and self.rect.left > self.screen_rect.left:
			self.centerx -= self.speed_factor

		elif self.moving_up and self.rect.top > self.screen_rect.top:
			self.centery -= self.speed_factor

		elif self.moving_down and self.rect.bottom < self.screen_rect.bottom:
			self.centery += self.speed_factor
			
		#Update rect object from self.center
		self.rect.centerx = self.centerx
		self.rect.centery = self.centery

	# blitme
	# Draw the character
	def blitme(self):
		self.screen.blit(self.image, self.rect)

	#### Insert more methods here ####
	# maybe add health

	# Encapsulation
	def getName(self):
		return self.name
	def setName(self, name):
		self.name = name
