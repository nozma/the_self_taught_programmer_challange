# -*- coding:utf-8 -*-


def prob03(arg1, arg2, arg3, arg4=1, arg5=2):
    """
    3つの必須引数と2つのオプション引数を持つ関数の例です。
    """
    print(f"引数1は{arg1}です")
    print(f"引数2は{arg2}です")
    print(f"引数3は{arg3}です")
    print(f"引数4は{arg4}です")
    print(f"引数5は{arg5}です")


if __name__ == '__main__':
    prob03(1, 2, 3, 4, 5)
    prob03(1, 1, 1)
