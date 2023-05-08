"""https://www.hackerrank.com/challenges/word-order/problem."""
from collections import OrderedDict


def word_count():
    """https://www.hackerrank.com/challenges/word-order/problem."""
    od = OrderedDict()
    for _ in range(int(input())):
        line = input()
        if line in od:
            od[line] += 1
        else:
            od[line] = 1
    print(len(od.keys()))
    print(*od.values())


if __name__ == '__main__':
    word_count()
