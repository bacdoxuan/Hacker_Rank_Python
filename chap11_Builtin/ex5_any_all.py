"""https://www.hackerrank.com/challenges/any-or-all/problem."""


def check_condition():
    """https://www.hackerrank.com/challenges/any-or-all/problem."""
    n = int(input())
    ilist = list(map(int, input().split()))
    check_positive = all(i > 0 for i in ilist)
    check_palindrom = any(i for i in ilist if str(i) == str(i)[::-1])
    print(all([check_positive, check_palindrom]))


if __name__ == '__main__':
    check_condition()
