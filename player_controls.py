import pygame

mass = 1
velocity = 8

def player_movement(keys_pressed, player_one, player_hitbox):
    # physics for jumping
    global mass
    global velocity

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

    if not player_one.is_jumping:
        if keys_pressed[pygame.K_SPACE]:
            player_one.is_jumping = True
    if player_one.is_jumping:
        player_one.moving_left = False
        player_one.moving_right = False
        print("velocity", velocity)
        F = (1 / 2) * mass * (velocity ** 2)
        player_one.y -= F
        velocity -= 1
        if velocity < 0:
            mass = - 1
        if velocity == -9:
            print("here",velocity)
            player_one.is_jumping = False
            velocity = 8
            mass = 1
