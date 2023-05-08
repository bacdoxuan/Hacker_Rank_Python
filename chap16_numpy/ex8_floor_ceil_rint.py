"""https://www.hackerrank.com/challenges/floor-ceil-and-rint/problem."""
import numpy


if __name__ == '__main__':
    list1 = list(map(float, input().split()))
    array1 = numpy.array(list1)
    print(numpy.floor(array1))
    print(numpy.ceil(array1))
    print(numpy.rint(array1))
