"""https://www.hackerrank.com/challenges/np-sum-and-prod/problem."""
import numpy


if __name__ == '__main__':
    n, m = map(int, input().split())
    list1 = [list(map(int, input().split())) for _ in range(n)]
    array1 = numpy.array(list1)
    sum_array1 = numpy.sum(array1, axis=0)
    print(numpy.product(sum_array1))
