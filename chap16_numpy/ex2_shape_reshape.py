"""https://www.hackerrank.com/challenges/np-shape-reshape/problem."""
import numpy


if __name__ == '__main__':
    s = list(map(int, input().split()))
    my_array = numpy.array(s)
    print(numpy.reshape(s, (3, 3)))
