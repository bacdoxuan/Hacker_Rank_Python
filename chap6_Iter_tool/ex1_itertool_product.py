""".

https://www.hackerrank.com/challenges/itertools-product/problem
"""
import itertools


def iter_product():
    """.

    https://www.hackerrank.com/challenges/itertools-product/problem
    """
    number_a = sorted(list(map(int, input().split())))
    number_b = sorted(list(map(int, input().split())))
    products = itertools.product(number_a, number_b)
    print(' '.join(str(i) for i in products))


if __name__ == '__main__':
    iter_product()
