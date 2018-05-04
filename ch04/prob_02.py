# -*- coding:utf-8 -*-


def echo(s: str):
    """
    文字列を受け取って文字列を返します。
    """
    return s


if __name__ == '__main__':
    s = echo(input("何か入力してください:"))
    print("あなたは「{}」と入力しました。".format(str(s)))
