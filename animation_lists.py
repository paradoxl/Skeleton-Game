import pygame
import spritesheets


playerWidth = 200
playerHeight =400


idlePlayer = [pygame.transform.scale(pygame.image.load("assets/Elementals_Leaf_ranger_Free_v1.0/animations/PNG/idle/idle_1.png"),(playerHeight,playerWidth)), pygame.transform.scale(pygame.image.load("assets/Elementals_Leaf_ranger_Free_v1.0/animations/PNG/idle/idle_2.png"),(playerHeight,playerWidth)),
              pygame.transform.scale(pygame.image.load("assets/Elementals_Leaf_ranger_Free_v1.0/animations/PNG/idle/idle_3.png"),(playerHeight,playerWidth)),pygame.transform.scale(pygame.image.load("assets/Elementals_Leaf_ranger_Free_v1.0/animations/PNG/idle/idle_4.png"),(playerHeight,playerWidth)),
              pygame.transform.scale(pygame.image.load("assets/Elementals_Leaf_ranger_Free_v1.0/animations/PNG/idle/idle_5.png"),(playerHeight,playerWidth)),pygame.transform.scale(pygame.image.load("assets/Elementals_Leaf_ranger_Free_v1.0/animations/PNG/idle/idle_6.png"),(playerHeight,playerWidth)),
              pygame.transform.scale(pygame.image.load("assets/Elementals_Leaf_ranger_Free_v1.0/animations/PNG/idle/idle_7.png"),(playerHeight,playerWidth)),pygame.transform.scale(pygame.image.load("assets/Elementals_Leaf_ranger_Free_v1.0/animations/PNG/idle/idle_8.png"),(playerHeight,playerWidth)),
              pygame.transform.scale(pygame.image.load("assets/Elementals_Leaf_ranger_Free_v1.0/animations/PNG/idle/idle_9.png"),(playerHeight,playerWidth)),pygame.transform.scale(pygame.image.load("assets/Elementals_Leaf_ranger_Free_v1.0/animations/PNG/idle/idle_10.png"),(playerHeight,playerWidth))
              ,pygame.transform.scale(pygame.image.load("assets/Elementals_Leaf_ranger_Free_v1.0/animations/PNG/idle/idle_11.png"),(playerHeight,playerWidth)),pygame.transform.scale(pygame.image.load("assets/Elementals_Leaf_ranger_Free_v1.0/animations/PNG/idle/idle_12.png"),(playerHeight,playerWidth))]

playerRunningRight = [pygame.transform.scale(pygame.image.load("assets/Elementals_Leaf_ranger_Free_v1.0/animations/PNG/run/run_1.png"),(playerHeight,playerWidth)),pygame.transform.scale(pygame.image.load("assets/Elementals_Leaf_ranger_Free_v1.0/animations/PNG/run/run_2.png"),(playerHeight,playerWidth)),
                      pygame.transform.scale(pygame.image.load("assets/Elementals_Leaf_ranger_Free_v1.0/animations/PNG/run/run_3.png"),(playerHeight,playerWidth)),pygame.transform.scale(pygame.image.load("assets/Elementals_Leaf_ranger_Free_v1.0/animations/PNG/run/run_4.png"),(playerHeight,playerWidth)),
                      pygame.transform.scale(pygame.image.load("assets/Elementals_Leaf_ranger_Free_v1.0/animations/PNG/run/run_5.png"),(playerHeight,playerWidth)),pygame.transform.scale(pygame.image.load("assets/Elementals_Leaf_ranger_Free_v1.0/animations/PNG/run/run_6.png"),(playerHeight,playerWidth)),
                      pygame.transform.scale(pygame.image.load("assets/Elementals_Leaf_ranger_Free_v1.0/animations/PNG/run/run_7.png"),(playerHeight,playerWidth)),pygame.transform.scale(pygame.image.load("assets/Elementals_Leaf_ranger_Free_v1.0/animations/PNG/run/run_8.png"),(playerHeight,playerWidth)),
                      pygame.transform.scale(pygame.image.load("assets/Elementals_Leaf_ranger_Free_v1.0/animations/PNG/run/run_9.png"),(playerHeight,playerWidth)),pygame.transform.scale(pygame.image.load("assets/Elementals_Leaf_ranger_Free_v1.0/animations/PNG/run/run_10.png"),(playerHeight,playerWidth))]

