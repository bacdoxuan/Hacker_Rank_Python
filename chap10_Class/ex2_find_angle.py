""".

https://www.hackerrank.com/challenges/class-2-find-the-torsional-angle/problem
"""
from math import degrees, acos


class Point(object):
    def __init__(self, x, y=None, z=None):
        if type(x) is list:
            self.x = x[0]
            self.y = x[1]
            self.z = x[2]
        else:
            self.x = x
            self.y = y
            self.z = z

    def __sub__(self, no):
        return Point(self.x - no.x, self.y - no.y, self.z - no.z)

    def dot(self, no):
        return (self.x * no.x) + (self.y * no.y) + (self.z * no.z)

    def cross(self, no):
        return Point((self.y*no.z) - (self.z*no.y), (self.z*no.x) - (self.x*no.z), (self.x*no.y) - (self.y*no.x))

    def absolute(self):
        return pow((self.x ** 2 + self.y ** 2 + self.z ** 2), 0.5)

    def __str__(self):
        return str(self.x) + ', ' + str(self.y) + ', ' + str(self.z)


def find_angle():
    """Find the angle in 3D dimension."""
    A = Point(list(map(float, input().split(' '))))
    B = Point(list(map(float, input().split(' '))))
    C = Point(list(map(float, input().split(' '))))
    D = Point(list(map(float, input().split(' '))))

    X = (B - A).cross(C - B)
    Y = (C - B).cross(D - C)

    phi = round(degrees(acos(X.dot(Y) / (X.absolute() * Y.absolute()))), 2)
    print(phi)


if __name__ == '__main__':
    find_angle()
