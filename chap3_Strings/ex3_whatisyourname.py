def print_full_name(a, b):
    """
    input first_name, last_name, then print with pattern:
    Hello first_name last_name! You just delved into python.
    """
    print("Hello {} {}! You just delved into python.".format(a, b))


if __name__ == '__main__':
    first_name = input()
    last_name = input()
    print_full_name(first_name, last_name)
