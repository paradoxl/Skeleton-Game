import pygame.display

import PlayerAnimationLists


class Player():
    def __init__(self, player_height, player_width, health, velocity, x,y,
                 moving_right, moving_left,idle,attacking,direction_facing):
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
        self.direction_facing = direction_facing
        # False is left True is right



#notes on player stats
# height = 400
# width = 200
# health = 100
# velocity = 10
# x = 100
# y = 300
#moving vars are false intitally
