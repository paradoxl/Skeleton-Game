import pygame
width = 900
height = 600
i = 1
# background = pygame.image.load()
WIN = pygame.display.set_mode((width, height))
playerHeight = 400
playerWidth = 200
# playerIcon = pygame.image.load("assets/Elementals_Leaf_ranger_Free_v1.0/animations/PNG/idle/idle_1.png")
idlePlayer = [pygame.transform.scale(pygame.image.load("assets/Elementals_Leaf_ranger_Free_v1.0/animations/PNG/idle/idle_1.png"),(playerHeight,playerWidth)), pygame.transform.scale(pygame.image.load("assets/Elementals_Leaf_ranger_Free_v1.0/animations/PNG/idle/idle_2.png"),(playerHeight,playerWidth)),
              pygame.transform.scale(pygame.image.load("assets/Elementals_Leaf_ranger_Free_v1.0/animations/PNG/idle/idle_3.png"),(playerHeight,playerWidth)),pygame.transform.scale(pygame.image.load("assets/Elementals_Leaf_ranger_Free_v1.0/animations/PNG/idle/idle_4.png"),(playerHeight,playerWidth)),
              pygame.transform.scale(pygame.image.load("assets/Elementals_Leaf_ranger_Free_v1.0/animations/PNG/idle/idle_5.png"),(playerHeight,playerWidth)),pygame.transform.scale(pygame.image.load("assets/Elementals_Leaf_ranger_Free_v1.0/animations/PNG/idle/idle_6.png"),(playerHeight,playerWidth)),
              pygame.transform.scale(pygame.image.load("assets/Elementals_Leaf_ranger_Free_v1.0/animations/PNG/idle/idle_7.png"),(playerHeight,playerWidth)),pygame.transform.scale(pygame.image.load("assets/Elementals_Leaf_ranger_Free_v1.0/animations/PNG/idle/idle_8.png"),(playerHeight,playerWidth)),
              pygame.transform.scale(pygame.image.load("assets/Elementals_Leaf_ranger_Free_v1.0/animations/PNG/idle/idle_9.png"),(playerHeight,playerWidth)),pygame.transform.scale(pygame.image.load("assets/Elementals_Leaf_ranger_Free_v1.0/animations/PNG/idle/idle_10.png"),(playerHeight,playerWidth))
              ,pygame.transform.scale(pygame.image.load("assets/Elementals_Leaf_ranger_Free_v1.0/animations/PNG/idle/idle_11.png"),(playerHeight,playerWidth)),pygame.transform.scale(pygame.image.load("assets/Elementals_Leaf_ranger_Free_v1.0/animations/PNG/idle/idle_12.png"),(playerHeight,playerWidth))]


# playerIcon = pygame.transform.scale(playerIcon, (playerHeight, playerWidth))
background_image = pygame.transform.scale(pygame.image.load("assets/NightForest/Layers/Image.png"),(width,height))
moving = False


def main():
    player = pygame.Rect(100,300, playerWidth,playerHeight)
    clock = pygame.time.Clock()
    clock.tick(60)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        kp = pygame.key.get_pressed()
        playerMovement(kp,player)
        draw(player)
           
                
            
def draw(player):
    clock = pygame.time.Clock()
    clock.tick(10)
    WIN.blit(background_image,(0,0))
    global i
    global width
    global height
    if i >= 12:
        i = 1
    value = idlePlayer[i]
    WIN.blit(value,(player.x,player.y))
    pygame.display.update()
    i += 1

def playerMovement(kp,player):
    if kp[pygame.K_LEFT]:
        playerMoving = True
        player.x -= 5
    if kp[pygame.K_RIGHT]:
        playerMoving = True
        player.x += 5
    if kp[pygame.K_SPACE]:
        playerJumping = True
        player.y -=1
        

              



main()