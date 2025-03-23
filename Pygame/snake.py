'''The snake is one square in size, moves in a uniform motion in the horizontal
or vertical direction, changing direction (turn) occurs after pressing a key.
Movement backwards is prohibited (end of the game). The board has periodic
boundary conditions. The player's task is to move the snake and eat nutritious
fruits that appear randomly on the board and live for a specified time. At any
time, there can be at most one fruit on the board. The game ends after
a specified time or after an illegal move. The result of the game is the state
of the fruit counter. There are two types of fruits, of different colors:
nutritious fruits and poisoned fruits. After eating a poisoned fruit, the
player is punished by subtracting points. Periodic increase in the snake's
speed and lengthening after eating a nutritious fruit, and shortening after
eating a poisoned fruit.'''

import pygame
import random
import sys

pygame.init()

pygame.font.init()
move_font = pygame.font.SysFont('Consolas', 20)
font = pygame.font.SysFont('Consolas', 50, bold=True)

window_size = 800
tile_size = 40
screen = pygame.display.set_mode((window_size, window_size))
pygame.display.set_caption('Snake')
# tiles
tile_centers = (tile_size//2, window_size-tile_size//2, tile_size)
random_position = lambda: [random.randrange(*tile_centers),
                           random.randrange(*tile_centers)]
# snake's head
snake = pygame.rect.Rect([0, 0, tile_size-2, tile_size-2])
# snake's position
snake.center = random_position()
# snake's length
snake_length = 1
snake_segments = [snake.copy()]
# moving a snake
snake_direction = (0, 0)
directions = {pygame.K_UP: 1, pygame.K_DOWN: 1,
              pygame.K_RIGHT: 1, pygame.K_LEFT: 1}
# snake's speed
start_time = 0.0000001
time, time_step = 0, 250 # delay [ms]
# fruit lifetime [ms]
fruit_time, living_time = 0, 10000

# fruits
fruit = pygame.rect.Rect([0, 0, tile_size-2, tile_size-2])
fruit.center = random_position()
type_fruit = 1
# eaten fruits
score = 0
# counting time - game lasts 100 seconds
counter = 100
counter_txt = font.render(str(counter), True, 'white')
timer_event = pygame.USEREVENT+1
pygame.time.set_timer(timer_event, 1000)

clock = pygame.time.Clock()
t = 60

done = False
finish = False

# main loop
while not done:
    screen.fill('black')
    move_txt = move_font.render('Use arrow buttons', True, 'white')
    screen.blit(move_txt, (550, 30))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == timer_event:
            counter -= 1
            counter_txt = font.render(str(counter), True, 'white')
            
    if not finish:
        screen.blit(counter_txt, (20, 20))

        # moving a snake on a board
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            if directions[pygame.K_UP]:
                snake_direction = (0, -tile_size)
                directions = {pygame.K_UP: 1, pygame.K_DOWN: 0,
                            pygame.K_RIGHT: 1, pygame.K_LEFT: 1}
            else:
                finish = True
        if keys[pygame.K_DOWN]:
            if directions[pygame.K_DOWN]:
                snake_direction = (0, tile_size)
                directions = {pygame.K_UP: 0, pygame.K_DOWN: 1,
                                pygame.K_RIGHT: 1, pygame.K_LEFT: 1}
            else:
                finish = True
        if keys[pygame.K_RIGHT]:
            if directions[pygame.K_RIGHT]:
                snake_direction = (tile_size, 0)
                directions = {pygame.K_UP: 1, pygame.K_DOWN: 1,
                                pygame.K_RIGHT: 1, pygame.K_LEFT: 0}
            else:
                finish = True
        if keys[pygame.K_LEFT]:
            if directions[pygame.K_LEFT]:
                snake_direction = (-tile_size, 0)
                directions = {pygame.K_UP: 1, pygame.K_DOWN: 1,
                                pygame.K_RIGHT: 0, pygame.K_LEFT: 1}
            else:
                finish = True
                
        # drawing a snake
        [pygame.draw.rect(screen, 'green', seg) for seg in snake_segments]

        # moving a snake
        start_time = pygame.time.get_ticks()
        time_now = pygame.time.get_ticks()
        if time_now - time > time_step:
            time = time_now
            snake.move_ip(snake_direction)
            snake_segments.append(snake.copy())
            snake_segments = snake_segments[-snake_length:]

        # nutritious and poisoned fruits
        if type_fruit == 1:
            pygame.draw.rect(screen, 'red', fruit)
        if type_fruit == 0:
            pygame.draw.rect(screen, 'blue', fruit)

        # interaction with fruits
        if snake.center == fruit.center:
            if type_fruit == 1:           
                snake_length += 1
                score += 1
            if type_fruit == 0:
                snake_length -=1
                score -=1
            if snake_length == 0:
                finish == True
            type_fruit = random.randint(0, 1)
            fruit.center = random_position()
            # fruit_time_now = pygame.time.get_ticks()

        # fruits on a board
        fruit_time_now = pygame.time.get_ticks()
        if fruit_time_now - fruit_time > living_time:
            type_fruit = random.randint(0, 1)
            fruit.center = random_position()
            fruit_time = fruit_time_now
            # increase snake's velocity
            time_step -= 25
        if time_step == 0:
            finish = True

        # end game after 100 seconds
        if counter == 0:
            finish = True
            
        # check borders and self-eating
        self_eat = pygame.Rect.collidelist(snake, snake_segments[:-1]) != -1
        if snake.left < 0 or snake.right > window_size or snake.top < 0\
           or snake.bottom > window_size or self_eat:
            finish = True

    if finish:
        screen.fill('black')
        game_txt = font.render('Game over!', True, 'white')
        score_txt = font.render('Score: '+str(score), True, 'white')
        screen.blit(game_txt, (window_size/2-150, window_size/2-50))
        screen.blit(score_txt, (window_size/2-130, window_size/2+20))
    
    pygame.display.flip()
    clock.tick(t)

pygame.quit()
