def minion_game(s):
    """
    Both players are given the same string, S.
    Both players have to make substrings using the letters of the string S.
    Stuart has to make words starting with consonants.
    Kevin has to make words starting with vowels.
    The game ends when both players have made all possible substrings.
    vowels contains: AEIOUaeiou
    Output:
    Print one line: the name of the winner and their score separated by a space.
    If the game is a draw, print Draw.
    """  # NOQA
    vowels = 'AEIOUaeiou'

    kevsc = 0
    stusc = 0
    for i in range(len(s)):
        if s[i] in vowels:
            kevsc += (len(s)-i)
        else:
            stusc += (len(s)-i)

    if kevsc > stusc:
        print("Kevin", kevsc)
    elif kevsc < stusc:
        print("Stuart", stusc)
    else:
        print("Draw")


if __name__ == '__main__':
    s = input()
    minion_game(s)
