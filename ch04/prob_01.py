# -*- coding:utf-8 -*-


def square(num):
    """
    数値を受け取り、2乗した値を返します。
    """
    try:
        return num ** 2
    except Exception as err:
        print("数値ではない値が渡されました。", err)


if __name__ == "__main__":
    n = input("数値を入力してください: ")
    try:
        print("{0}の二乗は{1}です。".format(n, square(float(n))))
    except Exception as err:
        print("数値として解釈できませんでした。", err)
