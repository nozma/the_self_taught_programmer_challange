# -*- coding:utf-8 -*-
import re


def main():
    str = "The ghost that says boo haunts the loo"
    matches = re.findall(".oo", str)
    print(matches)


if __name__ == '__main__':
    main()
