# -*- coding:utf-8 -*-


def cubed(n: float) -> float:
    return(n**3)


if __name__ == '__main__':
    try:
        num = float(input("数字を入力してください:"))
        print("{}の3乗は{}です。".format(num, cubed(num)))
    except ValueError:
        print("数字ではない文字列が渡されました。")
