def find_intersection():
    """
    Find the total number of elements in intersection set from set1, set2
    """
    n = int(input())  # NOQA
    set1 = set(input().split())
    m = int(input())  # NOQA
    set2 = set(input().split())
    print(len(set1 & set2))


if __name__ == '__main__':
    find_intersection()
