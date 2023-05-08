"""
https://www.hackerrank.com/challenges/find-angle/problem
"""

import math


def find_angle():
    """
    https://www.hackerrank.com/challenges/find-angle/problem

    References:
    https://www.mathsisfun.com/algebra/trig-solving-sss-triangles.html
    https://www.toaniq.com/chung-minh-tinh-chat-duong-trung-tuyen-cua-tam-giac-vuong/
    http://www.teacherschoice.com.au/Maths_Library/Trigonometry/solve_trig_AAS.htm
    """  # NOQA
    AB = float(input())
    BC = float(input())
    AC = math.sqrt(AB**2 + BC**2)
    cos_C = (AC**2 + BC**2 - AB**2) / (2 * AC * BC)
    print('{}{}'.format(round(math.degrees(math.acos(cos_C))), '°'))


if __name__ == '__main__':
    find_angle()
