# -*- coding:utf-8 -*-


class Rectangle():
    def __init__(self, w, h):
        self.width = w
        self.height = h

    def calculate_perimeter(self):
        return (self.width + self.height) * 2


class Square():
    def __init__(self, w):
        self.width = w

    def calculate_perimeter(self):
        return self.width * 4


if __name__ == '__main__':
    w = input("幅を入力: ")
    h = input("高さを入力: ")
    try:
        w = float(w)
        h = float(h)
        rectangle = Rectangle(w, h)
        square = Square(w)
        print(
            "幅{}, 高さ{}の長方形の外周は{}です。".format(
                w, h,
                rectangle.calculate_perimeter()
            )
        )
        print(
            "一辺の長さ{}の正方形の外周は{}です。".format(
                w,
                square.calculate_perimeter()
            )
        )
    except ValueError:
        print("入力を数値として解釈できませんでした。")
