import pygame, sys
from pygame.locals import *
from components.scenes import *
pygame.init()



WINDOW_WIDTH = 1200
WINDOW_HEIGHT = 800

# No scalling (for now)
# window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), HWSURFACE|DOUBLEBUF|RESIZABLE)
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

Music.initiate_background_music()
pygame.display.set_caption("Moldova Inc")
clock = pygame.time.Clock()

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
		if event.type == pygame.MOUSEWHEEL:
			Map.scroll = event.y
		elif event.type == pygame.KEYDOWN:
			if event.key == pygame.K_ESCAPE:
				if GameState.play:
					GameState.play = False
					GameState.pause = True
				elif GameState.pause:
					GameState.pause = False
					GameState.play = True
				elif GameState.settings:
					GameState.settings = False
					if Settings.back_is == "main_menu":
						GameState.main_menu = True
					elif Settings.back_is == "pause":
						GameState.pause = True
				elif GameState.upgrade_menu:
					GameState.upgrade_menu = False
					GameState.play = True
			elif event.key == pygame.K_SPACE and (GameState.play or GameState.statistic):
				if GameState.play:
					GameState.play = False
					GameState.statistic = True
				elif GameState.statistic:
					GameState.statistic = False
					Statistic._one_plot = True
					Statistic.delete_plot()
					GameState.play = True


		Map.pressed = pygame.mouse.get_pressed()[0]
		Map.motion = event.type == pygame.MOUSEMOTION

		GameState.mouse_button_pressed = pygame.mouse.get_pressed()[0]
		GameState.mouse_position = pygame.MOUSEMOTION


	window.fill((255,255,255))
	GameState.update(window)
	
	pygame.display.update()
	clock.tick(60)