def print_formatted(number):
    """
    Input Format:
    A single integer denoting n.
    Example: 17
    Output:
    decimal, octal, capitalized hexadecimal, and binary values of i for i
    range form 1 to 17
    1     1     1     1
    2     2     2    10
    3     3     3    11
    4     4     4   100
    5     5     5   101
    6     6     6   110
    7     7     7   111
    8    10     8  1000
    9    11     9  1001
   10    12     A  1010
   11    13     B  1011
   12    14     C  1100
   13    15     D  1101
   14    16     E  1110
   15    17     F  1111
   16    20    10 10000
   17    21    11 10001
    """
    w = len(bin(number)) - 1  # NOQA
    for i in range(1, number + 1):
        print('{}{}{}{}'.format(str(i).rjust(w - 1, ' '), str(oct(i))[2:].rjust(w, ' '), str(hex(i))[2:].upper().rjust(w, ' '), str(bin(i))[2:].rjust(w, ' ')))  # NOQA


if __name__ == '__main__':
    n = int(input())
    print_formatted(n)