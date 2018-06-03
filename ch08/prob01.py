# -*- coding:utf-8 -*-
import statistics


def main():
    nums = [1, 2, 4, 5]
    print("numbers: " + str(nums))
    print("median: " + str(statistics.median(nums)))
    print("low median: " + str(statistics.median_low(nums)))
    print("high median: " + str(statistics.median_high(nums)))


if __name__ == '__main__':
    main()
