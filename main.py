import math
import pygame
import PlayerAnimationLists
import player


# width = 900
# height = 600
# playerMoving = False # Code debt in the making
# WIN = pygame.display.set_mode((width, height))
# playerHeight = 400
# playerWidth = 200
# # playerIcon = pygame.transform.scale(playerIcon, (playerHeight, playerWidth))
# moving = False
#
# #Scrolling background
# scroll = 0
# scrollThreshRight = 600
# scrollThreshLeft = 50
# tiles = math.ceil(width / background_image.get_width()) + 1
# player1 = player.Player(playerHeight, playerWidth, 10, 10, 100, 300, False, False, False)
#
#
# #player movemnet vvariables
# idle_counter = 0
# running_right_counter = 0
#
# def main():
#     print(player1)
#     player_box = pygame.Rect(100,300, playerWidth,playerHeight)
#     clock = pygame.time.Clock()
#     clock.tick(60)
#     running = True
#     while running:
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 running = False
#         kp = pygame.key.get_pressed()
#         playerMovement(kp,player_box)
#         draw(player_box,kp)
#
#
#
# def draw(player,kp):
#     global scroll
#     clock = pygame.time.Clock()
#     clock.tick(10)
#     counter = 0
#     while (counter < tiles):
#         WIN.blit(background_image, (background_image.get_width() * counter + scroll, 0))
#         counter += 1
#     if abs(scroll) > background_image.get_width():
#         scroll = 0
#
#
#     global idle_counter
#     # Makes the player idle animation
#     if not moving:
#         if idle_counter >= 12:
#             idle_counter = 1
#         value = PlayerAnimationLists.idlePlayer[idle_counter]
#         WIN.blit(value,(player.x,player.y))
#         pygame.display.update()
#         idle_counter += 1
#
#     global running_right_counter
#     if moving:
#         if running_right_counter > 9:
#             running_right_counter = 0
#         if running_right_counter >= 9:
#             running_right_counter = 1
#             running = PlayerAnimationLists.playerRunningRight[running_right_counter]
#             WIN.blit(running,(player.x,player.y))
#             pygame.display.update()
#             running_right_counter += 1
#
# def playerMovement(kp,player):
#     global scroll
#     global playerMoving
#
#     if kp[pygame.K_LEFT] and player.x - 5 > 0:
#         player.x -= 10
#         if player.x < scrollThreshLeft:
#             scroll += 30
#             player.x += 10
#
#     if kp[pygame.K_RIGHT]:
#         player1.moving_left = False
#         player1.moving_right = True
#         player1.idle = False
#         player.x += 10
#         if player.x > scrollThreshRight:
#             scroll -= 30
#             player.x -= 10
#         # playerMoving = True
#
#     if kp[pygame.K_SPACE]:
#         playerJumping = True
#         player.y -=1
#
#
#
#
#
#
# main()











#####################################################################3
#Refactor this garbage fire
#####################
# issues
# game does not exit immediately

####################


# pygame stuffs
screen_width = 900
screen_height = 600
window = pygame.display.set_mode((screen_width, screen_height))
pygame.init()
# player information
player_height = 400
player_width = 200
player_health = 100
player_velocity = 10
player_starting_pos_x = 100
player_starting_pos_y = 300
player_moving_left = False
player_moving_right = False
player_idle = False

# background information
background_image = pygame.transform.scale(pygame.image.load("assets/NightForest/Layers/Image.png"),(screen_width,                                                                                                    screen_height))

# drawing player
idle_counter = 1
moving_right_counter = 1




def main():
    # variables for scrolling background
    scroll = 0
    counter = 0
    tiles = math.ceil(screen_width / background_image.get_width()) + 1
    # FPS
    clock = pygame.time.Clock()
    clock.tick(60)

    game_running = True
    while game_running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_running = False
                pygame.quit()
            keys_pressed = pygame.key.get_pressed()
            player_one = player.Player(player_height,player_width,player_health,player_velocity,player_starting_pos_x,
                                       player_starting_pos_y,player_moving_right,player_moving_left,player_idle)
            player_hitbox = pygame.Rect(player_one.x,player_one.y,player_one.player_width,player_one.player_height)

            # player_one.idle = True
            player_one.moving_right = True
            draw_background(counter, scroll, tiles)
            draw_player(keys_pressed,player_hitbox,player_one)
            player_movement(keys_pressed,player_one)



def draw_player(keys_pressed, player_hitbox, player_one):
    global idle_counter
    global moving_right_counter

    clock = pygame.time.Clock()
    clock.tick(10)

    if player_one.moving_right == True:
        if moving_right_counter >= 10:
            moving_right_counter = 1
        value = PlayerAnimationLists.playerRunningRight[moving_right_counter]
        window.blit(value,(player_one.x,player_one.y))
        moving_right_counter += 1



    if player_one.idle == True:
        if idle_counter >= 12:
            idle_counter = 1
        value = PlayerAnimationLists.idlePlayer[idle_counter]
        window.blit(value,(player_one.x,player_one.y))
        idle_counter += 1


    pygame.display.update()
def draw_background(counter,scroll,tiles):
    while (counter < tiles):
        window.blit(background_image, (background_image.get_width() * counter + scroll, 0))
        counter += 1
    if abs(scroll) > background_image.get_width():
        scroll = 0
    # pygame.display.update()
def player_movement(keys_pressed,player_one,):
    if keys_pressed[pygame.K_RIGHT]:
        player_one.x += 10
        print(player_one.x)
        


main()