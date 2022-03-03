import pygame
from pygame.locals import *
#https://opengameart.org/content/scrolling-loopable-parallax-backgrounds
#https://opengameart.org/content/bg-layers
#https://hello-tazzina.itch.io/green-woods




pygame.init()

root = pygame.display.set_mode((0,0),pygame.FULLSCREEN)
pygame.display.set_caption("Extreme Crazy Fishing")
running = True

mountain_bg = pygame.image.load("Assets/Mountains.png")
mountain_bg = pygame.transform.scale(mountain_bg,(800,440))
forest_bg = pygame.image.load("Assets/Forest.png")
forest_bg = pygame.transform.scale(forest_bg,(800,440))
sky_bg = pygame.image.load("Assets/SkyBG.png")
sky_bg = pygame.transform.scale(sky_bg,(800,340))
forest_fg = pygame.image.load("Assets/pine1.png")
forest_fg = pygame.transform.scale(forest_fg,(800,200))
forest_fg2 = pygame.image.load("Assets/pine2.png")
forest_fg2 = pygame.transform.scale(forest_fg2,(800,200))
boat = [pygame.transform.scale(pygame.image.load("Assets/Boat1.png"), (440, 180)), pygame.transform.scale(pygame.image.load("Assets/Boat1.png"), (440, 180)), pygame.transform.scale(pygame.image.load("Assets/Boat1.png"), (440, 180)), pygame.transform.scale(pygame.image.load("Assets/Boat2.png"), (440, 180)), pygame.transform.scale(pygame.image.load("Assets/Boat2.png"), (440, 180)), pygame.transform.scale(pygame.image.load("Assets/Boat2.png"), (440, 180)), pygame.transform.scale(pygame.image.load("Assets/Boat3.png"), (440, 180)), pygame.transform.scale(pygame.image.load("Assets/Boat3.png"), (440, 180)), pygame.transform.scale(pygame.image.load("Assets/Boat3.png"), (440, 180)),pygame.transform.scale(pygame.image.load("Assets/Boat4.png"), (440, 180)), pygame.transform.scale(pygame.image.load("Assets/Boat4.png"), (440, 180)), pygame.transform.scale(pygame.image.load("Assets/Boat4.png"), (440, 180))]
nature_fg = [pygame.transform.scale(pygame.image.load("Assets/secondground1.png"), (80, 80)), pygame.transform.scale(pygame.image.load("Assets/secondground1.png"), (80, 80)), pygame.transform.scale(pygame.image.load("Assets/secondground1.png"), (80, 80)), pygame.transform.scale(pygame.image.load("Assets/secondground2.png"), (80, 80)), pygame.transform.scale(pygame.image.load("Assets/secondground2.png"), (80, 80)), pygame.transform.scale(pygame.image.load("Assets/secondground2.png"), (80, 80)), pygame.transform.scale(pygame.image.load("Assets/secondground3.png"), (80, 80)), pygame.transform.scale(pygame.image.load("Assets/secondground3.png"), (80, 80)), pygame.transform.scale(pygame.image.load("Assets/secondground3.png"), (80, 80))]

width = 800
i = 0
j = 0
k = 0
count = 0
nat_count = 0

