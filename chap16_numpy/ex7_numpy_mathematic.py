"""https://www.hackerrank.com/challenges/np-array-mathematics/problem."""
import numpy


if __name__ == '__main__':
    n, m = map(int, input().split())
    list_a = [list(map(int, input().split())) for _ in range(n)]
    list_b = [list(map(int, input().split())) for _ in range(n)]
    array_a = numpy.array(list_a)
    array_b = numpy.array(list_b)
    print(array_a + array_b)
    print(array_a - array_b)
    print(array_a * array_b)
    print(array_a // array_b)
    print(array_a % array_b)
    print(array_a ** array_b)
