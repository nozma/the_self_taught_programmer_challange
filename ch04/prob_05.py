# -*- coding:utf-8 -*-


def tofloat(s: str) -> float:
    """
    文字列型の値を受け取ってfloat型として返します。
    """
    try:
        return(float(s))
    except Exception as err:
        print("float型に変換出来ませんでした。", err)


if __name__ == '__main__':
    print(tofloat(123))
    print(tofloat("1.1"))
    print(tofloat("1.23"))
    print(tofloat("abc"))
