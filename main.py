# J. Matthew Myers
# Distributed under the terms of the GNU GPLv3.
# 12/19/2021

# 2D Game Elements

import pygame
from pygame import *
from pygame.sprite import Group

import Character
from Character import *

import game_functions as gf
from game_functions import *

def main():
	# Initialize pygame instance
	pygame.init()
	# Setup screen with dimensions, caption, background
	screen = pygame.display.set_mode((600, 600))
	pygame.display.set_caption("Definitely Spider-Man PS5")
	bg_color = (255, 255, 255)

	# Create instance of Character class
	peter = Character("Peter Parker", screen, "Assets/peter.png", 0.65, 'a')
	
	# Create list of characters in program
	characters = []
	characters.append(peter)

	# Main event loop
	while True:
		# For each character, check events and update the character and the screen
		for character in characters:
			gf.check_events(screen, character)
			character.update()
			gf.update_screen(screen, character)
main()
