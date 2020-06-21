import random
import pygame

class Box():
    def __init__(self, row, col, screen):
        random_color = random.randint(0, 9)
        colors = [(255, 0, 0), (100, 0, 0), (0, 255, 0), (0, 100, 0), (0, 0, 255), (0, 0, 100), (255, 255, 0), (0, 255, 255), (255, 100, 0), (100, 255, 100)]
        self.color = colors[random_color]
        self.position = (row, col)
        self.screen = screen


    def update_position(self, new_row, new_col):
        self.position = (new_row, new_col)

    def get_position(self):
        return self.position

    def get_color(self):
        return self.color

    def set_color(self, c):
        self.color = c

    def blitme(self):
        x = self.position[1] * 40
        y = self.position[0] * 40
        pygame.draw.rect(self.screen, self.color, (x, y, 40, 40))
