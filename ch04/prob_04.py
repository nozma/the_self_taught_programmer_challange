# -*- coding:utf-8 -*-


def div2(num: int) -> int:
    """
    整数を受け取り、2で割って得られる整数を返します。
    """
    return int(num / 2)


def multiply4(num: int) -> int:
    """
    整数を受け取り、4倍した整数を返します。
    """
    return int(num * 4)


if __name__ == '__main__':
    n = div2(6)
    m = multiply4(n)
    print("結果は{}です".format(m))
    n = div2(5)
    m = multiply4(n)
    print("結果は{}です".format(m))
