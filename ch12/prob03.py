# -*- coding:utf-8 -*-


class Triangle:
    def __init__(self, b, h):
        self.base = b
        self.height = h

    def area(self):
        return self.base * self.height * 0.5


if __name__ == '__main__':
    try:
        b = float(input("底辺の長さを入力してください:"))
        h = float(input("高さを入力してください:"))
        triangle = Triangle(b, h)
        print("三角形の面積は{}です。".format(triangle.area()))
    except ValueError:
        print("数字で入力してください。")
