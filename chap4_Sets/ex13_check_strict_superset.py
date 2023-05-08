"""
https://www.hackerrank.com/challenges/py-check-strict-superset/problem
"""


def check_strict_superset():
    """
    Input Format:
    The first line contains the space separated elements of set A.
    The second line contains integer n, the number of other sets.
    The next n lines contains the space separated elements of the other sets
    Output:
    return True if A is a strict super set of all n sets, otherwise, print
    False.
    A strict superset has at least one element that does not exist in its
    subset.
    """
    set1 = set(input().split())
    n = int(input())
    print(all([set1 > set(input().split()) for _ in range(n)]))


if __name__ == '__main__':
    check_strict_superset()
