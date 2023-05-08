"""https://www.hackerrank.com/challenges/standardize-mobile-number-using-decorators/problem."""  # NOQA


def wrapper(func):
    """Format the input of function before sorting it."""
    def fun(l):
        temp = []
        for i in l:
            temp.append('+091' + ' ' + i[-10: -5] + ' ' + i[-5:])
        func(temp)
    return fun


@wrapper
def sort_phone(l):
    """Sort the input phone numbers after executing wrapper function."""
    print(*sorted(l), sep='\n')


if __name__ == '__main__':
    phone_list = [input() for _ in range(int(input()))]
    sort_phone(phone_list)
