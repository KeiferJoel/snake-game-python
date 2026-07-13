import pygame
import random

from src.settings import CELL_SIZE, FOOD, WIDTH, HEIGHT


class Food:
    def __init__(self):
        self.position = (0, 0)
        self.randomize([])

    def randomize(self, snake_body):
        cols = WIDTH // CELL_SIZE
        rows = HEIGHT // CELL_SIZE

        while True:
            position = (
                random.randint(0, cols - 1),
                random.randint(0, rows - 1)
            )

            if position not in snake_body:
                self.position = position
                break

    def draw(self, screen):
        x = self.position[0] * CELL_SIZE
        y = self.position[1] * CELL_SIZE

        rect = pygame.Rect(x, y, CELL_SIZE, CELL_SIZE)

        pygame.draw.rect(
            screen,
            FOOD,
            rect,
            border_radius=10
        )