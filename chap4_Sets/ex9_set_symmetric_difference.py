def find_symmetric_difference():
    """
    Find the total number of elements in symmetric_difference set from set1, set2
    """  # NOQA
    n = int(input())  # NOQA
    set1 = set(input().split())
    m = int(input())  # NOQA
    set2 = set(input().split())
    print(len(set1 ^ set2))


if __name__ == '__main__':
    find_symmetric_difference()
