import pygame
import time

pygame.init()
screen = pygame.display.set_mode((1440,1080))



micky = pygame.image.load("images/base_micky.jpg")
la = pygame.image.load("images/minute.png")
ra = pygame.image.load("images/second.png")



running = True
while running:

    screen.blit(micky,(0,0))

    current_time = time.localtime()
    min = current_time.tm_min
    sec = current_time.tm_sec

    min_angle = -min * 6
    sec_angle = -sec * 6


    scaled_la = pygame.transform.scale(la, (1440, 1080))
    rotated_la = pygame.transform.rotate(scaled_la, min_angle)
    la_rect = rotated_la.get_rect(center=(1440 // 2, 1080 // 2))
    screen.blit(rotated_la, la_rect)

    scaled_ra = pygame.transform.scale(ra, (53, 1080))  
    rotated_ra = pygame.transform.rotate(scaled_ra, sec_angle)
    ra_rect = rotated_ra.get_rect(center=(1440 // 2, 1080 // 2))
    screen.blit(rotated_ra, ra_rect)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()

    pygame.display.flip()
