"""https://www.hackerrank.com/challenges/re-group-groups/problem."""
import re


def find_repeated_char():
    """Find the first char repeated from left to right."""
    pattern = r'([a-zA-Z0-9])\1'

    s = input()
    result = re.search(pattern, s)
    if result:
        print(result.group(0)[0])
    else:
        print('-1')


if __name__ == '__main__':
    find_repeated_char()
