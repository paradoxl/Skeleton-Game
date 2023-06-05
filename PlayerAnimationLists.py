import pygame
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
