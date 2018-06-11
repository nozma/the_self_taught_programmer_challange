# -*- coding:utf-8 -*-
import math


class Circle:
    def __init__(self, r):
        self.radius = r

    def area(self):
        return math.pi * (self.radius ** 2)


if __name__ == '__main__':
    try:
        r = float(input("半径を入力してください: "))
        circle = Circle(r)
        print("半径{}の円の面積は{}です".format(circle.radius, circle.area()))
    except ValueError:
        print("数字ではない文字が入力されました。")
