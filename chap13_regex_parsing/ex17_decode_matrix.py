"""https://www.hackerrank.com/challenges/matrix-script/problem."""
import re


def main():
    matrix = []
    st = ''
    row, col = map(int, input().split())

    for i in range(row):
        s = input()
        matrix.append(s)

    for i in range(col):
        for j in matrix:
            st += j[i]

    pattern = r'(?<=\w)(\W+)(?=\w)'
    print(re.sub(pattern, ' ', st))


if __name__ == '__main__':
    main()
