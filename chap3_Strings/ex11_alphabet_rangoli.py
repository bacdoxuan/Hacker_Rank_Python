import string


def print_rangoli(size):
    """
    input an integer n, 0 < n < 27.
    output is a pattern like these:
    n = 3
    ----c----
    --c-b-c--
    c-b-a-b-c
    --c-b-c--
    ----c----

    n = 5
    --------e--------
    ------e-d-e------
    ----e-d-c-d-e----
    --e-d-c-b-c-d-e--
    e-d-c-b-a-b-c-d-e
    --e-d-c-b-c-d-e--
    ----e-d-c-d-e----
    ------e-d-e------
    --------e--------

    n = 10
    ------------------j------------------
    ----------------j-i-j----------------
    --------------j-i-h-i-j--------------
    ------------j-i-h-g-h-i-j------------
    ----------j-i-h-g-f-g-h-i-j----------
    --------j-i-h-g-f-e-f-g-h-i-j--------
    ------j-i-h-g-f-e-d-e-f-g-h-i-j------
    ----j-i-h-g-f-e-d-c-d-e-f-g-h-i-j----
    --j-i-h-g-f-e-d-c-b-c-d-e-f-g-h-i-j--
    j-i-h-g-f-e-d-c-b-a-b-c-d-e-f-g-h-i-j
    --j-i-h-g-f-e-d-c-b-c-d-e-f-g-h-i-j--
    ----j-i-h-g-f-e-d-c-d-e-f-g-h-i-j----
    ------j-i-h-g-f-e-d-e-f-g-h-i-j------
    --------j-i-h-g-f-e-f-g-h-i-j--------
    ----------j-i-h-g-f-g-h-i-j----------
    ------------j-i-h-g-h-i-j------------
    --------------j-i-h-i-j--------------
    ----------------j-i-j----------------
    ------------------j------------------
    """
    chars = string.ascii_lowercase
    n = size
    if n == 1:
        print('a')
    else:
        for i in range(n - 1, 0, -1):
            print('-' * i * 2 + '-'.join(chars[(n-1):(i-1):-1]) + ''.join(['-' + j for j in chars[(i+1):n]]) + '-' * i *2)
        print('-'.join(chars[(n-1):0:-1]) + '-' + chars[0] + '-' + '-'.join(chars[1:n]))
        for i in range(1, n):
            print('-' * i * 2 + '-'.join(chars[(n-1):(i-1):-1]) + ''.join(['-' + j for j in chars[(i+1):n]]) + '-' * i *2)

    # Another way to do it
    alpha = string.ascii_lowercase
    n = size
    L = []
    for i in range(n):
        s = "-".join(alpha[i:n])
        L.append((s[::-1]+s[1:]).center(4*n-3, "-"))
    print('\n'.join(L[:0:-1]+L))


if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