player_arrow_attack = [pygame.transform.scale(pygame.image.load("assets/Elementals_Leaf_ranger_Free_v1.0/animations/PNG/1_atk/1_atk_1.png"),(playerHeight,playerWidth)),pygame.transform.scale(pygame.image.load("assets/Elementals_Leaf_ranger_Free_v1.0/animations/PNG/1_atk/1_atk_2.png"),(playerHeight,playerWidth)),
                       pygame.transform.scale(pygame.image.load("assets/Elementals_Leaf_ranger_Free_v1.0/animations/PNG/1_atk/1_atk_3.png"),(playerHeight,playerWidth)),pygame.transform.scale(pygame.image.load("assets/Elementals_Leaf_ranger_Free_v1.0/animations/PNG/1_atk/1_atk_4.png"),(playerHeight,playerWidth)),
                       pygame.transform.scale(pygame.image.load("assets/Elementals_Leaf_ranger_Free_v1.0/animations/PNG/1_atk/1_atk_5.png"),(playerHeight,playerWidth)),pygame.transform.scale(pygame.image.load("assets/Elementals_Leaf_ranger_Free_v1.0/animations/PNG/1_atk/1_atk_6.png"),(playerHeight,playerWidth)),
                       pygame.transform.scale(pygame.image.load("assets/Elementals_Leaf_ranger_Free_v1.0/animations/PNG/1_atk/1_atk_7.png"),(playerHeight,playerWidth)),pygame.transform.scale(pygame.image.load("assets/Elementals_Leaf_ranger_Free_v1.0/animations/PNG/1_atk/1_atk_8.png"),(playerHeight,playerWidth)),
                       pygame.transform.scale(pygame.image.load("assets/Elementals_Leaf_ranger_Free_v1.0/animations/PNG/1_atk/1_atk_9.png"),(playerHeight,playerWidth)),pygame.transform.scale(pygame.image.load("assets/Elementals_Leaf_ranger_Free_v1.0/animations/PNG/1_atk/1_atk_10.png"),(playerHeight,playerWidth))]

player_bow_attack = [pygame.transform.scale(pygame.image.load("assets/Elementals_Leaf_ranger_Free_v1.0/animations/PNG/2_atk/2_atk_1.png"),(playerHeight,playerWidth)),pygame.transform.scale(pygame.image.load("assets/Elementals_Leaf_ranger_Free_v1.0/animations/PNG/2_atk/2_atk_2.png"),(playerHeight,playerWidth)),
                  pygame.transform.scale(pygame.image.load("assets/Elementals_Leaf_ranger_Free_v1.0/animations/PNG/2_atk/2_atk_3.png"),(playerHeight,playerWidth)),pygame.transform.scale(pygame.image.load("assets/Elementals_Leaf_ranger_Free_v1.0/animations/PNG/2_atk/2_atk_4.png"),(playerHeight,playerWidth)),
                  pygame.transform.scale(pygame.image.load("assets/Elementals_Leaf_ranger_Free_v1.0/animations/PNG/2_atk/2_atk_5.png"),(playerHeight,playerWidth)),pygame.transform.scale(pygame.image.load("assets/Elementals_Leaf_ranger_Free_v1.0/animations/PNG/2_atk/2_atk_6.png"),(playerHeight,playerWidth)),
                  pygame.transform.scale(pygame.image.load("assets/Elementals_Leaf_ranger_Free_v1.0/animations/PNG/2_atk/2_atk_7.png"),(playerHeight,playerWidth)),pygame.transform.scale(pygame.image.load("assets/Elementals_Leaf_ranger_Free_v1.0/animations/PNG/2_atk/2_atk_8.png"),(playerHeight,playerWidth)),
                  pygame.transform.scale(pygame.image.load("assets/Elementals_Leaf_ranger_Free_v1.0/animations/PNG/2_atk/2_atk_9.png"),(playerHeight,playerWidth)),pygame.transform.scale(pygame.image.load("assets/Elementals_Leaf_ranger_Free_v1.0/animations/PNG/2_atk/2_atk_10.png"),(playerHeight,playerWidth)),
                  pygame.transform.scale(pygame.image.load("assets/Elementals_Leaf_ranger_Free_v1.0/animations/PNG/2_atk/2_atk_11.png"),(playerHeight,playerWidth)),pygame.transform.scale(pygame.image.load("assets/Elementals_Leaf_ranger_Free_v1.0/animations/PNG/2_atk/2_atk_12.png"),(playerHeight,playerWidth)),
                  pygame.transform.scale(pygame.image.load("assets/Elementals_Leaf_ranger_Free_v1.0/animations/PNG/2_atk/2_atk_13.png"),(playerHeight,playerWidth)),pygame.transform.scale(pygame.image.load("assets/Elementals_Leaf_ranger_Free_v1.0/animations/PNG/2_atk/2_atk_14.png"),(playerHeight,playerWidth)),
                  pygame.transform.scale(pygame.image.load("assets/Elementals_Leaf_ranger_Free_v1.0/animations/PNG/2_atk/2_atk_15.png"),(playerHeight,playerWidth))]

