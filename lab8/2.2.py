# Imports
import pygame, sys
from pygame.locals import *
import random, time

# Initializing 
pygame.init()

# Setting up FPS 
FPS = 10  # Slower FPS for snake movement
FramePerSec = pygame.time.Clock()

# Creating colors
BLUE  = (0, 0, 255)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
DARK_GREEN = (0, 100, 0)

# Other Variables for use in the program
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 400  # Square screen for snake game
BLOCK_SIZE = 20
SPEED = 5
SCORE = 0

# Setting up Fonts
font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, WHITE)

# Create a screen 
DISPLAYSURF = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
DISPLAYSURF.fill(BLACK)
pygame.display.set_caption("Snake Game")

class Snake(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.size = 1
        self.elements = [[SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2]]  # Start in the middle
        self.direction = "RIGHT"
        self.image = pygame.Surface((BLOCK_SIZE, BLOCK_SIZE))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.topleft = self.elements[0]
        
    def update(self):
        # Move the snake
        head = self.elements[0].copy()
        
        if self.direction == "RIGHT":
            head[0] += BLOCK_SIZE
        elif self.direction == "LEFT":
            head[0] -= BLOCK_SIZE
        elif self.direction == "UP":
            head[1] -= BLOCK_SIZE
        elif self.direction == "DOWN":
            head[1] += BLOCK_SIZE
            
        # Check for wall collision
        if (head[0] >= SCREEN_WIDTH or head[0] < 0 or 
            head[1] >= SCREEN_HEIGHT or head[1] < 0):
            return True  # Game over
            
        # Check for self collision
        if head in self.elements:
            return True  # Game over
            
        self.elements.insert(0, head)
        
        # Remove tail if we haven't eaten food
        if len(self.elements) > self.size:
            self.elements.pop()
            
        self.rect.topleft = self.elements[0]
        return False
        
    def grow(self):
        self.size += 1
        
    def draw(self, surface):
        for segment in self.elements:
            pygame.draw.rect(surface, GREEN, (segment[0], segment[1], BLOCK_SIZE, BLOCK_SIZE))
            pygame.draw.rect(surface, DARK_GREEN, (segment[0], segment[1], BLOCK_SIZE, BLOCK_SIZE), 1)

class Food(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((BLOCK_SIZE, BLOCK_SIZE))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.randomize_position()
    
    def randomize_position(self):
        self.rect.x = random.randint(0, (SCREEN_WIDTH - BLOCK_SIZE) // BLOCK_SIZE) * BLOCK_SIZE
        self.rect.y = random.randint(0, (SCREEN_HEIGHT - BLOCK_SIZE) // BLOCK_SIZE) * BLOCK_SIZE

# Setting up Sprites        
snake = Snake()
food = Food()

# Creating Sprites Groups
all_sprites = pygame.sprite.Group()
all_sprites.add(snake)
all_sprites.add(food)

# Game Loop
while True:
    # Cycles through all events occurring  
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == KEYDOWN:
            if event.key == K_RIGHT and snake.direction != "LEFT":
                snake.direction = "RIGHT"
            elif event.key == K_LEFT and snake.direction != "RIGHT":
                snake.direction = "LEFT"
            elif event.key == K_UP and snake.direction != "DOWN":
                snake.direction = "UP"
            elif event.key == K_DOWN and snake.direction != "UP":
                snake.direction = "DOWN"

    # Fill the screen
    DISPLAYSURF.fill(BLACK)
    
    # Check for collision with food
    if pygame.sprite.collide_rect(snake, food):
        SCORE += 1
        snake.grow()
        food.randomize_position()
        # Make sure food doesn't appear on snake
        while (food.rect.topleft in snake.elements):
            food.randomize_position()
    
    # Update snake position and check for game over
    game_over_flag = snake.update()
    
    if game_over_flag:
        pygame.mixer.Sound('images/crash.wav').play()
        time.sleep(1)
        
        DISPLAYSURF.fill(RED)
        DISPLAYSURF.blit(game_over, (30, 150))
        
        final_score = font_small.render(f"Final Score: {SCORE}", True, WHITE)
        DISPLAYSURF.blit(final_score, (120, 220))
        
        pygame.display.update()
        time.sleep(2)
        pygame.quit()
        sys.exit()
    
    # Draw all elements
    snake.draw(DISPLAYSURF)
    DISPLAYSURF.blit(food.image, food.rect)
    
    # Display score
    score_text = font_small.render(f"Score: {SCORE}", True, WHITE)
    DISPLAYSURF.blit(score_text, (10, 10))
    
    pygame.display.update()
    FramePerSec.tick(FPS)