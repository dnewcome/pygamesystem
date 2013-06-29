import pygame, sys
import emu

from pygame.locals import *

# set up pygame
pygame.init()

# set up the window
windowSurface = pygame.display.set_mode((500, 400), 0, 32)
pygame.display.set_caption('Retro!')

# set up the colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# get a pixel array of the surface
pixArray = pygame.PixelArray(windowSurface)
pixArray[480][380] = BLACK
del pixArray

# draw the window onto the screen
pygame.display.update()

def render( windowSurface, mem ):
	# draw a blue circle onto the surface
	windowSurface.fill(WHITE)	
	for i in range (0, 100):
		pygame.draw.circle(windowSurface, BLUE, (i%10*50, i/10*50), mem[i], 0)
	pygame.display.update()
	print 'rendering ' + str(r)

# run the game loop
r = 0
while True:
    r += 1
    emu.tick()
    render( windowSurface, emu.mem )
    pygame.time.wait(10)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
