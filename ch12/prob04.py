# -*- coding:utf-8 -*-


class Hexagon:
    def __init__(self, s1, s2, s3, s4, s5, s6):
        self.s1 = s1
        self.s2 = s2
        self.s3 = s3
        self.s4 = s4
        self.s5 = s5
        self.s6 = s6

    def calculate_perimeter(self):
        return self.s1 + self.s2 + self.s3 + self.s4 + self.s5 + self.s6


if __name__ == '__main__':
    num = input("六角形の辺を6つ半角スペース区切りで入力してください:")
    try:
        s = [float(i) for i in num.split()]
        hex = Hexagon(s[0], s[1], s[2], s[3], s[4], s[5])
        print("外周の長さは{}です。".format(hex.calculate_perimeter()))
    except ValueError:
        print("数字以外の入力がありました。")
    except IndexError:
        print("辺は6つ入力してください。")
