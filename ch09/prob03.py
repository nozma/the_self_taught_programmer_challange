# -*- coding:utf-8 -*-
import csv


def main():
    movies = [
        ["Top Gun", "Risky Business", "Minority Report"],
        ["Titanic", "The Revenant", "Inception"],
        ["Training Day", "Man on Fire", "Flight"]
    ]
    with open("result.csv", "w") as f:
        w = csv.writer(f)
        for movie in movies:
            w.writerow(movie)


if __name__ == '__main__':
    main()
