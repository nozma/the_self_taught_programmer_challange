# -*- coding:utf-8 -*-


def main():
    answer = [1, 5, 99]

    while(True):
        user = input("数字を予想して入力してね!(qで終了): ")
        if user == "q":
            break

        try:
            num = int(user)

            if num in answer:
                print("正解!")
            else:
                print("不正解!")

        except ValueError:
            print("整数を入力してください(qで終了します)。")


if __name__ == '__main__':
    main()
