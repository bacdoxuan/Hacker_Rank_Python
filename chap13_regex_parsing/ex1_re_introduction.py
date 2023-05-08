"""https://www.hackerrank.com/challenges/introduction-to-regex/problem."""
import re


def check_float_form():
    """Check if input numbers in correct float form"""
    pattern = r'(\+|-)?\d*\.\d+$'
    for i in range(int(input())):
        s = input()
        print(bool(re.match(pattern, s)))


if __name__ == '__main__':
    check_float_form()
