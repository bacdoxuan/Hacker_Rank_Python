def happiness_points(nm, set1, setA, setB):
    """
    Input:
    3 2 --> n = 3, m = 2
    1 5 3 --> list 1 with n integers number
    3 1 --> set A with m integers
    5 7 --> set B with m integers
    Ouput:
    if a number in list 1 in set A then happiness_points += 1
    if a number in list 1 in set B than happiness_points -= 1
    result = total happiness
    in example above:
    1, 3 in list 1 also in set A --> happiness_points = +2
    5 in list 1 also in set B --> happiness_points = -1
    --> total happiness_points = +2 -1 = 1
    """
    points = 0
    for i in set1:
        if i in setA:
            points += 1
        if i in setB:
            points -= 1
    return points


if __name__ == '__main__':
    nm = input().split()
    set1 = list(input().split())
    setA = set(input().split())
    setB = set(input().split())
    print(happiness_points(nm, set1, setA, setB))
