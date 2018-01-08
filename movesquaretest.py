#pygame is required

import pygame
pygame.mixer.pre_init()

pygame.init()
screen = pygame.display.set_mode((1024, 768))
done = False

color = ((0,255,255))
x=5
y=5
side=123

ten = 10
one = 1
pygame.mixer.music.load("music.mp3")
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play(-1)
while not done:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        done = True

        if ten > one:
        	color = ((0,255,255))

        	x = x +2
        	y = y+2
        	ten = ten-1
        	print "eat dog"
        else:
        	color = ((255,0,0))
        	x = x +2
        	y = y+2
        	ten = ten+1
        	print "eat cat"



     	pygame.draw.rect(screen, color, pygame.Rect(x, y, side, side))

        pygame.display.flip()