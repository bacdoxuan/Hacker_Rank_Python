def symmetric_different(m, list1, n, list2):
    """
    find the difference between to list and print in ascending order
    input:
    1 an integer m
    2 a list contains m integers
    3 an integer n
    4 a list contains n integers
    output:
    print the difference between 2 lists, each difference in one line, in
    ascending order
    """
    set1 = set(list1)
    set2 = set(list2)
    diff1 = set1.difference(set2)
    diff2 = set2.difference(set1)
    result = list(diff1) + list(diff2)
    result.sort()
    for n in result:
        print(n)


if __name__ == '__main__':
    m = int(input())
    list1 = list(map(int, input().split()))
    n = int(input())
    list2 = list(map(int, input().split()))
    symmetric_different(m, list1, n, list2)
