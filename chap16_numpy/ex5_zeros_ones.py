"""https://www.hackerrank.com/challenges/np-zeros-and-ones/problem."""
import numpy


if __name__ == '__main__':
    dimension = tuple(map(int, input().split()))
    print(numpy.zeros(dimension, dtype=numpy.int))
    print(numpy.ones(dimension, dtype=numpy.int))
