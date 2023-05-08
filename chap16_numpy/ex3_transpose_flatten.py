"""https://www.hackerrank.com/challenges/np-transpose-and-flatten/problem."""
import numpy


if __name__ == '__main__':
    row, col = map(int, input().split())
    my_list = [list(map(int, input().split())) for _ in range(row)]
    my_array = numpy.array(my_list)
    print(my_array.transpose())
    print(my_array.flatten())
