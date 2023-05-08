def capitalize(string):
    """
    Input: hello world, 12abc
    Output: Hello World, 12abc
    """
    string = ' ' + string
    st = [char for char in string]
    try:
        for i in range(len(st)):
            if st[i] == ' ':
                st[i + 1] = st[i + 1].upper()
    except Exception:
        pass
    st.pop(0)
    return ''.join(st)


if __name__ == '__main__':
    string = input()
    capitalized_string = capitalize(string)
    print(capitalized_string)
