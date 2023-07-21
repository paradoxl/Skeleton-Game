import pygame



def player_movement(keys_pressed,player_one,player_hitbox):
    # physics for jumping
    velocity = 5
    mass = 1

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

    if keys_pressed[pygame.K_SPACE]:
        print("Jumped")
        player_one.is_jumping = True

        F = (1/2)*mass*(velocity**2)
        player_one.y -= F
        velocity = velocity -1

        if velocity < 0:
            mass = -1
        if velocity == -1:
            player_one.is_jumping = False



    #
    # else:
    #     player_one.is_jumping = False
    # Create jump function.
