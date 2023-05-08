"""
https://www.hackerrank.com/challenges/triangle-quest-2/problem
"""


def print_triangle():
    """
    print the triangle like this:
    n = 5
    result:
    1
    121
    12321
    1234321
    123454321

    Solution:
    1 = 1 * 1 = (10^1 // 9) * (10^1 // 9)
    121 = 11 * 11 = (10^2 // 9) * (10^2 // 9)
    12321 = 111 * 111 = (10^3 // 9) * (10^3 // 9)
    1234321 = 1111 * 1111 = (10^4 // 9) * (10^4 // 9)
    123454321 = 11111 * 11111 = (10^5 // 9) * (10^5 // 9)
    --> with i: (10**i//9)**2
    """
    for i in range(0, int(input())+1):
        print((10**i//9)**2)


if __name__ == '__main__':
    print_triangle()
