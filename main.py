import pygame
from src.settings import *
from src.snake import Snake

pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption(TITLE)

clock = pygame.time.Clock()
snake = Snake()

running = True

while running:

    for event in pygame.event.get():
        snake.move()
        
    if event.type == pygame.QUIT:
        running = False

    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_UP:
            snake.change_direction((0, -1))

        elif event.key == pygame.K_DOWN:
            snake.change_direction((0, 1))

        elif event.key == pygame.K_LEFT:
            snake.change_direction((-1, 0))

        elif event.key == pygame.K_RIGHT:
            snake.change_direction((1, 0))


    screen.fill(BACKGROUND)
    snake.draw(screen)
    pygame.display.flip()

    clock.tick(FPS)

pygame.quit()