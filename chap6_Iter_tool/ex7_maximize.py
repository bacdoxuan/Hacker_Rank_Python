"""https://www.hackerrank.com/challenges/maximize-it/problem."""
import itertools


def find_max():
    """URL.

    https://www.hackerrank.com/challenges/maximize-it/problem
    """
    maxs = 0
    nk = input().split()
    n, k = int(nk[0]), int(nk[1])
    data = [list(map(int, input().split()))[1:] for _ in range(n)]
    prod = itertools.product(*data)
    try:
        while True:
            nxt = next(prod)
            s = sum(i**2 for i in nxt) % k
            if s > maxs:
                maxs = s
                # print(nxt)
    except Exception:
        pass
    finally:
        print(maxs)


if __name__ == '__main__':
    find_max()
