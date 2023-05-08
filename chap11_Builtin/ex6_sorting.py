"""https://www.hackerrank.com/challenges/ginorts/problem."""


def sorting_string(st):
    """https://www.hackerrank.com/challenges/ginorts/problem."""
    result = sorted(st, key=lambda x: (x.isdigit() and int(x) % 2 == 0,
                                       x.isdigit(), x.isupper(),
                                       x.islower(), x))
    print(*result, sep='')


if __name__ == '__main__':
    st = input()
    sorting_string(st)
