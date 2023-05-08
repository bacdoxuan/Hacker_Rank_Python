"""https://www.hackerrank.com/challenges/np-arrays/problem."""
import numpy


def reverse_sorting(s):
    """using numpy array."""
    my_array = numpy.array(list(map(float, s.split())))
    print(my_array[::-1])


def main():
    """Main function."""
    s = input()
    reverse_sorting(s)


if __name__ == '__main__':
    main()