player_ultimate_attack = [pygame.transform.scale(pygame.image.load("assets/Elementals_Leaf_ranger_Free_v1.0/animations/PNG/3_atk/3_atk_1.png"),(playerHeight,playerWidth)),pygame.transform.scale(pygame.image.load("assets/Elementals_Leaf_ranger_Free_v1.0/animations/PNG/3_atk/3_atk_2.png"),(playerHeight,playerWidth)),
                          pygame.transform.scale(pygame.image.load("assets/Elementals_Leaf_ranger_Free_v1.0/animations/PNG/3_atk/3_atk_3.png"),(playerHeight,playerWidth)),pygame.transform.scale(pygame.image.load("assets/Elementals_Leaf_ranger_Free_v1.0/animations/PNG/3_atk/3_atk_4.png"),(playerHeight,playerWidth)),
                          pygame.transform.scale(pygame.image.load("assets/Elementals_Leaf_ranger_Free_v1.0/animations/PNG/3_atk/3_atk_5.png"),(playerHeight,playerWidth)),pygame.transform.scale(pygame.image.load("assets/Elementals_Leaf_ranger_Free_v1.0/animations/PNG/3_atk/3_atk_6.png"),(playerHeight,playerWidth)),
                          pygame.transform.scale(pygame.image.load("assets/Elementals_Leaf_ranger_Free_v1.0/animations/PNG/3_atk/3_atk_7.png"),(playerHeight,playerWidth)),pygame.transform.scale(pygame.image.load("assets/Elementals_Leaf_ranger_Free_v1.0/animations/PNG/3_atk/3_atk_8.png"),(playerHeight,playerWidth)),
                          pygame.transform.scale(pygame.image.load("assets/Elementals_Leaf_ranger_Free_v1.0/animations/PNG/3_atk/3_atk_9.png"),(playerHeight,playerWidth)),pygame.transform.scale(pygame.image.load("assets/Elementals_Leaf_ranger_Free_v1.0/animations/PNG/3_atk/3_atk_10.png"),(playerHeight,playerWidth)),
                          pygame.transform.scale(pygame.image.load("assets/Elementals_Leaf_ranger_Free_v1.0/animations/PNG/3_atk/3_atk_11.png"),(playerHeight,playerWidth)),pygame.transform.scale(pygame.image.load("assets/Elementals_Leaf_ranger_Free_v1.0/animations/PNG/3_atk/3_atk_12.png"),(playerHeight,playerWidth))]

