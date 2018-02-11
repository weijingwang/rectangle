import pygame
pygame.mixer.pre_init()
pygame.init()

screen = pygame.display.set_mode((800,600))

green = (0,255,0)
dgreen = (0,127,0)

draw = pygame.draw

oof = pygame.mixer.Sound("hit1.ogg")

pygame.mixer.music.load("oceanman.mp3")
pygame.mixer.music.play(-1)

def optionsMenu():
	done = False
	count = 4

	volume = 1

	while not done:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				done = True
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_RIGHT:
					count = count +1 
					oof.play()
					print count
					if count == 5:
						count = 4
						oof.play()
						print count
				if event.key == pygame.K_LEFT:
					count = count -1
					oof.play()
					print count
					if count == -1:
						count = 0
						oof.play()
						print count

			draw.rect(screen, dgreen, pygame.Rect(0,0,100,100))#0
			draw.rect(screen, dgreen, pygame.Rect(101,0,100,100))#1
			draw.rect(screen, dgreen, pygame.Rect(202,0,100,100))#2
			draw.rect(screen, dgreen, pygame.Rect(303,0,100,100))#3
			draw.rect(screen, dgreen, pygame.Rect(404,0,100,100))#4

			if count == 0:
				draw.rect(screen, green, pygame.Rect(0,0,100,100))#0
				volume = 0
			elif count == 1:
				draw.rect(screen, green, pygame.Rect(101,0,100,100))#1
				volume = 0.25
			elif count ==2:
				draw.rect(screen, green, pygame.Rect(202,0,100,100))#2
				volume = 0.5
			elif count ==3:
				draw.rect(screen, green, pygame.Rect(303,0,100,100))#3
				volume = 0.75
			elif count == 4:
				draw.rect(screen, green, pygame.Rect(404,0,100,100))#4
				volume = 1

			pygame.mixer.music.set_volume(volume)
			oof.set_volume(volume)
		pygame.display.update()

optionsMenu()
