# -*- coding:utf-8 -*-
import cubed


def main():
    try:
        num = float(input("なにか数字入れてや: "))
        print("{}の3乗は{}やで。".format(num, cubed.cubed(num)))
    except ValueError:
        print("数字ちゃうで…")


if __name__ == '__main__':
    main()
