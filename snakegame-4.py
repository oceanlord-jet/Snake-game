import pygame
import time
import random


width = 800
height = 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake Game")
score = 0

snake_block = 10
snake_speed = 15
snake_list = []
snake_length = 1
apple_x = round(random.randrange(0, width - snake_block) / 10.0) * 10.0
apple_y = round(random.randrange(0, height - snake_block) / 10.0) * 10.0
block_size = 10
black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
green = (0,255,0)

x1_change = 0
y1_change = 0
x1 = width/2
y1 = height/2
clock = pygame.time.Clock()
game_over = False
game_close = False

def show_splash_screen():
    # initialize pygame
    pygame.init()
    height=600
    width=800
    # create the window
    screen = pygame.display.set_mode((width, height))
    screen.fill((0, 0, 0))
    
    # draw white dots on the screen
    for i in range(100):
        x = random.randint(0, width)
        y = random.randint(0, height)
        pygame.draw.circle(screen, (255, 255, 255), (x, y), 2)
    
    # create and draw the start button
    font = pygame.font.Font(None, 40)
    text = font.render("START", True, (0,0,0))
    text_rect = text.get_rect(center=(width//2, height//2))
    pygame.draw.rect(screen, (255, 255, 255), text_rect.inflate(10, 10))
    screen.blit(text, text_rect)
    
    # update the screen
    pygame.display.update()
    
    # wait for user to press the start button
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN and text_rect.collidepoint(event.pos):
                return

# call the function to show the splash screen
show_splash_screen()

pygame.init()
# Start the game loop
while not game_over:
    while game_close == True:
        message = "Game Over"
        score(snake_length-1)
        screen.fill(black)
        pygame.display.update()
    
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    game_over = True
                    game_close = False
                if event.key == pygame.K_c:
                    gameLoop()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
            game_close = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x1_change = -snake_block
                y1_change = 0
            elif event.key == pygame.K_RIGHT:
                x1_change = snake_block
                y1_change = 0
            elif event.key == pygame.K_UP:
                y1_change = -snake_block
                x1_change = 0
            elif event.key == pygame.K_DOWN:
                y1_change = snake_block
                x1_change = 0
    if x1 >= width or x1 < 0 or y1 >= height or y1 < 0:
        game_close = True
    x1 += x1_change
    y1 += y1_change
    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, (255, 0, 0), [apple_x, apple_y, snake_block, snake_block])
    pygame.draw.rect(screen, (0, 255, 0), [x1, y1, snake_block, snake_block])
    pygame.display.update()

    if x1 == apple_x and y1 == apple_y:
        score += 1
        print("Yummy!!")
    clock.tick(snake_speed)
    
    if x1 == apple_x and y1 == apple_y:
        score += 1
        apple_x = round(random.randrange(0, width - block_size) / 10.0) * 10.0
        apple_y = round(random.randrange(0, height - block_size) / 10.0) * 10.0
        snake_list.append((x1, y1))
        for x, y in snake_list:
            pygame.draw.rect(screen, (0,0,255), [x, y, block_size, block_size])
        screen.fill(black)
        pygame.draw.rect(screen, (255, 255, 0), [x1, y1, block_size, block_size])
        pygame.draw.rect(screen, (255, 0, 0), [apple_x, apple_y, block_size, block_size])
        pygame.display.set_caption("Score: " + str(score))
    
    if x1 >= width or x1 < 0 or y1 >= height or y1 < 0:
        running = False
        game_over_font = pygame.font.Font(None, 50)
        game_over_text = game_over_font.render("Game Over", True, (255,255,255))
        score_text = game_over_font.render("Score: " + str(score), True, (255,255,255))
        text_width, text_height = game_over_text.get_size()
        score_width, score_height = score_text.get_size()
        screen.blit(game_over_text, (width//2 - text_width//2, height//2 - text_height//2))
        screen.blit(score_text, (width//2 - score_width//2, height//2 - score_height//2 + text_height))
        
        pygame.display.update()
        clock.tick(600)
        pygame.time.delay(500)
            
show_splash_screen(screen)            
    
pygame.quit()
