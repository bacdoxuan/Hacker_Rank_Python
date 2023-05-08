"""https://www.hackerrank.com/challenges/itertools-combinations-with-replacement/problem."""  # NOQA
from itertools import combinations_with_replacement as cwr


def find_combinations_with_replacement():
    """https://www.hackerrank.com/challenges/itertools-combinations-with-replacement/problem."""  # NOQA
    data = list(input().split())
    result = []
    temp_result = list(cwr(data[0], int(data[1])))
    for i in temp_result:
        result.append(''.join(sorted(i)))
    for i in sorted(result):
        print(i)


if __name__ == '__main__':
    find_combinations_with_replacement()
