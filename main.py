import pygame
from src.settings import *

pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption(TITLE)

clock = pygame.time.Clock()

running = True

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(BACKGROUND)

    pygame.display.flip()

    clock.tick(FPS)

pygame.quit()