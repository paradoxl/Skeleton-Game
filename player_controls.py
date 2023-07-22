import random

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
        attack1 = pygame.mixer.Sound("assets/music/slash-21834.mp3")
        pygame.mixer.Sound.play(attack1)

    if keys_pressed[pygame.K_2]:
        player_one.attacking2 = True
        attack2 = pygame.mixer.Sound("assets/music/bow-release-bow-and-arrow-4-101936.mp3")
        pygame.mixer.Sound.play(attack2)

    if keys_pressed[pygame.K_3]:
        player_one.attacking3 = True

        attack3 = pygame.mixer.Sound("assets/music/arrow-wood-impact-146418.mp3")
        pygame.mixer.Sound.play(attack3)


    if not player_one.is_jumping:
        if keys_pressed[pygame.K_SPACE]:
            player_one.is_jumping = True
            musicQue = ["assets/music/jump1.mp3","assets/music/jump2.mp3","assets/music/jump3.mp3","assets/music/jump1.mp3","assets/music/jump4.mp3",
                        "assets/music/jump5.mp3","assets/music/jump6.mp3","assets/music/jump7.mp3","assets/music/jump8.mp3","assets/music/jump9.mp3",
                        "assets/music/jump10.mp3"]
            jumping = pygame.mixer.Sound(random.choice(musicQue))
            pygame.mixer.Sound.play(jumping)
    if player_one.is_jumping:
        player_one.moving_left = False
        player_one.moving_right = False
        F = (1 / 2) * mass * (velocity ** 2)
        player_one.y -= F
        velocity -= 1
        if velocity < 0:
            mass = - 1
        if velocity == -9:
            player_one.is_jumping = False
            velocity = 8
            mass = 1
