import pygame
pygame.mixer.pre_init()
pygame.init()

done = False
screen = pygame.display.set_mode((800,600))
green = (0,255,0)
red = (255,0,0)

countMax = 2
countMin = 0
count = 0

draw = pygame.draw

oof = pygame.mixer.Sound("hit1.ogg")

pygame.mixer.music.load("oceanman.mp3")
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play(-1)



while not done:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_UP:
				count = count -1
				print count
				oof.play()
				if count == -1:
					count = 2
					print count
					oof.play()
			if event.key == pygame.K_DOWN:
				count = count +1
				print count
				oof.play()
				if count ==3:
					count = 0
					print count
					oof.play()

		draw.rect(screen, red, pygame.Rect(0,0,100,100))#0
		draw.rect(screen, red, pygame.Rect(0,102,100,100))#1
		draw.rect(screen , red, pygame.Rect(0,204,100,100))#2
		if count ==0:
			draw.rect(screen, green, pygame.Rect(0,0,100,100))
		elif count == 1:
			draw.rect(screen, green, pygame.Rect(0,102,100,100))
		elif count == 2:
			draw.rect(screen , green, pygame.Rect(0,204,100,100))
		else:
			print count

	pygame.display.update()