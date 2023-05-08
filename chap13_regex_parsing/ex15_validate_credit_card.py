"""https://www.hackerrank.com/challenges/validating-credit-card-number/problem.
"""
import re


def check_creditcard(s):
    """check if an input is correct format."""
    if len(s) == 16 or len(s) == 19:
        if re.search(r'(\d)\1{3}|\s|\_', s):
            print('Invalid')
        elif re.search(r'(\d)\1-\1{2}', s):
            print('Invalid')
        elif re.match(r'[456]\d{3}(\-\d{4}){3}', s) or re.match(r'[456]\d{15}$', s):
            print('Valid')
        else:
            print('Invalid')
    else:
        print('Invalid')


def main():
    for _ in range(int(input())):
        s = input()
        check_creditcard(s)


if __name__ == '__main__':
    main()
