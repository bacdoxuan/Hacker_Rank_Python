if __name__ == '__main__':
    """
    Enter N students, each student has one score. Print students who have
    second lowest score
    """
    students = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name, score])
    students.sort(key=lambda x: x[0])
    lowest_score = min(students, key=lambda x: x[1])[1]
    lowest_students = [st for st in students if st[1] == lowest_score]
    for student in lowest_students:
        students.remove(student)
    lowest_score = min(students, key=lambda x: x[1])[1]
    for student in students:
        if student[1] == lowest_score:
            print(student[0])
