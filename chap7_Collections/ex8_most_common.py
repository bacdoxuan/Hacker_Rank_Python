"""https://www.hackerrank.com/challenges/most-commons/problem."""
from collections import Counter, OrderedDict


def find_most_common():
    """Note.

    Here there's a new concept of OrderedCounter, which combine Counter and
    OrderedDict
    """
    # Use of Counter and Orderdict
    # class OrderedCounter(Counter, OrderedDict):
    #     pass
    # [print(*c) for c in OrderedCounter(sorted(input())).most_common(3)]

    # Another way to do it
    data = sorted(input())
    od = OrderedDict()
    for i in data:
        if i in od:
            od[i] += 1
        else:
            od[i] = 1
    result = sorted(od.items(), key=lambda x: x[1], reverse=True)[: 3]
    for j in result:
        print(*j)


if __name__ == '__main__':
    find_most_common()
