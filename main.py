# 2D Game Elements



import pygame
from pygame import *
from pygame.sprite import Group

import Character
from Character import *

import game_functions as gf
from game_functions import *

def main():
	pygame.init()
	screen = pygame.display.set_mode((600, 600))
	pygame.display.set_caption("Definitely Spider-Man PS5")
	bg_color = (255, 255, 255)

	peter = Character("Peter Parker", screen, "Assets/peter.png", 0.65, 'a')
	characters = []
	characters.append(peter)

	while True:
		for character in characters:
			gf.check_events(screen, character)
			character.update()
			gf.update_screen(screen, character)

	input()

main()