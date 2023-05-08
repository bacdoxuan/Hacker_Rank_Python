"""Find sub string."""


def count_substring(string, sub_string):
    """
    Enter a string.
    Each character in the string is an ascii character.
    Enter a sub_string.
    Count the number of time that sub_string appears in the string.
    """
    lss = len(sub_string)
    ls = len(string)
    count = 0
    for i in range(ls - lss + 1):
        if string[i: i + lss] == sub_string:
            count += 1
    return count


if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    count = count_substring(string, sub_string)
    print(count)
