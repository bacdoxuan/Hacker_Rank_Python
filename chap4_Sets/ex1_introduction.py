import statistics


def average(array):
    """
    a simple example to calculate the average number of an array
    """
    return statistics.mean(set(array))


if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)
