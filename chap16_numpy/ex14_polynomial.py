"""https://www.hackerrank.com/challenges/np-polynomials/problem."""
import numpy as np

"""
np.poly: Find coefficients by an array of roots
np.root: Find the root with an array of coefficients of polynomial

np.polyint: returns an antiderivative (indefinite integral) of a polynomial
np.polyder: returns the derivative of the specified order of a polynomial
(Check more with https://en.wikipedia.org/wiki/Antiderivative)

np.polyval: calculate the value of polynomial at point x (x is a specific value)

np.popolyfit
"""


def calculate_polynomial_at_point_x():
    """Use polyval to find the result."""
    input_list = list(map(float, input().split()))
    point_x = float(input())

    print(np.polyval(input_list, point_x))


if __name__ == '__main__':
    calculate_polynomial_at_point_x()
