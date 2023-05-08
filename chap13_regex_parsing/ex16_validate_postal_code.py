"""https://www.hackerrank.com/challenges/validating-postalcode/problem."""
import re


def wrong_conditions(s):
    s = str(s)
    con1 = s.startswith('0')
    con2 = len(s) != 6
    con3 = bool(re.search(r'(\d\d)\1', s))
    con4 = (s[0] == s[2] and s[3] == s[5])
    con5 = (s[0] == s[2] and s[2] == s[4])
    con6 = (s[1] == s[3] and s[3] == s[5])
    return (con1 or con2 or con3 or con4 or con5 or con6)


def check_postal_code(s):
    try:
        result = wrong_conditions(s)
    except Exception:
        result = True
    return result


def main():
    s = input()
    if check_postal_code(s):
        print('False')
    else:
        print('True')


if __name__ == '__main__':
    main()
