if __name__ == '__main__':
    """
    Consider a list (list = []). You can perform the following commands:

    1 insert i e: Insert integer e at position i.
    2 print: Print the list.
    3 remove e: Delete the first occurrence of integer e.
    4 append e: Insert integer e at the end of the list.
    5 sort: Sort the list.
    6 pop: Pop the last element from the list.
    7 reverse: Reverse the list.

    Initialize your list and read in the value of n followed by n lines of 
    commands where each command will be of the types listed above.
    Iterate through each command in order and perform the corresponding
    operation on your list.
    """  # NOQA
    N = int(input())
    temp_list = []
    for _ in range(N):
        command = str(input())
        cmd = command.split()
        if cmd[0] == 'insert':
            temp_list.insert(int(cmd[1]), int(cmd[2]))
        if cmd[0] == 'print':
            print(temp_list)
        if cmd[0] == 'remove':
            temp_list.remove(int(cmd[1]))
        if cmd[0] == 'append':
            temp_list.append(int(cmd[1]))
        if cmd[0] == 'sort':
            temp_list.sort()
        if cmd[0] == 'pop':
            temp_list.pop()
        if cmd[0] == 'reverse':
            temp_list.reverse()
