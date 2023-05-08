def set_operations():
    """
    Input:
    1. input integer n, the number of element
    2. input n integers of set s, space separated.
    3. input integer m, the number of commands
    4. The next m lines input either pop, remove, discard command with associated value
    Output:
    The final result after applying m commands on set s.
    """  # NOQA
    n = int(input())
    s = set(map(int, input().split()))
    m = int(input())
    for _ in range(m):
        command = list(input().split())
        try:
            if command[0] == 'pop':
                s.pop()
            if command[0] == 'remove':
                s.remove(int(command[1]))
            if command[0] == 'discard':
                s.discard(int(command[1]))
        except Exception:
            pass
    print(sum(s))


if __name__ == '__main__':
    set_operations()
