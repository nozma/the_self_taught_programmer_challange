# -*- coding:utf-8 -*-
# 2つの値で割り算をして、商を出力する

def mydiv2():
    try:
        x, y = [int(i) for i in input("2数の商を計算します。'x y'のように数字を入力してください: ").split()]
    except Exception as err:
        print("2つの数字として解釈できませんでした。", err)
        return

    try:
        print("{0}÷{1}の商は{2}です。".format(x, y, x // y))
    except Exception as err:
        print("商を計算できませんでした。", err)

if __name__ == '__main__':
    mydiv2()