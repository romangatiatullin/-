grades = [[5,3,3,5,4], [2,2,2,3],[4,5,5,2], [4,4,3], [5,5,5,4,5]]
students = {'Johny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
average_grades = {}
sorted_students = sorted(students)
for student, grade in zip(sorted_students, grades):
    average_grades[student] = sum(grade) / len(grade)
    print(average_grades)