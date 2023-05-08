from collections import OrderedDict


def merge_the_tools(str1, k):
    """
    Input:
    The first line contains a single string denoting s.
    The second line contains an integer, k, denoting the length of each subsegment.
    1 <= n <= 10^4, where n is length of s
    1 <= k <= n
    n is multiple of k

    Output:
    devide s into n/k subsegments, each subsegment has no repeated character

    Example:

    Input: 
    AABCAAADA
    3

    Output:
    AB
    CA
    AD
    """  # NOQA
    nosub = int(len(str1) / k)
    for i in range(nosub):
        print(''.join(OrderedDict.fromkeys(str1[i * k: i * k + k])))


if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
