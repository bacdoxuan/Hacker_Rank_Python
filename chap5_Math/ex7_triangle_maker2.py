"""
https://www.hackerrank.com/challenges/python-quest-1/problem
"""


def triangle_maker_2():
    """
    https://www.hackerrank.com/challenges/python-quest-1/problem
    Input:
    5
    Ouput:
    1
    22
    333
    4444
    """
    for i in range(1, int(input())):
        print(10 ** i // 9 * i)


if __name__ == '__main__':
    triangle_maker_2()
