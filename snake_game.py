# Written by CJ Teas

import pygame
import time
import random
pygame.init()

display_width = 800
display_height = 600

display = pygame.display.set_mode((display_width, display_height))
pygame.display.update()
pygame.display.set_caption('Welcome to CJs Snake Game! ')

# Assigning colors to draw the snake and food.
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
blue = (50, 153, 213)

# Set clock to update screen 
clock = pygame.time.Clock()

# Set variable for snake size
snake_movement = 20

# Set rate of change of time (update speed)
snake_speed = 20

# Set font style
font_style = pygame.font.SysFont('Times New Roman', 50)

# Defining a function to draw our snake
def our_snake(snake_movement, snake_list):
    for x in snake_list:
        pygame.draw.rect(display, black, [x[0], x[1], snake_movement, snake_movement])

# Defining a score display function
def user_score(score):
    value = font_style.render('Your Score: {}'.format(score), True, white)
    display.blit(value, (0, 0))

# Defining a function to draw messages to the display. 
def message(msg, color):
    mesg = font_style.render(msg, True, color)
    display.blit(mesg, [display_width / 6, display_height / 3])

def game_loop():
    game_over = False # Game is started as not over.
    game_close = False

    x1 = display_width / 2
    y1 = display_height / 2

    # Variables to make snake move
    x1_change = 0
    y1_change = 0

    snake_list = []
    length_of_snake = 1

    # Setting food coordinates
    foodx = round(random.randrange(0, display_width - snake_movement) / snake_movement) * snake_movement
    foody = round(random.randrange(0, display_height - snake_movement) / snake_movement) * snake_movement

    while not game_over: # While the game isn't over, run the sequence of events.

        while game_close == True: 
            display.fill(blue)
            message('You Lost! Press "C" to play again, or "Q" to quit.', red)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_c:
                        game_loop()
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT: # When you click x button program terminates
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_movement
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    x1_change = 0
                    y1_change = -snake_movement
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_movement
                    y1_change = 0
                elif event.key == pygame.K_DOWN:
                    x1_change = 0
                    y1_change = snake_movement
        if x1 > display_width or x1 < 0 or y1 > display_height or y1 < 0:
            game_close = True
        
        # Applying change to the snake
        x1 += x1_change
        y1 += y1_change

        # Changing display color to blue
        display.fill(blue)

        # Adding onto length of snake
        pygame.draw.rect(display, red, [foodx, foody, snake_movement, snake_movement])

        snake_head = []
        snake_head.append(x1)
        snake_head.append(y1)
        snake_list.append(snake_head)

        if len(snake_list) > length_of_snake:
            del snake_list[0]

        for x in snake_list[:-1]:
            if x == snake_head:
                game_close = True

        our_snake(snake_movement, snake_list)
        user_score(length_of_snake - 1)

        pygame.display.update()


        # Drawing food to display
       

        pygame.display.update() 

        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, display_width - snake_movement) / snake_movement) * snake_movement
            foody = round(random.randrange(0, display_height - snake_movement) / snake_movement) * snake_movement
            length_of_snake += 1

        clock.tick(snake_speed)

    pygame.quit()
    quit()

game_loop()

