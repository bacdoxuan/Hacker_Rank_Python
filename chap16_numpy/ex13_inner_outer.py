"""https://www.hackerrank.com/challenges/np-inner-and-outer/problem."""
import numpy


if __name__ == '__main__':
    list1 = list(map(int, input().split()))
    array1 = numpy.array(list1)
    list2 = list(map(int, input().split()))
    array2 = numpy.array(list2)
    print(numpy.inner(array1, array2))
    print(numpy.outer(array1, array2))
