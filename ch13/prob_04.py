# -*- coding:utf-8 -*-


class Horse():
    def __init__(self, name, rider):
        self.name = name
        self.rider = rider


class Rider():
    def __init__(self, name):
        self.name = name


if __name__ == '__main__':
    horse_name = input("馬の名前を入力してください: ")
    rider_name = input("騎手の名前を入力してください: ")
    rider = Rider(rider_name)
    horse = Horse(horse_name, rider)

    print("馬の名前は{}です。".format(horse.name))
    print("騎手の名前は{}です。".format(horse.rider.name))
