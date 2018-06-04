# -*- coding:utf-8 -*-
import csv


def main():
    movies = [
        ["トップガン", "リスキービジネス", "マイノリティ・リポート"],
        ["タイタニック", "レヴェナント", "インセプション"],
        ["トレーニングデイ", "マン・オン・ファイアー", "フライト"]
    ]

    with open("result_ja.csv", "w") as f:
        w = csv.writer(f)
        for movie in movies:
            w.writerow(movie)


if __name__ == '__main__':
    main()
