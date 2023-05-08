if __name__ == '__main__':
    """
    Input Format:
    The first line contains an integer, n , denoting the number of elements in the tuple.
    The second line contains n space-separated integers describing the elements in tuple t.

    Output Format:
    Print the result of hash(t)
    """  # NOQA
    n = int(input())
    integer_list = map(int, input().split())
    print(hash(tuple(integer_list)))
