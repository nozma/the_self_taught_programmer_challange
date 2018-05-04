# -*- coding:utf-8 -*-

def prob02():
    try:
        num = float(input("数値を入力: "))
    except:
        print("数値として解釈できませんでした。")
        return
    
    if(num <= 10):
        print("値は10以下ですね")
    elif(num <= 25):
        print("値は10より大きく、25以下ですね。")
    else:
        print("値は25以上ですね。")

if __name__ == '__main__':
    prob02()
