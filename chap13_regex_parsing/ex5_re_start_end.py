"""https://www.hackerrank.com/challenges/re-start-re-end/problem."""
import re


def find_substring(s, k):
    """Use re.star and re.end to find start and end index of a substring."""
    found = False
    for i in range(len(s)):
        result = re.search(k, s[i: i + len(k)])
        if result:
            print((result.start() + i, result.end() + i - 1))
            found = True
    if not found:
        print((-1, -1))


if __name__ == '__main__':
    s = input()
    k = input()
    find_substring(s, k)
