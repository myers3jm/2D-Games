import sys
from sys import *
import pygame
from pygame import *

def check_keydown_events(event, character):
	#Respond to keypresses - A
	if character.control_scheme == 'a':
		if event.key == pygame.K_d:
			character.moving_right = True
		elif event.key == pygame.K_a:
			character.moving_left = True
		elif event.key == pygame.K_w:
			character.moving_up = True
		elif event.key == pygame.K_s:
			character.moving_down = True
		elif event.key == pygame.K_ESCAPE:
			pygame.quit()
			sys.exit()
	# B
	elif character.control_scheme == 'b':
		if event.key == pygame.K_RIGHT:
			character.moving_right = True
		elif event.key == pygame.K_LEFT:
			character.moving_left = True
		elif event.key == pygame.K_UP:
			character.moving_up = True
		elif event.key == pygame.K_DOWN:
			character.moving_down = True
		elif event.key == pygame.K_ESCAPE:
			pygame.quit()
			sys.exit()

def check_keyup_events(event, character):
	#Respond to key releases - A
	if character.control_scheme == 'a':
		if event.key == pygame.K_d:
			character.moving_right = False
		elif event.key == pygame.K_a:
			character.moving_left = False
		elif event.key == pygame.K_w:
			character.moving_up = False
		elif event.key == pygame.K_s:
			character.moving_down = False
	# B
	elif character.control_scheme == 'b':
		if event.key == pygame.K_RIGHT:
			character.moving_right = False
		elif event.key == pygame.K_LEFT:
			character.moving_left = False
		elif event.key == pygame.K_UP:
			character.moving_up = False
		elif event.key == pygame.K_DOWN:
			character.moving_down = False
		
def check_events(screen, character):
	#Respond to keypresses and mouse events
	for event in pygame.event.get():
		#print(event)
		if event.type == pygame.QUIT:
			sys.exit()
		elif event.type == pygame.KEYDOWN:
			check_keydown_events(event, character)
		elif event.type == pygame.KEYUP:
			check_keyup_events(event, character)

def update_screen(screen, character):
	# Update images on the screen and flip to the new screen
	# Redraw the screen during each pass through the loop
	screen.fill((0, 0, 0))

	character.blitme()

	# Make the most recently drawn screen visible
	pygame.display.flip()