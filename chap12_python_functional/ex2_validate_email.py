"""https://www.hackerrank.com/challenges/validate-list-of-email-address-with-filter/problem."""  # NOQA
import re


def validate(s):
    """A valid email address.

    It must have the username@websitename.extension format type.
    The username can only contain letters, digits, dashes and underscores.
    The website name can only have letters and digits.
    The maximum length of the extension is 3.
    """

    # Solution 1: Using regular expression
    pattern = r'[a-zA-Z0-9_-]+@[a-zA-Z0-9]+\.[a-zA-Z]{1,3}$'
    result = re.match(pattern, s)
    if result:
        return True
    else:
        return False

    # Solution 2: using string method, longer code
    # ...


def filter_mail(emails):
    return list(filter(validate, emails))


if __name__ == '__main__':
    n = int(input())
    emails = []
    for _ in range(n):
        emails.append(input())

    filtered_emails = filter_mail(emails)
    filtered_emails.sort()
    print(filtered_emails)
