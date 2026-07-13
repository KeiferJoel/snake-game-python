import pygame
from src.settings import CELL_SIZE, SNAKE


class Snake:
    def __init__(self):
        self.body = [
            (10, 10),
            (9, 10),
            (8, 10)
        ]

        # Dirección inicial (hacia la derecha)
        self.direction = (1, 0)

    def move(self):
        head_x, head_y = self.body[0]

        dx, dy = self.direction

        new_head = (head_x + dx, head_y + dy)

        # Agrega la nueva cabeza
        self.body.insert(0, new_head)

        # Elimina la cola
        self.body.pop()

    def change_direction(self, direction):
        dx, dy = self.direction
        new_dx, new_dy = direction

        # Evita girar 180°
        if (dx + new_dx, dy + new_dy) != (0, 0):
            self.direction = direction

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