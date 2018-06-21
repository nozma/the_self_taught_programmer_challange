# -*- coding:utf-8 -*-


class MyClass():
    def __init__(self, val):
        self.val = val


def my_compare(obj1, obj2):
    return obj1 is obj2


if __name__ == '__main__':
    x = MyClass("hoge")
    y = MyClass("hoge")
    z = x
    print(my_compare(x, y))
    print(my_compare(x, z))
