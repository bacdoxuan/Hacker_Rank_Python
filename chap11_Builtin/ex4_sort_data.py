"""https://www.hackerrank.com/domains/python/py-built-ins."""


def sort_lambda():
    """https://www.hackerrank.com/domains/python/py-built-ins."""
    no_lines, no_elements = map(int, input().split())
    total = []
    for _ in range(no_lines):
        total.append(list(map(int, input().split())))
    kth = int(input())
    result = sorted(total, key=lambda x: x[kth])
    for i in result:
        print(*i)


if __name__ == '__main__':
    sort_lambda()
