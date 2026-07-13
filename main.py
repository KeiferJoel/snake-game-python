import pygame
from src.settings import *
from src.snake import Snake
from src.food import Food

pygame.init()
font = pygame.font.SysFont("Arial", 28)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption(TITLE)

clock = pygame.time.Clock()
snake = Snake()
food = Food()

score = 0

running = True

while running:

    for event in pygame.event.get():
        snake.move()
        
        if snake .body[0] == food.position:
            snake.eat()
            food.randomize(snake.body)
            score += 1
        

        score_text = font.render(f"Score: {score}", True, TEXT)
        screen.blit(score_text, (15, 15))

        

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
    food.draw(screen)
    pygame.display.flip()

    clock.tick(FPS)

pygame.quit()