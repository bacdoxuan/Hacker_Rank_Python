"""https://www.hackerrank.com/challenges/zipped/problem."""
import statistics


def cal_average_point():
    """https://www.hackerrank.com/challenges/zipped/problem."""
    no_students, no_subjects = map(int, input().split())
    students_points = []
    for _ in range(no_subjects):
        students_points.append(list(map(float, input().split())))

    result = list(zip(*students_points))
    for i in range(no_students):
        print('%.1f' % statistics.mean(result[i]))


if __name__ == '__main__':
    cal_average_point()
