# -*- coding:utf-8 -*-

def prob06():
    try:
        age = int(input("年齢を整数で入力してください: "))
    except:
        print("数字として解釈できませんでした。")
    
    if age < 0:
        print("我々とは違う時間軸に生きているようですね。")
    elif age < 120:
        print(f"こんにちは。あなたの年齢は{age}歳なんですね。")
    else:
        print(f"{age}歳!? 人類ではないようですね…。")

if __name__=='__main__':
    prob06()