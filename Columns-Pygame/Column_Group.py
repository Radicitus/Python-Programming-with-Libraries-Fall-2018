import pygame
import random
from Box import Box


class ColumnGroup:
    def __init__(self, settings, screen):
        self.settings = settings
        self.screen = screen
        self.initial_position = [0, random.randint(0, 5)]
        self.position = self.initial_position
        self.boxes = []
        row = 0
        for box in range(3):
            col = self.position[1]
            self.boxes.append(Box(row, col, screen))
            row -= 1
        self.move_right = False
        self.move_left = False

    def rotate(self):
        color_1 = self.boxes[2].get_color()
        color_2 = self.boxes[0].get_color()
        color_3 = self.boxes[1].get_color()
        self.boxes[0].set_color(color_1)
        self.boxes[1].set_color(color_2)
        self.boxes[2].set_color(color_3)

    def update(self, down=False):
        if self.move_right and self.position[1] < 5:
            self.position[1] += 1
            for box in self.boxes:
                box.update_position(box.get_position()[0], box.get_position()[1] + 1)
        if self.move_left and self.position[1] > 0:
            self.position[1] -= 1
            for box in self.boxes:
                box.update_position(box.get_position()[0], box.get_position()[1] - 1)
        if down:
            self.position[0] += 1
            for box in self.boxes:
                box.update_position(box.get_position()[0] + 1, box.get_position()[1])

    def get_all_position(self):
        to_return = []
        for box in self.boxes:
            to_return.append(box.get_position())
        return to_return

    def get_position(self):
        return self.position

    def to_add(self):
        return self.boxes

    def is_left(self):
        return self.move_left

    def is_right(self):
        return self.move_right

    def change_left(self):
        if self.move_left:
            self.move_left = False
        else:
            self.move_left = True

    def change_right(self):
        if self.move_right:
            self.move_right = False
        else:
            self.move_right = True


