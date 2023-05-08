"""https://www.hackerrank.com/challenges/map-and-lambda-expression/problem."""


def fibonacci(n):
    """Return a list of first n fibonacci numbers."""
    if n == 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        a, b = 0, 1
        fibo_list = [0, 1]
        for _ in range(n - 2):
            a, b = b, a + b
            fibo_list.append(b)
        return fibo_list


cube = lambda x: [i**3 for i in x if x]


if __name__ == '__main__':
    n = int(input())
    print(cube(fibonacci(n)))
