"""
https://www.hackerrank.com/challenges/validating-named-email-addresses/problem.
"""
import re


def email_validation(s):
    """Email validation.

    Each eail has 3 part:
    user name
    company name
    domain name
    """
    data = s.split()
    pattern = r'^[a-zA-Z][\w\-\.]*@[A-Za-z]+\.[a-zA-Z]{1,3}$'
    if bool(re.match(pattern, data[1][1:-1])):
        print(s)


if __name__ == '__main__':
    n = int(input())
    for _ in range(n):
        s = input()
        email_validation(s)
