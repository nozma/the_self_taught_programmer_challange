# -*- coding:utf-8 -*-


class Square():
    square_list = []

    def __init__(self, w):
        self.width = float(w)
        self.square_list.append(self)

    def __repr__(self):
        w = self.width
        return "{} by {} by {} by {}".format(w, w, w, w)


if __name__ == '__main__':
    sq1 = Square(5)
    sq2 = Square(10)
    print(sq1)
    print(Square.square_list)
