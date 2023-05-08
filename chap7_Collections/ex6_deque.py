"""https://www.hackerrank.com/challenges/py-collections-deque/problem."""
from collections import deque


def deque_functions():
    """https://www.hackerrank.com/challenges/py-collections-deque/problem."""
    n = int(input())
    dq = deque()
    for _ in range(n):
        command = input().split()
        if command[0] == 'append':
            dq.append(command[1])
        if command[0] == 'appendleft':
            dq.appendleft(command[1])
        if command[0] == 'pop':
            dq.pop()
        if command[0] == 'popleft':
            dq.popleft()
    print(*dq)


if __name__ == '__main__':
    deque_functions()
