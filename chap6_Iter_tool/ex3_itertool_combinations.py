"""https://www.hackerrank.com/challenges/itertools-combinations/problem."""
from itertools import combinations


def find_combinations():
    """https://www.hackerrank.com/challenges/itertools-combinations/problem."""
    data = list(input().split())
    for i in range(1, int(data[1]) + 1):
        result = []
        temp_result = list(combinations(data[0], i))
        for j in temp_result:
            result.append(''.join(sorted(j)))
        for k in sorted(result):
            print(k)


if __name__ == '__main__':
    find_combinations()
