import math

import pygame
from pygame.examples.go_over_there import clock

#window variables
width = 900
height = 500
window = pygame.display.set_mode(width,height)


#background assets
background = pygame.image.load("assets/NightForest/Image without mist.png").convert()
scroll = 0
tiles = math.ceil(width / background.get_width())+1


running = True
clock.tick(60)
while running:
    for event in pygame.event.get():
        if event.type == pygame.quit():
            running = False
            print("Killed program")
            pygame.quit()
    i = 0
    while i < tiles:
        window.blit(background,background.get_width()*i + scroll,0)
        i+=1
        print("here")
        # scroll -= 6
pygame.display.update()