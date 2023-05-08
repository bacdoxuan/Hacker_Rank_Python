if __name__ == '__main__':
    """
    desgin a pattern like this:
    input: N, M = N * 3. N is an odd integer number
    Example:
    N, M = 9, 27
    Output:
    ------------.|.------------
    ---------.|..|..|.---------
    ------.|..|..|..|..|.------
    ---.|..|..|..|..|..|..|.---
    ----------WELCOME----------
    ---.|..|..|..|..|..|..|.---
    ------.|..|..|..|..|.------
    ---------.|..|..|.---------
    ------------.|.------------

    N, M = 5, 15
    Output:
    ------.|.------
    ---.|..|..|.---
    ----WELCOME----
    ---.|..|..|.---
    ------.|.------
    """
    N, M = map(int, input().split())
    for i in range(1, N, 2):
        print('-'*int((M - i*3)*0.5) + '.|.'*i + '-'*int((M - i*3)*0.5))
    print('-'*int((M-7)*0.5) + 'WELCOME' + '-'*int((M-7)*0.5))
    for i in range(N-2, -1, -2):
        print('-'*int((M - i*3)*0.5) + '.|.'*i + '-'*int((M - i*3)*0.5))

    # Another way to do it
    for i in range(1, N, 2):
        print(('.|.' * i).center(M, '-'))
    print('WELCOME'.center(M, '-'))
    for i in range(N-2, -1, -2):
        print(('.|.' * i).center(M, '-'))
