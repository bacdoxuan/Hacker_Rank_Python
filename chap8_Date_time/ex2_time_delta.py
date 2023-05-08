"""https://www.hackerrank.com/challenges/python-time-delta/problem."""
from datetime import datetime as dt
from dateutil import parser


def find_time_diff_seconds():
    """https://www.hackerrank.com/challenges/python-time-delta/problem.

    Sample Input 0
    2
    Sun 10 May 2015 13:54:36 -0700
    Sun 10 May 2015 13:54:36 -0000
    Sat 02 May 2015 19:54:36 +0530
    Fri 01 May 2015 13:54:36 -0000

    Sample Output 0

    25200
    88200
    """

    # Solution 1, use datetime module
    fmt = '%a %d %b %Y %H:%M:%S %z'
    for i in range(int(input())):
        print(int(abs((dt.strptime(input(), fmt) -
                       dt.strptime(input(), fmt)).total_seconds())))
    # Solution 2, use dateutil module
    for _ in range(int(input())):
        d1 = parser.parse(input().strip())
        d2 = parser.parse(input().strip())
        print(abs(int((d2 - d1).total_seconds())))


if __name__ == '__main__':
    find_time_diff_seconds()
