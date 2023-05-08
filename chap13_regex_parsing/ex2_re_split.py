"""https://www.hackerrank.com/challenges/re-split/problem."""
import re


def split_re(s):
    a = list(filter(None, re.split('\.', s)))
    for i in a:
        b = list(filter(None, re.split(',', i)))
        for j in b:
            print(j)


if __name__ == '__main__':
    s = input()
    split_re(s)
