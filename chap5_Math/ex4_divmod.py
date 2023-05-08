"""https://www.hackerrank.com/challenges/python-mod-divmod/problem."""


def cal_divmod():
    """https://www.hackerrank.com/challenges/python-mod-divmod/problem."""
    number_a = int(input())
    number_b = int(input())
    print(number_a // number_b)
    print(number_a % number_b)
    print(divmod(number_a, number_b))


if __name__ == '__main__':
    cal_divmod()
