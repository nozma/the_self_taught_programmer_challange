# -*- coding:utf-8 -*-


class Apple:
    def __init__(self, wg, w, h, br):
        self.weight = wg  # 重さ
        self.width = w    # 幅
        self.height = h   # 高さ
        self.brix = br    # 糖度


if __name__ == '__main__':
    apple = Apple(100, 50, 50, 13)
    print("重量: {}".format(apple.weight))
    print("幅: {}".format(apple.width))
    print("高さ: {}".format(apple.height))
    print("糖度: {}".format(apple.brix))
