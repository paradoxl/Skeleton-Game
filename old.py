# def background():
# #     background_image = pygame.image.load("assets/NightForest/Layers/Image.png")
# #     background_image = pygame.transform.scale(background_image,(width,height))
# #     WIN.blit(background_image,(0,0))

# # def playerMovement(kp, playerbox):
# #     WIN.blit(playerIcon, (playerbox.x, playerbox.y))
# #     if kp[pygame.K_RIGHT]:
# #         playerbox.x += 5
# #     if kp[pygame.K_LEFT]:
# #         playerbox.x -= 5
# #     if kp[pygame.K_UP]:
# #         playerbox.y -= 20
# #         time.sleep(1)
# #         print("jumped")
# #         playerbox.y += 10
# # def refresh():
# #     pygame.display.update()
# # def main():
# #     playerbox = pygame.Rect(600, 200, playerWidth, playerHeight)
# #     clock = pygame.time.Clock()
# #     run = True
# #     while run:
# #         clock.tick(60)

# #         for event in pygame.event.get():
# #             if event.type == pygame.QUIT:
# #                 run = False
# #                 pygame.quit()
# #             background()
# #             kp = pygame.key.get_pressed()
# #             playerMovement(kp, playerbox)
# #             refresh()
