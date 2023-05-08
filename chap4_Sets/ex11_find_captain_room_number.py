def find_captain_room_number():
    """
    Input:
    n : number of members per group
    list1: a list contains rooms' number of members and captain room number.

    each room number repeat n times, except the captain room number.
    --> captain room number repeat less then (n-1) times compare to other
    room numbers

    let's call captain room number = c, repeat only 1 time.
    other rooms is l1, l2, ... lk, each room will repeat n times with the above conditions.

    --> set(list1) = {l1, l2, ..., lk, c} is known
    so, we can can calculate sum(set1)*n == (l1 + l2 + ... + lk + c) * n
    we can alse calculate sum(list1) = (l1 + l2 + ... + lk) * n + c
    here, due to:
    (l1 + l2 + ... + lk) * n + c == (l1 + l2 + ... + lk + c) * n - (n-1)*c
                   |                             |
                   V                             V
                sum(list1)                    sum(set1)*n
    --> sum(list1) == sum(set1)*n - (n-1)*c
    --> c = (sum(set1)*n - sum(list1)) / (n-1)
    """  # NOQA
    n = int(input())
    list1 = list(map(int, input().split()))
    set1 = set(list1)
    captain_room_numer = int((sum(set1) * n - sum(list1)) / (n - 1))
    print(captain_room_numer)


if __name__ == '__main__':
    find_captain_room_number()
