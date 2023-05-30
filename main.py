import pygame
import math
width = 900
height = 600
# background = pygame.image.load()
WIN = pygame.display.set_mode((width, height))
playerIcon = pygame.image.load("assets/Elementals_Leaf_ranger_Free_v1.0/animations/PNG/idle/idle_1.png")
idlePlayer = [pygame.image.load("assets/Elementals_Leaf_ranger_Free_v1.0/animations/PNG/idle/idle_1.png"), pygame.image.load("assets/Elementals_Leaf_ranger_Free_v1.0/animations/PNG/idle/idle_2.png"),
              pygame.image.load("assets/Elementals_Leaf_ranger_Free_v1.0/animations/PNG/idle/idle_3.png"),pygame.image.load("assets/Elementals_Leaf_ranger_Free_v1.0/animations/PNG/idle/idle_4.png"),
              pygame.image.load("assets/Elementals_Leaf_ranger_Free_v1.0/animations/PNG/idle/idle_5.png"),pygame.image.load("assets/Elementals_Leaf_ranger_Free_v1.0/animations/PNG/idle/idle_6.png"),
              pygame.image.load("assets/Elementals_Leaf_ranger_Free_v1.0/animations/PNG/idle/idle_7.png"),pygame.image.load("assets/Elementals_Leaf_ranger_Free_v1.0/animations/PNG/idle/idle_8.png"),
              pygame.image.load("assets/Elementals_Leaf_ranger_Free_v1.0/animations/PNG/idle/idle_9.png"),pygame.image.load("assets/Elementals_Leaf_ranger_Free_v1.0/animations/PNG/idle/idle_10.png")
              ,pygame.image.load("assets/Elementals_Leaf_ranger_Free_v1.0/animations/PNG/idle/idle_11.png"),pygame.image.load("assets/Elementals_Leaf_ranger_Free_v1.0/animations/PNG/idle/idle_12.png")]
playerHeight = 400
playerWidth = 200
playerIcon = pygame.transform.scale(playerIcon, (playerHeight, playerWidth))
background_image = pygame.transform.scale(pygame.image.load("assets/NightForest/Layers/Image.png"),(width,height))
moving = False


def main():
    player = pygame.Rect(100,300, playerWidth,playerHeight)
    clock = pygame.time.Clock
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        kp = pygame.key.get_pressed()
        playerMovement(kp,player)
        draw(player)
           
                
            
def draw(player):
    WIN.blit(background_image,(0,0))
    # WIN.blit(playerIcon,(player.x,player.y))
    for i in idlePlayer:
        WIN.blit(i,(player.x, player.y))
    pygame.display.update()

def playerMovement(kp,player):
    if kp[pygame.K_LEFT]:
        player.x -= 1


    if kp[pygame.K_RIGHT]:
        player.x += 1
              



main()