player_jump = [pygame.transform.scale(pygame.image.load("assets/Elementals_Leaf_ranger_Free_v1.0/animations/PNG/jump_full/jump_1.png"),(playerHeight,playerWidth)),pygame.transform.scale(pygame.image.load("assets/Elementals_Leaf_ranger_Free_v1.0/animations/PNG/jump_full/jump_2.png"),(playerHeight,playerWidth)),
               pygame.transform.scale(pygame.image.load("assets/Elementals_Leaf_ranger_Free_v1.0/animations/PNG/jump_full/jump_3.png"),(playerHeight,playerWidth)),pygame.transform.scale(pygame.image.load("assets/Elementals_Leaf_ranger_Free_v1.0/animations/PNG/jump_full/jump_4.png"),(playerHeight,playerWidth)),
               pygame.transform.scale(pygame.image.load("assets/Elementals_Leaf_ranger_Free_v1.0/animations/PNG/jump_full/jump_5.png"),(playerHeight,playerWidth)),pygame.transform.scale(pygame.image.load("assets/Elementals_Leaf_ranger_Free_v1.0/animations/PNG/jump_full/jump_6.png"),(playerHeight,playerWidth)),
               pygame.transform.scale(pygame.image.load("assets/Elementals_Leaf_ranger_Free_v1.0/animations/PNG/jump_full/jump_7.png"),(playerHeight,playerWidth)),pygame.transform.scale(pygame.image.load("assets/Elementals_Leaf_ranger_Free_v1.0/animations/PNG/jump_full/jump_8.png"),(playerHeight,playerWidth)),
               pygame.transform.scale(pygame.image.load("assets/Elementals_Leaf_ranger_Free_v1.0/animations/PNG/jump_full/jump_9.png"),(playerHeight,playerWidth)),pygame.transform.scale(pygame.image.load("assets/Elementals_Leaf_ranger_Free_v1.0/animations/PNG/jump_full/jump_10.png"),(playerHeight,playerWidth)),
               pygame.transform.scale(pygame.image.load("assets/Elementals_Leaf_ranger_Free_v1.0/animations/PNG/jump_full/jump_11.png"),(playerHeight,playerWidth)),pygame.transform.scale(pygame.image.load("assets/Elementals_Leaf_ranger_Free_v1.0/animations/PNG/jump_full/jump_12.png"),(playerHeight,playerWidth)),
               pygame.transform.scale(pygame.image.load("assets/Elementals_Leaf_ranger_Free_v1.0/animations/PNG/jump_full/jump_13.png"),(playerHeight,playerWidth)),pygame.transform.scale(pygame.image.load("assets/Elementals_Leaf_ranger_Free_v1.0/animations/PNG/jump_full/jump_14.png"),(playerHeight,playerWidth)),
               pygame.transform.scale(pygame.image.load("assets/Elementals_Leaf_ranger_Free_v1.0/animations/PNG/jump_full/jump_15.png"),(playerHeight,playerWidth)),pygame.transform.scale(pygame.image.load("assets/Elementals_Leaf_ranger_Free_v1.0/animations/PNG/jump_full/jump_16.png"),(playerHeight,playerWidth)),
               pygame.transform.scale(pygame.image.load("assets/Elementals_Leaf_ranger_Free_v1.0/animations/PNG/jump_full/jump_17.png"),(playerHeight,playerWidth)),pygame.transform.scale(pygame.image.load("assets/Elementals_Leaf_ranger_Free_v1.0/animations/PNG/jump_full/jump_18.png"),(playerHeight,playerWidth)),
               pygame.transform.scale(pygame.image.load("assets/Elementals_Leaf_ranger_Free_v1.0/animations/PNG/jump_full/jump_19.png"),(playerHeight,playerWidth)),pygame.transform.scale(pygame.image.load("assets/Elementals_Leaf_ranger_Free_v1.0/animations/PNG/jump_full/jump_20.png"),(playerHeight,playerWidth)),
               pygame.transform.scale(pygame.image.load("assets/Elementals_Leaf_ranger_Free_v1.0/animations/PNG/jump_full/jump_21.png"),(playerHeight,playerWidth)),pygame.transform.scale(pygame.image.load("assets/Elementals_Leaf_ranger_Free_v1.0/animations/PNG/jump_full/jump_22.png"),(playerHeight,playerWidth))]


#######################################
# Enemies                             #
#######################################

