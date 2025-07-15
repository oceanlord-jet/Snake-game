import pygame
import sys
import time
import random

pygame.init()

# Screen dimensions
width = 800
height = 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake Game")

# Colors
black = (0,0,0)
white = (255,255,255)
red   = (255,0,0)
green = (0,255,0)

# Snake properties
snake_block = 10
snake_speed = 15
snake_list = []
snake_length = 1

# Initial position
x1 = width/2
y1 = height/2
x1_change = 0
y1_change = 0

# Apple position
apple_x = round(random.randrange(0, width - snake_block) / 10.0) * 10.0
apple_y = round(random.randrange(0, height - snake_block) / 10.0) * 10.0

clock = pygame.time.Clock()
game_over = False

# ---------------- NEW: Score Display ----------------
font_style = pygame.font.SysFont("bahnschrift", 25)

def show_score(score):
    value = font_style.render("Score: " + str(score), True, white)
    screen.blit(value, [10, 10])
# ----------------------------------------------------

def show_splash_screen():
    splash = True
    while splash:
        screen.fill((0, 0, 0))
        # Draw white dots
        for _ in range(100):
            x = random.randint(0, width)
            y = random.randint(0, height)
            pygame.draw.circle(screen, (255, 255, 255), (x, y), 2)
        # Draw start button
        font = pygame.font.Font(None, 40)
        text = font.render("START", True, (0,0,0))
        text_rect = text.get_rect(center=(width//2, height//2))
        pygame.draw.rect(screen, (255,255,255), text_rect.inflate(10, 10))
        screen.blit(text, text_rect)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN and text_rect.collidepoint(event.pos):
                splash = False

show_splash_screen()

# Main Game Loop
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and x1_change == 0:
                x1_change = -snake_block
                y1_change = 0
            elif event.key == pygame.K_RIGHT and x1_change == 0:
                x1_change = snake_block
                y1_change = 0
            elif event.key == pygame.K_UP and y1_change == 0:
                y1_change = -snake_block
                x1_change = 0
            elif event.key == pygame.K_DOWN and y1_change == 0:
                y1_change = snake_block
                x1_change = 0

    # Update head position
    x1 += x1_change
    y1 += y1_change

    # Check for boundary collision
    if x1 >= width or x1 < 0 or y1 >= height or y1 < 0:
        game_over = True

    screen.fill(black)
    pygame.draw.rect(screen, red, [apple_x, apple_y, snake_block, snake_block])

    # Update snake body
    snake_head = [x1, y1]
    snake_list.append(snake_head)
    if len(snake_list) > snake_length:
        del snake_list[0]

    # Check self collision
    for segment in snake_list[:-1]:
        if segment == snake_head:
            game_over = True

    # Draw snake
    for segment in snake_list:
        pygame.draw.rect(screen, green, [segment[0], segment[1], snake_block, snake_block])

    # ---------------- NEW: Show Score ----------------
    show_score(snake_length - 1)
    # --------------------------------------------------

    pygame.display.update()

    # Check if apple eaten
    if x1 == apple_x and y1 == apple_y:
        snake_length += 1
        apple_x = round(random.randrange(0, width - snake_block) / 10.0) * 10.0
        apple_y = round(random.randrange(0, height - snake_block) / 10.0) * 10.0

    clock.tick(snake_speed)

# Game Over screen
font = pygame.font.Font(None, 50)
game_over_text = font.render("Game Over", True, white)
score_text = font.render("Score: " + str(snake_length-1), True, white)
text_width, text_height = game_over_text.get_size()
score_width, score_height = score_text.get_size()
screen.fill(black)
screen.blit(game_over_text, (width//2 - text_width//2, height//2 - text_height//2))
screen.blit(score_text, (width//2 - score_width//2, height//2 - score_height//2 + text_height))
pygame.display.update()
time.sleep(2)

pygame.quit()
