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

# run the game loop
while True:
	emu.tick()
	render( windowSurface, emu.mem )
	pygame.time.wait(10)
	for event in pygame.event.get():
		if event.type == QUIT:
			print 'quitting'
			pygame.quit()
			sys.exit()
		# joystick is memory mapped to last byte of
		# address space
		elif event.type == KEYUP:
			if( event.key == K_RETURN ):
				emu.mem[99] &= ~( 1 << 0 )
			elif( event.key == K_w ):
				emu.mem[99] &= ~( 1 << 1 )
			elif( event.key == K_a ):
				emu.mem[99] &= ~( 1 << 2 )
			elif( event.key == K_s ):
				emu.mem[99] &= ~( 1 << 3 )
			elif( event.key == K_d ):
				emu.mem[99] &= ~( 1 << 4 )
		elif event.type == KEYDOWN:
			if( event.key == K_RETURN ):
				emu.mem[99] |= ( 1 << 0 )
			elif( event.key == K_w ):
				emu.mem[99] |= ( 1 << 1 )
			elif( event.key == K_a ):
				emu.mem[99] |= ( 1 << 2 )
			elif( event.key == K_s ):
				emu.mem[99] |= ( 1 << 3 )
			elif( event.key == K_d ):
				emu.mem[99] |= ( 1 << 4 )