Skeleton_Sprite_Sheet_Idle = spritesheets.spritesheet("assets/Skeleton/Sprite Sheets/Skeleton Idle.png")
Skeleton_Sprite_Sheet_Walk = spritesheets.spritesheet("assets/Skeleton/Sprite Sheets/Skeleton Walk.png")
skeleton_enemy = [
        pygame.transform.scale(Skeleton_Sprite_Sheet_Idle.image_at((0, 0, 24, 32), colorkey=(0, 0, 0)), (75, 75)),
        pygame.transform.scale(Skeleton_Sprite_Sheet_Idle.image_at((24, 0, 24, 32), colorkey=(0, 0, 0)), (75, 75)),
        pygame.transform.scale(Skeleton_Sprite_Sheet_Idle.image_at((48, 0, 24, 32), colorkey=(0, 0, 0)), (75, 75)),
        pygame.transform.scale(Skeleton_Sprite_Sheet_Idle.image_at((72, 0, 24, 32), colorkey=(0, 0, 0)), (75, 75)),
        pygame.transform.scale(Skeleton_Sprite_Sheet_Idle.image_at((96, 0, 24, 32), colorkey=(0, 0, 0)), (75, 75)),
        pygame.transform.scale(Skeleton_Sprite_Sheet_Idle.image_at((120, 0, 24, 32), colorkey=(0, 0, 0)), (75, 75)),
        pygame.transform.scale(Skeleton_Sprite_Sheet_Idle.image_at((144, 0, 24, 32), colorkey=(0, 0, 0)), (75, 75)),
        pygame.transform.scale(Skeleton_Sprite_Sheet_Idle.image_at((168, 0, 24, 32), colorkey=(0, 0, 0)), (75, 75)),
        pygame.transform.scale(Skeleton_Sprite_Sheet_Idle.image_at((192, 0, 24, 32), colorkey=(0, 0, 0)), (75, 75)),
        pygame.transform.scale(Skeleton_Sprite_Sheet_Idle.image_at((216, 0, 24, 32), colorkey=(0, 0, 0)), (75, 75)),
        pygame.transform.scale(Skeleton_Sprite_Sheet_Idle.image_at((240, 0, 24, 32), colorkey=(0, 0, 0)), (75, 75))]

skeleton_enemy_walk = [
        pygame.transform.scale(Skeleton_Sprite_Sheet_Walk.image_at((0, 0, 24, 32), colorkey=(0, 0, 0)), (75, 75)),
        pygame.transform.scale(Skeleton_Sprite_Sheet_Walk.image_at((24, 0, 24, 32), colorkey=(0, 0, 0)), (75, 75)),
        pygame.transform.scale(Skeleton_Sprite_Sheet_Walk.image_at((48, 0, 24, 32), colorkey=(0, 0, 0)), (75, 75)),
        pygame.transform.scale(Skeleton_Sprite_Sheet_Walk.image_at((72, 0, 24, 32), colorkey=(0, 0, 0)), (75, 75)),
        pygame.transform.scale(Skeleton_Sprite_Sheet_Walk.image_at((96, 0, 24, 32), colorkey=(0, 0, 0)), (75, 75)),
        pygame.transform.scale(Skeleton_Sprite_Sheet_Walk.image_at((120, 0, 24, 32), colorkey=(0, 0, 0)), (75, 75)),
        pygame.transform.scale(Skeleton_Sprite_Sheet_Walk.image_at((144, 0, 24, 32), colorkey=(0, 0, 0)), (75, 75)),
        pygame.transform.scale(Skeleton_Sprite_Sheet_Walk.image_at((168, 0, 24, 32), colorkey=(0, 0, 0)), (75, 75)),
        pygame.transform.scale(Skeleton_Sprite_Sheet_Walk.image_at((192, 0, 24, 32), colorkey=(0, 0, 0)), (75, 75)),
        pygame.transform.scale(Skeleton_Sprite_Sheet_Walk.image_at((216, 0, 24, 32), colorkey=(0, 0, 0)), (75, 75)),
        pygame.transform.scale(Skeleton_Sprite_Sheet_Walk.image_at((240, 0, 24, 32), colorkey=(0, 0, 0)), (75, 75))]