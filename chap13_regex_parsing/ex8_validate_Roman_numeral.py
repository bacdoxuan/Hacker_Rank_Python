"""https://www.hackerrank.com/challenges/validate-a-roman-number/problem."""


def check_roman_numeral(s):
    """check how to construct a Roman numeral.

    http://www.diveintopython.net/regular_expressions/roman_numerals.html."""
    import re
    pattern = r'^(?=[MDCLXVI])M{0,3}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$'
    print(bool(re.match(pattern, s)))


if __name__ == "__main__":
    s = input()
    check_roman_numeral(s)
