"""
https://www.hackerrank.com/challenges/python-power-mod-power/problem
"""


def pow_math():
    """
    https://www.hackerrank.com/challenges/python-power-mod-power/problem
    """
    number_a, number_b, number_m = int(input()), int(input()), int(input())
    print(pow(number_a, number_b))
    print(pow(number_a, number_b, number_m))


if __name__ == '__main__':
    pow_math()
