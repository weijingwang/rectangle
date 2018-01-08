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
pygame.mixer.music.set_volume(0)
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
        	color = ((125,255,255))
        	x = x +2
        	y = y+2
        	ten = ten+1
        	print "eat cat"
        if pygame.key.get_pressed()[pygame.K_UP]:
        	y = y - 7
        if pygame.key.get_pressed()[pygame.K_DOWN]:
        	y = y +3
        if pygame.key.get_pressed()[pygame.K_LEFT]:
        	x = x - 7
        if pygame.key.get_pressed()[pygame.K_RIGHT]:
        	x =x+3


        screen.fill((0, 0, 0))

     	pygame.draw.rect(screen, color, pygame.Rect(x, y, side, side))

        pygame.display.flip()