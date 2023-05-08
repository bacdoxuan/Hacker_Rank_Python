"""https://www.hackerrank.com/challenges/incorrect-regex/problem."""
import re


def check_regex():
    """How to check a pattern if it is in correct regex format?."""
    for _ in range(int(input())):
        try:
            re.compile(input())
        except Exception:
            print('False')
        else:
            print('True')


if __name__ == '__main__':
    check_regex()
