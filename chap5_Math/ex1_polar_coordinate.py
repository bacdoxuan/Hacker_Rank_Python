"""
https://www.hackerrank.com/challenges/polar-coordinates/problem
"""

import cmath


def find_polar_coordinate():
    """
    Input: a complex number x + jy
    Output: the polar coordinate of the input complex number

    Example:
    Input: 1 + 2j
    Output: should be correct up to 3 decimal places
    2.236
    1.107
    """
    complex_number = complex(input())
    polar_coordinate = cmath.polar(complex_number)
    for i in polar_coordinate:
        print('%.3f' % i)


if __name__ == '__main__':
    find_polar_coordinate()
