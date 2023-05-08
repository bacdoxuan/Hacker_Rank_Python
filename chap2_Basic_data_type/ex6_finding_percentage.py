if __name__ == '__main__':
    """
    input integer N
    input N student with name, followed by student's scores, separated by spaces
    input name of one student in N students above
    print the average score of the student you've just entered
    """  # NOQA
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    from statistics import mean
    print("%.2f" % mean(student_marks[query_name]))
