import math
import pygame
width = 900
height = 600
i = 1
WIN = pygame.display.set_mode((width, height))
border = pygame.Rect((width,0,10,height))
BLACK = (0, 0, 0)
playerHeight = 400
playerWidth = 200
playerMoving = False

# playerIcon = pygame.image.load("assets/Elementals_Leaf_ranger_Free_v1.0/animations/PNG/idle/idle_1.png")
idlePlayer = [pygame.transform.scale(pygame.image.load("assets/Elementals_Leaf_ranger_Free_v1.0/animations/PNG/idle/idle_1.png"),(playerHeight,playerWidth)), pygame.transform.scale(pygame.image.load("assets/Elementals_Leaf_ranger_Free_v1.0/animations/PNG/idle/idle_2.png"),(playerHeight,playerWidth)),
              pygame.transform.scale(pygame.image.load("assets/Elementals_Leaf_ranger_Free_v1.0/animations/PNG/idle/idle_3.png"),(playerHeight,playerWidth)),pygame.transform.scale(pygame.image.load("assets/Elementals_Leaf_ranger_Free_v1.0/animations/PNG/idle/idle_4.png"),(playerHeight,playerWidth)),
              pygame.transform.scale(pygame.image.load("assets/Elementals_Leaf_ranger_Free_v1.0/animations/PNG/idle/idle_5.png"),(playerHeight,playerWidth)),pygame.transform.scale(pygame.image.load("assets/Elementals_Leaf_ranger_Free_v1.0/animations/PNG/idle/idle_6.png"),(playerHeight,playerWidth)),
              pygame.transform.scale(pygame.image.load("assets/Elementals_Leaf_ranger_Free_v1.0/animations/PNG/idle/idle_7.png"),(playerHeight,playerWidth)),pygame.transform.scale(pygame.image.load("assets/Elementals_Leaf_ranger_Free_v1.0/animations/PNG/idle/idle_8.png"),(playerHeight,playerWidth)),
              pygame.transform.scale(pygame.image.load("assets/Elementals_Leaf_ranger_Free_v1.0/animations/PNG/idle/idle_9.png"),(playerHeight,playerWidth)),pygame.transform.scale(pygame.image.load("assets/Elementals_Leaf_ranger_Free_v1.0/animations/PNG/idle/idle_10.png"),(playerHeight,playerWidth))
              ,pygame.transform.scale(pygame.image.load("assets/Elementals_Leaf_ranger_Free_v1.0/animations/PNG/idle/idle_11.png"),(playerHeight,playerWidth)),pygame.transform.scale(pygame.image.load("assets/Elementals_Leaf_ranger_Free_v1.0/animations/PNG/idle/idle_12.png"),(playerHeight,playerWidth))]

playerRunningRight = [pygame.transform.scale(pygame.image.load("assets/Elementals_Leaf_ranger_Free_v1.0/animations/PNG/run/run_1.png"),(playerHeight,playerWidth)),pygame.transform.scale(pygame.image.load("assets/Elementals_Leaf_ranger_Free_v1.0/animations/PNG/run/run_2.png"),(playerHeight,playerWidth)),
                      pygame.transform.scale(pygame.image.load("assets/Elementals_Leaf_ranger_Free_v1.0/animations/PNG/run/run_3.png"),(playerHeight,playerWidth)),pygame.transform.scale(pygame.image.load("assets/Elementals_Leaf_ranger_Free_v1.0/animations/PNG/run/run_4.png"),(playerHeight,playerWidth)),
                      pygame.transform.scale(pygame.image.load("assets/Elementals_Leaf_ranger_Free_v1.0/animations/PNG/run/run_5.png"),(playerHeight,playerWidth)),pygame.transform.scale(pygame.image.load("assets/Elementals_Leaf_ranger_Free_v1.0/animations/PNG/run/run_6.png"),(playerHeight,playerWidth)),
                      pygame.transform.scale(pygame.image.load("assets/Elementals_Leaf_ranger_Free_v1.0/animations/PNG/run/run_7.png"),(playerHeight,playerWidth)),pygame.transform.scale(pygame.image.load("assets/Elementals_Leaf_ranger_Free_v1.0/animations/PNG/run/run_8.png"),(playerHeight,playerWidth)),
                      pygame.transform.scale(pygame.image.load("assets/Elementals_Leaf_ranger_Free_v1.0/animations/PNG/run/run_9.png"),(playerHeight,playerWidth)),pygame.transform.scale(pygame.image.load("assets/Elementals_Leaf_ranger_Free_v1.0/animations/PNG/run/run_10.png"),(playerHeight,playerWidth))]

# playerIcon = pygame.transform.scale(playerIcon, (playerHeight, playerWidth))
background_image = pygame.transform.scale(pygame.image.load("assets/NightForest/Layers/Image.png"),(width,height))
moving = False

#Scrolling background
scroll = 0
scrollThreshRight = 600
scrollThreshLeft = 50
tiles = math.ceil(width / background_image.get_width()) + 1

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
    global scroll
    clock = pygame.time.Clock()
    clock.tick(10)
#the background scrolls. need to have it do this only when player goes off edge of screen.
    counter = 0
    while (counter < tiles):
        WIN.blit(background_image, (background_image.get_width() * counter + scroll, 0))
        counter += 1
    # scroll -= 6
    if abs(scroll) > background_image.get_width():
        scroll = 0
    global i
    global width
    global height

    #Makes the player idle animation
    if not playerMoving:
        if i >= 12:
            i = 1
        value = idlePlayer[i]
        WIN.blit(value,(player.x,player.y))
        pygame.display.update()
        i += 1

def playerMovement(kp,player):
    global scroll

    if kp[pygame.K_LEFT] and player.x - 5 > 0:
        player.x -= 10
        if player.x < scrollThreshLeft:
            scroll += 30
            player.x += 10

    if kp[pygame.K_RIGHT]:
        player.x += 10
        if player.x > scrollThreshRight:
            scroll -= 30
            player.x -= 10

    if kp[pygame.K_SPACE]:
        playerJumping = True
        player.y -=1
        

              



main()