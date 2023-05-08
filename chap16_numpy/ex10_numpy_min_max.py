"""https://www.hackerrank.com/challenges/np-min-and-max/problem."""
import numpy


if __name__ == '__main__':
    n, m = map(int, input().split())
    list1 = [list(map(int, input().split())) for _ in range(n)]
    array1 = numpy.array(list1)
    min_axis1 = numpy.min(array1, axis=1)
    print(numpy.max(min_axis1))
