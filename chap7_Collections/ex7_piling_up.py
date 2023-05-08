"""https://www.hackerrank.com/challenges/piling-up/problem."""
from collections import deque


def validation():
    """https://www.hackerrank.com/challenges/piling-up/problem."""
    result = []
    no_testcases = int(input())
    for _ in range(no_testcases):
        dq = deque()
        n = int(input())
        dq.extend(list(map(int, input().split())))
        length_dq = len(dq)
        while length_dq > 1:
            max_dq = max(dq[0], dq[1], dq[-2], dq[-1])
            if dq[0] == max_dq:
                dq.popleft()
                length_dq -= 1
            elif dq[-1] == max_dq:
                dq.pop()
                length_dq -= 1
            else:
                break

        if length_dq == 1:
            result.append('Yes')
        else:
            result.append('No')

    for i in result:
            print(i)


if __name__ == '__main__':
    validation()
