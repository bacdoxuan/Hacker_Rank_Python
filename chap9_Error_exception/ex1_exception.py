"""https://www.hackerrank.com/challenges/exceptions/problem."""


def catch_exceptions():
    """https://www.hackerrank.com/challenges/exceptions/problem."""
    for _ in range(int(input())):
        try:
            a, b = map(int, input().split())
            print(a // b)
        except Exception as e:
            print('Error Code:', e)


if __name__ == '__main__':
    catch_exceptions()