while running:
	root.fill((99, 155, 255))
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running=False
			pygame.quit()


	root.blit(sky_bg, (i, 0))
	root.blit(sky_bg, (width + i, 0))
	root.blit(sky_bg, (width * 2 + i, 0))
	root.blit(sky_bg, (width * 3 + i, 0))
	root.blit(sky_bg, (width * 4 + i, 0))
	root.blit(mountain_bg, (i, -100))
	root.blit(mountain_bg, (width + i, -100))
	root.blit(mountain_bg, (width * 2 + i, -100))
	root.blit(mountain_bg, (width * 3 + i, -100))
	root.blit(mountain_bg, (width * 4 + i, -100))
	if i < -width:
		i = 0
	if j < -width:
		j = 0
	if k < -width:
		k = 0
	i -= 1
	j -= 10
	k -= 3
	root.blit(forest_bg, (j, -90))
	root.blit(forest_bg, (width + j, -90))
	root.blit(forest_bg, (width * 2 + j, -90))
	root.blit(forest_bg, (width * 3 + j, -90))
	root.blit(forest_bg, (width * 4 + j, -90))
	root.blit(forest_fg2, (k, 200))
	root.blit(forest_fg2, (width + k, 200))
	root.blit(forest_fg2, (width * 2 + k, 200))
	root.blit(forest_fg2, (width * 3 + k, 200))
	root.blit(forest_fg2, (width * 4 + k, 200))
	root.blit(forest_fg, (j, 280))
	root.blit(forest_fg, (width + j, 280))
	root.blit(forest_fg, (width * 2 + j, 280))
	root.blit(forest_fg, (width * 3 + j, 280))
	root.blit(forest_fg, (width * 4 + j, 280))
	root.blit(nature_fg[nat_count], (j, 437))
	root.blit(nature_fg[nat_count], (width / 10 + j, 437))
	root.blit(nature_fg[nat_count], (width / 10 * 2 + j, 437))
	root.blit(nature_fg[nat_count], (width / 10 * 3 + j, 437))
	root.blit(nature_fg[nat_count], (width / 10 * 4 + j, 437))
	root.blit(nature_fg[nat_count], (width / 10 * 5 + j, 437))
	root.blit(nature_fg[nat_count], (width / 10 * 6 + j, 437))
	root.blit(nature_fg[nat_count], (width / 10 * 7 + j, 437))
	root.blit(nature_fg[nat_count], (width / 10 * 8 + j, 437))
	root.blit(nature_fg[nat_count], (width / 10 * 9 + j, 437))
	root.blit(nature_fg[nat_count], (width / 10 * 10 + j, 437))
	root.blit(nature_fg[nat_count], (width / 10 * 11 + j, 437))
	root.blit(nature_fg[nat_count], (width / 10 * 12 + j, 437))
	root.blit(nature_fg[nat_count], (width / 10 * 13 + j, 437))
	root.blit(nature_fg[nat_count], (width / 10 * 14 + j, 437))
	root.blit(nature_fg[nat_count], (width / 10 * 15 + j, 437))
	root.blit(nature_fg[nat_count], (width / 10 * 16 + j, 437))
	root.blit(nature_fg[nat_count], (width / 10 * 17 + j, 437))
	root.blit(nature_fg[nat_count], (width / 10 * 18 + j, 437))
	root.blit(nature_fg[nat_count], (width / 10 * 19 + j, 437))
	root.blit(nature_fg[nat_count], (width / 10 * 20 + j, 437))
	root.blit(nature_fg[nat_count], (width / 10 * 21 + j, 437))
	root.blit(nature_fg[nat_count], (width / 10 * 22 + j, 437))
	root.blit(nature_fg[nat_count], (width / 10 * 23 + j, 437))
	root.blit(nature_fg[nat_count], (width / 10 * 24 + j, 437))
	root.blit(nature_fg[nat_count], (width / 10 * 25 + j, 437))
	root.blit(nature_fg[nat_count], (width / 10 * 26 + j, 437))
	root.blit(nature_fg[nat_count], (width / 10 * 27 + j, 437))
	root.blit(nature_fg[nat_count], (width / 10 * 28 + j, 437))
	root.blit(nature_fg[nat_count], (width / 10 * 29 + j, 437))
	root.blit(nature_fg[nat_count], (width / 10 * 30 + j, 437))
	root.blit(nature_fg[nat_count], (width / 10 * 31 + j, 437))
	root.blit(nature_fg[nat_count], (width / 10 * 32 + j, 437))
	root.blit(nature_fg[nat_count], (width / 10 * 33 + j, 437))
	root.blit(nature_fg[nat_count], (width / 10 * 34 + j, 437))
	root.blit(nature_fg[nat_count], (width / 10 * 35 + j, 437))
	root.blit(nature_fg[nat_count], (width / 10 * 36 + j, 437))
	root.blit(nature_fg[nat_count], (width / 10 * 37 + j, 437))
	if count > 11:
		count = 0
	if nat_count > 7:
		nat_count = 0
	nat_count += 1
	root.blit(boat[count], (150, 600))
	count += 1

	pygame.display.update()




