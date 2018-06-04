# -*- coding:utf-8 -*-


def main():
    ans = input("好きな食べ物は何ですか?: ")
    with open("answer.txt", "w") as f:
        f.write(ans)


if __name__ == '__main__':
    main()
