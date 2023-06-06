import math
import pygame
import PlayerAnimationLists
import player
width = 900
height = 600
playerMoving = False # Code debt in the making
i = 1
WIN = pygame.display.set_mode((width, height))
playerHeight = 400
playerWidth = 200
# playerIcon = pygame.transform.scale(playerIcon, (playerHeight, playerWidth))
background_image = pygame.transform.scale(pygame.image.load("assets/NightForest/Layers/Image.png"),(width,height))
moving = False

#Scrolling background
scroll = 0
scrollThreshRight = 600
scrollThreshLeft = 50
tiles = math.ceil(width / background_image.get_width()) + 1
player1 = player.Player(playerHeight, playerWidth, 10, 10, 100, 300, False, False, False)


def main():
    print(player1)
    player_box = pygame.Rect(100,300, playerWidth,playerHeight)
    clock = pygame.time.Clock()
    clock.tick(60)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        kp = pygame.key.get_pressed()
        playerMovement(kp,player_box)
        draw(player_box,kp)
           
                
            
def draw(player,kp):
    global scroll
    clock = pygame.time.Clock()
    clock.tick(10)
    counter = 0
    while (counter < tiles):
        WIN.blit(background_image, (background_image.get_width() * counter + scroll, 0))
        counter += 1
    if abs(scroll) > background_image.get_width():
        scroll = 0



    global i
    # global width
    # global height

    #Makes the player idle animation
    if not kp[pygame.K_LEFT] and kp[pygame.K_RIGHT]:
        if i >= 12:
            i = 1
        value = PlayerAnimationLists.idlePlayer[i]
        WIN.blit(value,(player.x,player.y))
        pygame.display.update()
        i += 1

    if kp[pygame.K_RIGHT]:
        if i > 9:
            i = 0
        if i >= 9:
            i = 1
            running = PlayerAnimationLists.playerRunningRight[i]
            WIN.blit(running,(player.x,player.y))
            pygame.display.update()
            i += 1

def playerMovement(kp,player):
    global scroll
    global playerMoving

    if kp[pygame.K_LEFT] and player.x - 5 > 0:
        player.x -= 10
        if player.x < scrollThreshLeft:
            scroll += 30
            player.x += 10

    if kp[pygame.K_RIGHT]:
        player1.moving_left = False
        player1.moving_right = True
        player1.idle = False
        player.x += 10
        if player.x > scrollThreshRight:
            scroll -= 30
            player.x -= 10
        # playerMoving = True

    if kp[pygame.K_SPACE]:
        playerJumping = True
        player.y -=1
        

              



main()