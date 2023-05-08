if __name__ == '__main__':
    """
    find the second largest number in a list then print it
    """
    n = int(input())
    arr = map(int, input().split())
    result = list(arr)
    max_value = max(result)
    while max(result) == max_value:
        result.remove(max_value)
    print(max(result))
