"""https://www.hackerrank.com/challenges/compress-the-string/problem."""
from itertools import groupby


def stringcompress():
    """User itertools.groupby to compress a string.

    Input.
    abbbccdefffaaabbbccc
    Output.
    (1, 'a') (3, 'b') (2, 'c') (1, 'd') (1, 'e') (3, 'f') (3, 'a') (3, 'b') (3, 'c')
    """  # NOQA
    data = input()
    for i, j in groupby(data):
        print((len(list(j)), int(i)), end=' ')


if __name__ == '__main__':
    stringcompress()
