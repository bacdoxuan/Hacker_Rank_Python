def set_mutation():
    """
    Input:
    The first line contains the number of elements in set A.
    The second line contains the space separated list of elements in set A.
    The third line contains integer N, the number of other sets.
    The next 2 * N lines are divided into parts containing two lines each.
    The first line of each part contains the space separated entries of the operation name and the length of the other set.
    The second line of each part contains space separated list of elements in the other set.

    Output:
    Output the sum of elements in set A.

    Example:

    Input:
     16
     1 2 3 4 5 6 7 8 9 10 11 12 13 14 24 52
     4
     intersection_update 10
     2 3 5 6 8 9 1 4 7 11
     update 2
     55 66
     symmetric_difference_update 5
     22 7 35 62 58
     difference_update 7
     11 22 35 55 58 62 66

    Output:
    38
    """  # NOQA
    n = int(input())
    setA = set(map(int, input().split()))
    m = int(input())
    for _ in range(m):
        command = list(input().split())
        setB = set(map(int, input().split()))
        if command[0] == 'update':
            setA.update(setB)
        if command[0] == 'intersection_update':
            setA.intersection_update(setB)
        if command[0] == 'difference_update':
            setA.difference_update(setB)
        if command[0] == 'symmetric_difference_update':
            setA.symmetric_difference_update(setB)
    print(sum(setA))


if __name__ == '__main__':
    """
    .update() or |=
    Update the set by adding elements from an iterable/another set.

    >>> H = set("Hacker")
    >>> R = set("Rank")
    >>> H.update(R)
    >>> print H
    set(['a', 'c', 'e', 'H', 'k', 'n', 'r', 'R'])

    .intersection_update() or &=
    Update the set by keeping only the elements found in it and an iterable/another set.

    >>> H = set("Hacker")
    >>> R = set("Rank")
    >>> H.intersection_update(R)
    >>> print H
    set(['a', 'k'])

    .difference_update() or -=
    Update the set by removing elements found in an iterable/another set.

    >>> H = set("Hacker")
    >>> R = set("Rank")
    >>> H.difference_update(R)
    >>> print H
    set(['c', 'e', 'H', 'r'])

    .symmetric_difference_update() or ^=
    Update the set by only keeping the elements found in either set, but not in both.

    >>> H = set("Hacker")
    >>> R = set("Rank")
    >>> H.symmetric_difference_update(R)
    >>> print H
    set(['c', 'e', 'H', 'n', 'r', 'R'])
    """  # NOQA
    set_mutation()
