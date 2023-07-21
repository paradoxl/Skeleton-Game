import math
import random

import pygame
import animation_lists
import enemy
import player
import player_controls
import spritesheets

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
gravity = 0.6
jump_height = 20
jump_speed = 20
# background information
background_image = pygame.transform.scale(pygame.image.load("assets/NightForest/Layers/Image.png"),(screen_width,screen_height))

# drawing player
idle_counter = 1
moving_right_counter = 1
moving_left_counter = 1
attack_counter = 1
jump_counter = 1



# drawing enemy
enemy_idle = 1
enemy_start_pos_x = 600
enemy_start_pos_y = 425

player_one = player.Player(player_height, player_width, player_health, player_velocity, player_starting_pos_x,
                           player_starting_pos_y, False, False, False,False,True,False)
Skeleton_enemy = enemy.Enemy(player_height,player_width,10,player_velocity,enemy_start_pos_x,enemy_start_pos_y,False,False,False,
                             False,False)

player_hitbox = pygame.Rect(player_one.x, player_one.y, player_one.player_width, player_one.player_height)


def main():
    # variables for scrolling background
    scroll = 0
    counter = 0
    tiles = math.ceil(screen_width / background_image.get_width()) + 1

    clock = pygame.time.Clock()
    clock.tick(60)

    game_running = True
    while game_running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_running = False
        keys_pressed = pygame.key.get_pressed()
        draw_background(counter, scroll, tiles)
        # player_movement(keys_pressed,player_one,player_hitbox)
        player_controls.player_movement(keys_pressed,player_one,player_hitbox)
        draw_player(keys_pressed,player_hitbox,player_one)
        jump_animation(player_one)
        draw_enemy()

        pygame.display.update()


def draw_player(keys_pressed, player_hitbox, player_one):
    global idle_counter
    global moving_right_counter
    global moving_left_counter
    global attack_counter
    global jump_counter

    clock = pygame.time.Clock()
    clock.tick(10)
    # Movement right
    if player_one.moving_right:
        if moving_right_counter >= 10:
            moving_right_counter = 1
        value = animation_lists.playerRunningRight[moving_right_counter]
        window.blit(value,(player_one.x,player_one.y))
        moving_right_counter += 1
        player_one.direction_facing = True
    # Movement left
    elif player_one.moving_left:
        if moving_left_counter >= 10:
            moving_left_counter = 1
        value = pygame.transform.flip(animation_lists.playerRunningRight[moving_left_counter], True, False)
        window.blit(value,(player_one.x,player_one.y))
        moving_left_counter += 1
        player_one.direction_facing = False

    # Melee attack
    elif player_one.attacking:
        if player_one.direction_facing:
            if attack_counter == 9:
                player_one.attacking = False
                attack_counter = 1
            value = animation_lists.player_arrow_attack[attack_counter]
            window.blit(value,(player_one.x,player_one.y))
            attack_counter += 1

        # since we do not want a continuous loop of the character attacking we set to false when the full animation
        # has cycled.

        else:
            if attack_counter == 9:
                player_one.attacking = False
                attack_counter = 1
            value = pygame.transform.flip(animation_lists.player_arrow_attack[attack_counter],True,False)
            window.blit(value, (player_one.x, player_one.y))
            attack_counter += 1

    # jump works properly with higher framerate. Need to refactor this to work seperately of other animations.
<<<<<<< Updated upstream
    elif player_one.is_jumping:
        if jump_counter == 22:
            player_one.is_jumping = False
            jump_counter = 1
        value = animation_lists.player_jump[jump_counter]
        window.blit(value,(player_one.x,player_one.y))
        jump_counter += 1
=======

>>>>>>> Stashed changes

    # Idle
    else:
        if player_one.direction_facing:
            if idle_counter >= 12:
                idle_counter = 1
            value = animation_lists.idlePlayer[idle_counter]
            window.blit(value,(player_one.x,player_one.y))
            idle_counter += 1
        else:
            if idle_counter >= 12:
                idle_counter = 1
            value = pygame.transform.flip(animation_lists.idlePlayer[idle_counter], True, False)
            window.blit(value, (player_one.x, player_one.y))
            idle_counter += 1


def draw_enemy():
    global enemy_idle


    if enemy_idle >= 11:
        enemy_idle = 1
    window.blit(animation_lists.skeleton_enemy[enemy_idle], (600,425))
    enemy_idle +=1


def draw_background(counter,scroll,tiles):
    while (counter < tiles):
        window.blit(background_image, (background_image.get_width() * counter + scroll, 0))
        counter += 1
    if abs(scroll) > background_image.get_width():
        scroll = 0

<<<<<<< Updated upstream

=======
def jump_animation(player_one):
    player_one.id
    global jump_counter
    if player_one.is_jumping:
        if jump_counter == 22:
            player_one.is_jumping = False
            jump_counter = 1
        value = animation_lists.player_jump[jump_counter]
        window.blit(value,(player_one.x,player_one.y))
        jump_counter += 1
>>>>>>> Stashed changes

if __name__ == '__main__':
          main()