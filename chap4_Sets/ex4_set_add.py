def unique_countries():
    """
    count the number of unique countries from user's input

    Input:
    7
    UK
    China
    USA
    France
    New Zealand
    UK
    France

    Output:
    5
    UK and France repeat twice. Hence, the total number of distinct
    country stamps is 5
    """
    n = int(input())
    set1 = set()
    for _ in range(n):
        set1.add(input())
    print(len(set1))


if __name__ == '__main__':
    unique_countries()
