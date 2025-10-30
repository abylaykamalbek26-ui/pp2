import pygame
import os

pygame.init()
screen = pygame.display.set_mode((800,600))


music_folder = "music"
allmusic = os.listdir(music_folder)

playlist = []
for song in allmusic:
    playlist.append(os.path.join(music_folder, song))


play = pygame.image.load("images/play.png")
pause= pygame.image.load("images/pause.png")
next = pygame.image.load("images/next.png")
prev = pygame.image.load("images/prev.png")

index = 0
pygame.mixer.music.load(playlist[index]) 
pygame.mixer.music.play(0)

play_mus = True 

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
        if event.type == pygame.KEYDOWN: 
            if event.key == pygame.K_SPACE:
                if play_mus:
                    play_mus = False
                    pygame.mixer.music.pause()
                elif play_mus == False:
                    play_mus = True
                    pygame.mixer.music.unpause()

            if event.key == pygame.K_RIGHT: 
                index += 1 
                pygame.mixer.music.load(playlist[index])
                pygame.mixer.music.play()

            if event.key == pygame.K_LEFT: 
                index -=1
                pygame.mixer.music.load(playlist[index])
                pygame.mixer.music.play()
    
    screen.fill((0,0,0))
    
    font= pygame.font.Font(None, 30)
    text= font.render(os.path.basename(playlist[index]), True, (255, 255, 255))
    
    
    screen.blit(text, (300, 200))
    play = pygame.transform.scale(play, (75, 75))
    pause = pygame.transform.scale(pause, (75, 75))
    
    
    if play_mus:
        screen.blit(pause, (370, 400))
    elif play_mus == False: 
        screen.blit(play, (370, 400))
        
        
    next = pygame.transform.scale(next, (75, 75))
    screen.blit(next, (450, 400))
    
    
    prev = pygame.transform.scale(prev, (75, 75))
    screen.blit(prev, (280, 400))

    pygame.display.flip()