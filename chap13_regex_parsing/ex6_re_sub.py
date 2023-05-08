"""https://www.hackerrank.com/challenges/re-sub-regex-substitution/problem."""
import re


def replace_string():
    """replace || by or, replace && by and."""
    no_lines = int(input())
    pattern1 = r'(?<=\s)\|{2}(?=\s)'
    pattern2 = r'(?<=\s)\&{2}(?=\s)'
    for _ in range(no_lines):
        s = input()
        s = re.sub(pattern1, 'or', s, flags=re.M)
        print(re.sub(pattern2, 'and', s, flags=re.M))


if __name__ == '__main__':
    replace_string()
