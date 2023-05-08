"""https://www.hackerrank.com/challenges/py-collections-ordereddict/problem."""
from collections import OrderedDict


def find_net_prices():
    """.

    https://www.hackerrank.com/challenges/py-collections-ordereddict/problem
    """
    n = int(input())
    things = OrderedDict()
    for _ in range(n):
        *item, price = input().split()
        item, price = ' '.join(item), int(price)
        if item in things:
            things[item] += price
        else:
            things[item] = price

    for i, j in things.items():
        print(i, j)


if __name__ == '__main__':
    find_net_prices()
