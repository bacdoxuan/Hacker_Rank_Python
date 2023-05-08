"""https://www.hackerrank.com/challenges/re-findall-re-finditer/problem."""
import re


def find_substring(s):
    """Have to use positive look behind so it does not consume the characters."""
    pattern = r'(?<=[qwrtypsdfghjklzxcvbnm])([aeiou]{2,})([qwrtypsdfghjklzxcvbnm])'
    # positive look behind: ?<=[...], check more on https://regex101.com/
    result = re.findall(pattern, s, flags=re.I)  # flags=re.I to IGNORECASE
    if result:
        for i in result:
            print(i[0])
    else:
        print(-1)


if __name__ == '__main__':
    s = input()
    find_substring(s)
