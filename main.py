import pygame
import time
import random

# initialisation pygame
pygame.init()
# add screen size
width, height = 640, 480
screen = pygame.display.set_mode((width, height))

pygame.display.update()
pygame.display.set_caption('Snake game by me')

colors = {
    'snake_head': (0, 255, 0),
    'snake_tail': (0, 200, 0),
    'apple': (255, 0, 0)
}

snake_pos = {
    'x': width / 2 - 10,
    'y': height / 2 - 10,
    'x_change': 0,
    'y_change': 0
}

snake_size = (10, 10)

snake_speed = 10

snake_tails = []

for i in range(100):
    snake_tails.append([snake_pos['x'] + (i*10), snake_pos['y']])

food_size = (10, 10)
food_eaten = 0
food_pos = {
    'x': round(random.randrange(0, width - snake_size[0]) / 10) * 10,
    'y': round(random.randrange(0, height - snake_size[1]) / 10) * 10
}

game_end = False
while not game_end:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_end = True

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and snake_pos['y_change'] == 0:
                snake_pos['x_change'] = 0
                snake_pos['y_change'] = -snake_speed
            elif event.key == pygame.K_DOWN and snake_pos['y_change'] == 0:
                snake_pos['x_change'] = 0
                snake_pos['y_change'] = snake_speed
            elif event.key == pygame.K_LEFT and snake_pos['x_change'] == 0:
                snake_pos['x_change'] = -snake_speed
                snake_pos['y_change'] = 0
            elif event.key == pygame.K_RIGHT and snake_pos['x_change'] == 0:
                snake_pos['x_change'] = snake_speed
                snake_pos['y_change'] = 0

    time.sleep(0.1)

    screen.fill((0, 0, 0))

    ltx = snake_pos['x']
    lty = snake_pos['y']

    for i, v in enumerate(snake_tails):
        _ltx, _lty = snake_tails[i][0], snake_tails[i][1]
        snake_tails[i][0], snake_tails[i][1] = ltx, lty
        ltx, lty = _ltx, _lty

    for i, v in enumerate(snake_tails):
        if (snake_pos['x'] + snake_pos['x_change'] == snake_tails[i][0] and snake_pos['y'] + snake_pos['y_change'] ==
                snake_tails[i][1]):
            snake_tails = snake_tails[:i]
            break

    for t in snake_tails:
        pygame.draw.rect(screen, colors['snake_tail'], [
            t[0],
            t[1],
            snake_size[0],
            snake_size[1]])

    snake_pos['x'] += snake_pos['x_change']
    snake_pos['y'] += snake_pos['y_change']

    if (snake_pos['x'] < -snake_size[0]):
        snake_pos['x'] = width
    elif (snake_pos['x'] > width):
        snake_pos['x'] = 0
    elif (snake_pos['y'] < -snake_size[1]):
        snake_pos['y'] = height
    elif (snake_pos['y'] > height):
        snake_pos['y'] = 0

    # snake
    pygame.draw.rect(screen, colors['snake_head'], [
        snake_pos['x'],
        snake_pos['y'],
        snake_size[0],
        snake_size[1]])

    # food
    pygame.draw.rect(screen, colors['apple'], [
        food_pos['x'],
        food_pos['y'],
        food_size[0],
        food_size[1]])

    if (snake_pos['x'] == food_pos['x']
            and snake_pos['y'] == food_pos['y']):
        food_eaten += 1
        food_pos = {
            'x': round(random.randrange(0, width - snake_size[0]) / 10) * 10,
            'y': round(random.randrange(0, height - snake_size[1]) / 10) * 10
        }
        snake_tails.append([food_pos['x'], food_pos['y']])
    pygame.display.update()
pygame.quit()
quit()
