def split_and_join(line):
    """
    Turn abc to a-b-c, or hello to h-e-l-l-o
    """
    return '-'.join(line.split())


if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)
