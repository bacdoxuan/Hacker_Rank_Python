"""https://www.hackerrank.com/challenges/input/problem."""


def eval_function(k, polynomial):
    """https://www.hackerrank.com/challenges/input/problem."""
    if eval(polynomial) == k:
        print('True')
    else:
        print('False')


if __name__ == '__main__':
    x, k = map(int, input().split())
    polynomial = input()
    eval_function(k, polynomial)
