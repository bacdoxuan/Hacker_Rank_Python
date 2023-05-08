""".

https://www.hackerrank.com/challenges/itertools-permutations/problem
"""
import itertools


def find_permutation():
    """.

    https://www.hackerrank.com/challenges/itertools-permutations/problem
    """
    data = list(input().split())
    tmp_result = list(itertools.permutations(data[0], int(data[1])))
    result = []
    for i in tmp_result:
        result.append(''.join(i))
    for i in sorted(result):
        print(i)


if __name__ == '__main__':
    find_permutation()
