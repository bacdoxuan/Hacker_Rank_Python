"""https://www.hackerrank.com/challenges/np-concatenate/problem."""
import numpy


if __name__ == '__main__':
    n, m, p = map(int, input().split())
    list1 = [list(map(int, input().split())) for _ in range(n)]
    array1 = numpy.array(list1)
    list2 = [list(map(int, input().split())) for _ in range(m)]
    array2 = numpy.array(list2)
    print(numpy.concatenate((array1, array2)))
