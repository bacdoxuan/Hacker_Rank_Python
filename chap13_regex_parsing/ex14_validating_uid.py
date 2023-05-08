"""https://www.hackerrank.com/challenges/validating-uid/problem."""
import re


def check_uid(s):
    """Check if UID is correct format or not"""
    s = ''.join(sorted(s))
    if re.search(r'(.)\1', s):
        print('Invalid')
    elif re.search(r'\W', s):
        print('Invalid')
    elif len(s) != 10:
        print('Invalid')
    elif re.match(r'\d{3,}[A-Z]{2,}\w*', s):
        print('Valid')
    else:
        print('Invalid')


def main():
    for _ in range(int(input())):
        s = input()
        check_uid(s)


if __name__ == '__main__':
    main()
