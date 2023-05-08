if __name__ == '__main__':
    """
    Input a string S
    Output:
    1 In the first line, print True if S has any alphanumeric characters. Otherwise, print False.
    2 In the second line, print True if S has any alphabetical characters. Otherwise, print False.
    3 In the third line, print True if S has any digits. Otherwise, print False.
    4 In the fourth line, print True if S has any lowercase characters. Otherwise, print False.
    5 In the fifth line, print True if S has any uppercase characters. Otherwise, print False. 
    """  # NOQA
    s = input()
    print(any(char.isalnum() for char in s))
    print(any(char.isalpha() for char in s))
    print(any(char.isdigit() for char in s))
    print(any(char.islower() for char in s))
    print(any(char.isupper() for char in s))
