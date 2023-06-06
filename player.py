import pygame.display

import PlayerAnimationLists


class Player():
    def __init__(self, player_height, player_width, health, velocity, x,y,
                 moving_right, moving_left,idle):
        self.player_height = player_height
        self.player_width = player_width
        self.health = health
        self.velocity = velocity
        self.x = x
        self.y = y
        self.moving_right = moving_right
        self.moving_left = moving_left
        self.idle = idle




    # def drawPlayer(self, kp, moving, moving_right, moving_left, hit_box):
    #     if not moving:
    #         if i >= 12:
    #             i = 1
    #             idle = PlayerAnimationLists.idlePlayer[i]
    #             # How do i blit outside of the main file.
    #             # WIN.blit(idle, (player.x, player.y))
    #             pygame.display.update()
    #             i +=1
    #
    #     if moving:
    #         if moving_right:
    #             if i > 9:
    #                 i = 1
    #                 running_right = PlayerAnimationLists.playerRunningRight[i]
    #                 #WIN.blit(running_right(player.x,player.y))
    #                 pygame.display.update()
    #                 i += 1
    #
