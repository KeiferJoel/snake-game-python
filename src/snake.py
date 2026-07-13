import pygame
from src.settings import CELL_SIZE, SNAKE


class Snake:
    def __init__(self):
        self.body = [
            (10, 10),
            (9, 10),
            (8, 10)
        ]

    def draw(self, screen):
        for segment in self.body:
            x = segment[0] * CELL_SIZE
            y = segment[1] * CELL_SIZE

            rect = pygame.Rect(x, y, CELL_SIZE, CELL_SIZE)

            pygame.draw.rect(
                screen,
                SNAKE,
                rect,
                border_radius=5
            )