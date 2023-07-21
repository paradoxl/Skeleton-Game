import pygame


def player_movement(keys_pressed,player_one,player_hitbox):
    if keys_pressed[pygame.K_RIGHT]:
        player_one.x += 10
        player_hitbox.x += 10
        player_one.idle = False
        player_one.moving_right = True
        player_one.moving_left = False
    else:
        player_one.moving_right = False
        player_one.idle = True
    if keys_pressed[pygame.K_LEFT]:
        player_one.idle = False
        player_one.moving_right = False
        player_one.moving_left = True
        player_one.x -= 10
        player_hitbox.x -= 10
    else:
        player_one.moving_left = False
        player_one.idle = True

    if keys_pressed[pygame.K_1]:
        player_one.attacking = True



    # Create jump function.
