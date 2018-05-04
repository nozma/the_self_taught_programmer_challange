# -*- coding:utf-8 -*-

def mydiv():
    try:
        x, y = [int(i) for i in input("余りを計算します。2つの整数を'x y'のように入力してください:").split()]
    except:
        print("2つの整数として解釈できませんでした。")
        return

    try:
        print("{0}÷{1}の余りは{2}です。".format(x, y, x % y))
    except:
        print("余りを計算できませんでした。")
        return

if __name__ == '__main__':
    mydiv()