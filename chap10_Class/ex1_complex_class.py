"""https://www.hackerrank.com/challenges/class-1-dealing-with-complex-numbers/problem."""
import math


class Complex(object):
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def __add__(self, other):
        c = self.real
        d = self.imaginary
        a = other.real
        b = other.imaginary
        return Complex(c + a, d + b)

    def __sub__(self, other):
        c = self.real
        d = self.imaginary
        a = other.real
        b = other.imaginary
        return Complex(c - a, d - b)

    def __mul__(self, other):
        c = self.real
        d = self.imaginary
        a = other.real
        b = other.imaginary
        return Complex(c * a - d * b, c * b + a * d)

    def __truediv__(self, other):
        c = self.real
        d = self.imaginary
        a = other.real
        b = other.imaginary
        div_real = (a * c + b * d)/(a**2 + b**2)
        div_imaginary = (a * d - b * c)/(a**2 + b**2)
        return Complex(div_real, div_imaginary)

    def mod(self):
        c = self.real
        d = self.imaginary
        return Complex(math.sqrt(c**2 + d**2), 0)

    def __str__(self):
        if self.imaginary == 0:
            result = "%.2f+0.00i" % (self.real)
        elif self.real == 0:
            if self.imaginary >= 0:
                result = "0.00+%.2fi" % (self.imaginary)
            else:
                result = "0.00-%.2fi" % (abs(self.imaginary))
        elif self.imaginary > 0:
            result = "%.2f+%.2fi" % (self.real, self.imaginary)
        else:
            result = "%.2f-%.2fi" % (self.real, abs(self.imaginary))
        return result


if __name__ == '__main__':
    c = map(float, input().split())
    d = map(float, input().split())
    x = Complex(*c)
    y = Complex(*d)
    print(*map(str, [x+y, x-y, x*y, x/y, x.mod(), y.mod()]), sep='\n')
