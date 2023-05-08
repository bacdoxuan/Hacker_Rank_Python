"""https://www.hackerrank.com/challenges/collections-counter/problem."""
from collections import Counter


def cal_money():
    """Find the money that shoes owner can earn.

    https://www.hackerrank.com/challenges/collections-counter/problem
    """
    money_earned = 0
    no_shoes = int(input())  # NOQA
    size_shoes = Counter(list(map(int, input().split())))
    no_customers = int(input())
    for _ in range(no_customers):
        input_data = list(map(int, input().split()))
        if size_shoes[input_data[0]]:
            money_earned += input_data[1]
            size_shoes[input_data[0]] -= 1
    print(money_earned)


if __name__ == '__main__':
    cal_money()
