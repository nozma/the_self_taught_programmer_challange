# -*- coding:utf-8


class Shape():
    def __init__(self):
        pass

    def what_am_i(self):
        return("I am a shape.")


class Rectangle(Shape):
    def __init__(self, w, h):
        self.width = w
        self.height = h

    def calculate_perimeter(self):
        return (self.width + self.height) * 2


class Square(Shape):
    def __init__(self, w):
        self.width = w

    def calculate_perimeter(self):
        return self.width * 4

    def change_size(self, diff):
        self.width += diff


if __name__ == '__main__':
    rect = Rectangle(3, 5)
    print(rect.what_am_i())
