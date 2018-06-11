# -*- coding:utf-8 -*-


def hangman(word):
    wrong = 0
    stages = [
        "",
        "_______      ",
        "|      |     ",
        "|      O     ",
        "|     /|\    ",
        "|     / \    ",
        "|            "
    ]
    answer = list(word)
    board = ["_"] * len(word)
    win = False
    print("ハングマンへようこそ!")

    while wrong < len(stages) - 1:
        print("\n")
        char = input("1文字を予想してね: ")
        if char in answer:
            char_i = answer.index(char)
            board[char_i] = char
            answer[char_i] = '$'
        else:
            wrong += 1
        print(" ".join(board))
        print("\n".join(stages[0:wrong + 1]))
        if "_" not in board:
            print("あなたの勝ち!")
            print(" ".join(board))
            win = True
            break
    if not win:
        print("\n".join(stages))
        print("あなたの負け!正解は {}.".format(word))


if __name__ == '__main__':
    import random
    word_list = [
        "cat",
        "dog",
        "hangman",
        "magic",
        "python"
    ]
    hangman(random.choice(word_list))
