# -*- coding:utf-8


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

    def change_size(self, diff):
        self.width += diff


if __name__ == '__main__':
    square = Square(5.0)
    while(True):
        diff = input("正方形の横幅は{}です。いくつ変化させますか？(qで終了): ".format(square.width))
        if diff == "q":
            break
        try:
            diff = float(diff)
            square.change_size(diff)
        except ValueError:
            print("入力を数字として解釈できませんでした。")
