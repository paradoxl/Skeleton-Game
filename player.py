import pygame.display

import animation_lists


class Player():
    def __init__(self, player_height, player_width, health, velocity, x,y,
                 moving_right, moving_left,idle,attacking,attacking2,attacking3,direction_facing,is_jumping):
        self.player_height = player_height
        self.player_width = player_width
        self.health = health
        self.velocity = velocity
        self.x = x
        self.y = y
        self.moving_right = moving_right
        self.moving_left = moving_left
        self.idle = idle
        self.attacking = attacking
        self.attacking2 = attacking2
        self.attacking3 = attacking3
        self.direction_facing = direction_facing
        self.is_jumping = is_jumping




#notes on player stats
# height = 400
# width = 200
# health = 100
# velocity = 10
# x = 100
# y = 300
#moving vars are false intitally
