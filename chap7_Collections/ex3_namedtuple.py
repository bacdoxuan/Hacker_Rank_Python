"""https://www.hackerrank.com/challenges/py-collections-namedtuple/problem."""
from collections import namedtuple


def cal_average_points():
    """.

    https://www.hackerrank.com/challenges/py-collections-namedtuple/problem
    """
    n = int(input())
    Student = namedtuple('Student', input().split())
    print('%.2f' % (sum([int(Student(*input().split()).MARKS) for _ in range(n)]) / n))  # NOQA


if __name__ == '__main__':
    cal_average_points()
