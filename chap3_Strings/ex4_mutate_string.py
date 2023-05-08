def mutate_string(string, position, character):
    """
    Input a string, an integer number and a character
    replace the character with position = number in the string
    by the input character
    """
    return ''.join([string[:position], character, string[position + 1:]])


if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)
