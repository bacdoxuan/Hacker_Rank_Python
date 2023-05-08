"""https://www.hackerrank.com/challenges/validating-the-phone-number/problem."""
import re

if __name__ == '__main__':
    pattern = r'(7|8|9)\d{9}$'
    n = int(input())
    for _ in range(n):
        if re.match(pattern, input()):
            print('YES')
        else:
            print('NO')
