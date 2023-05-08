"""https://www.hackerrank.com/challenges/hex-color-code/problem."""
import re


def check_hex_format(s):
    """Check and list all valid format of hex-color-code from input."""
    pattern = r'(?<!\n)#[\da-f]{3}(?!\w)(?!\n)|(?<!\n)#[\da-f]{6}(?!\w)(?!\n)'
    result = re.findall(pattern, s, flags=re.I)
    for i in result:
        print(i)


if __name__ == '__main__':
    n = int(input())
    s = ''
    for _ in range(n):
        s += input() + '\n'
    check_hex_format(s)
