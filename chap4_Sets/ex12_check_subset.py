"""
https://www.hackerrank.com/challenges/py-check-subset/problem
"""


def check_subset():
    """
    Input:
    first line: n = number of test cases
    each test case:
    first line: n numbers of
    """
    for i in range(int(input())):
        a = int(input())
        A = set(input().split())
        b = int(input())
        B = set(input().split())
        print(A.issubset(B))


if __name__ == '__main__':
    check_subset()
