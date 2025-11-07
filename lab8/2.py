import pygame 
import time 
import random

pygame.init()

screen = pygame.display.set_mode((400 , 400))

speed = 15
fps = pygame.time.Clock()

snake_pos = [100,50]

snake_body = [[100,50],[90,50],[80,50],[70,50]]

fruit_pos = [random.randrange(1,400),random.randrange(1,400)]

fruit_spawn = True

score =0
level =0

dir = 'RIGHT'

running = True 

while running:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                dir = 'UP'
            if event.key == pygame.K_DOWN:
                dir = 'DOWN'
            if event.key == pygame.K_RIGHT:
                dir = 'RIGHT'
            if event.key == pygame.K_LEFT:
                dir = 'LEFT'

    if dir == 'UP':
        snake_pos[1] -= 10
    if dir == 'DOWN':
        snake_pos[1] += 10
    if dir == 'LEFT':
        snake_pos[0] -= 10
    if dir == 'RIGHT':
        snake_pos[0] += 10 

    snake_body.insert(0, list(snake_pos))
    if abs(snake_pos[0] - fruit_pos[0]) < 10 and abs(snake_pos[1] - fruit_pos[1]) < 10:
        score += 10
        fruit_spawn = False
    else:
        snake_body.pop()
        
    if not fruit_spawn:
        fruit_pos = [random.randrange(1,400),random.randrange(1,400)]
        fruit_spawn = True
    
    screen.fill("black")

    
    for pos in snake_body:
        pygame.draw.rect(screen, "green",pygame.Rect(pos[0], pos[1], 10, 10))

    pygame.draw.rect(screen, "White", pygame.Rect(fruit_pos[0], fruit_pos[1], 10, 10))

    if snake_pos[0] < 0 or snake_pos[0] > 790:
        running = False
        pygame.quit()
    if snake_pos[1] < 0 or snake_pos[1] > 790:
        running = False
        pygame.quit()

    for block in snake_body[1:]:
        if snake_pos[0] == block[0] and snake_pos[1] == block[1]:
            running = False
            pygame.quit()

    font= pygame.font.Font(None, 30)
    score_text= font.render("Score:"+str(score), True, "White")
    level_text = font.render("level:"+str(level), True,"White")
    screen.blit(score_text, (10, 0))
    screen.blit(level_text, (330, 0))
    pygame.display.update()
    fps.tick(speed)
