"""https://www.hackerrank.com/challenges/iterables-and-iterators/problem."""
from itertools import combinations


def find_percentage():
    """https://www.hackerrank.com/challenges/iterables-and-iterators/problem."""  # NOQA
    data = list([input(), list(input().split())])
    n = int(input())
    combs = list(combinations(data[1], n))
    subsets = [i for i in combs if 'a' in i]
    print("%.3f" % (len(subsets) / len(combs)))


if __name__ == '__main__':
    find_percentage()
