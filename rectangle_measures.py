import math

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return 2 * (self.width + self.height)

    def get_diagonal(self):
        diagonal = round(math.sqrt((self.width ** 2) + (self.height ** 2)),2)
        return diagonal

    def set_width(self, new_width):
        self.width = new_width

    def set_height(self, new_height):
        self.height = new_height

    def retrieve_dimensions(self):
        return self.width, self.height
