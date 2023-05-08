"""https://www.hackerrank.com/challenges/defaultdict-tutorial/problem."""
from collections import defaultdict


def find_index():
    """https://www.hackerrank.com/challenges/defaultdict-tutorial/problem."""
    groupa = defaultdict(list)
    groupb = defaultdict(list)
    n, m = map(int, input().split())

    for _ in range(n):
        groupa['chars'].append(input())
    for _ in range(m):
        groupb['chars'].append(input())

    for charb in groupb['chars']:
        if charb in groupa['chars']:
            result = []
            for i in range(len(groupa['chars'])):
                if groupa['chars'][i] == charb:
                    result.append(i + 1)
            print(*result)
        else:
            print(-1)


if __name__ == '__main__':
    find_index()
