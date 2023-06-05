import pygame.display

import PlayerAnimationLists


class player():
    def __init__(self, player_height, player_width, health, velocity, x,y):
        self.player_height = player_height
        self.player_width = player_width
        self.health = health
        self.velocity = velocity
        self.x = x
        self.y = y

    def drawPlayer(self, kp, moving, moving_right, moving_left, hit_box):
        if not moving:
            if i >= 12:
                i = 1
                idle = PlayerAnimationLists.idlePlayer[i]
                # How do i blit outside of the main file.
                # WIN.blit(idle, (player.x, player.y))
                pygame.display.update()
                i +=1

        if moving:
            if moving_right:
                if i > 9:
                    i = 1
                    running_right = PlayerAnimationLists.playerRunningRight[i]
                    #WIN.blit(running_right(player.x,player.y))
                    pygame.display.update()
                    i += 1

    