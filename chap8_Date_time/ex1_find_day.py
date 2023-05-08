"""https://www.hackerrank.com/challenges/calendar-module/problem."""
from datetime import date
from calendar import day_name, weekday


def find_day_name(m, d, y):
    """https://www.hackerrank.com/challenges/calendar-module/problem."""
    # Using datetime module
    weekdays = ['MONDAY', 'TUESDAY', 'WEDNESDAY', 'THURSDAY',
                'FRIDAY', 'SATURDAY', 'SUNDAY']
    print(weekdays[date(y, m, d).weekday()])

    # Using calender module
    print(day_name[weekday(y, m, d)])


if __name__ == '__main__':
    m, d, y = map(int, input().split())
    find_day_name(m, d, y)
