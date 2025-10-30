import pygame 

pygame.init()
screen = pygame.display.set_mode((800,400))
screen.fill("White")
running = True

circle_move = 20
circle_x = 25
circle_y = 25
clock=pygame.time.Clock()

while running:

    
    


    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and circle_x > 25:
        circle_x -= circle_move
    elif keys[pygame.K_RIGHT] and circle_x < 800:
        circle_x += circle_move
    elif keys[pygame.K_UP] and circle_y > 25:
        circle_y -= circle_move
    elif keys[pygame.K_DOWN] and circle_y < 400 :
        circle_y = circle_move        

    screen.fill("White")

    pygame.draw.circle(screen , "Red" , (circle_x,circle_y),25)

   


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()

    pygame.display.flip()
    clock.tick(60)

