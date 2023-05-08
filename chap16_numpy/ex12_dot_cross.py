import numpy


if __name__ == '__main__':
    n = int(input())
    list1 = [list(map(int, input().split())) for _ in range(n)]
    array1 = numpy.array(list1)
    list2 = [list(map(int, input().split())) for _ in range(n)]
    array2 = numpy.array(list2)
    print(numpy.dot(array1, array2))
