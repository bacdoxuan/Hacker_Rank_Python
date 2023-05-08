"""https://www.hackerrank.com/challenges/np-mean-var-and-std/problem."""
import numpy


if __name__ == '__main__':
    n, m = map(int, input().split())
    list1 = [list(map(int, input().split())) for _ in range(n)]
    array1 = numpy.array(list1)
    print(numpy.mean(array1, axis=1))
    print(numpy.var(array1, axis=0))
    print(numpy.std(array1))
