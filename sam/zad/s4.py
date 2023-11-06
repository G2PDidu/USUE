def update_grades(grades):
    updated_grades = []
    for grade in grades:
        if grade == 2:
            updated_grades.append(1)
        elif grade == 3:
            updated_grades.append(4)
        else:
            updated_grades.append(grade)
    return updated_grades

grades_1 = [2,3,4,5,3,4,5,2,2,5,3,4,3,5,4]
grades_2 = [4,2,3,5,3,5,4,2,2,5,4,3,5,3,4]
grades_3 = [5,4,3,3,4,3,3,5,5,3,3,3,3,4,4]

updated_grades_1 = update_grades(grades_1)
updated_grades_2 = update_grades(grades_2)
updated_grades_3 = update_grades(grades_3)

print("Обновленный массив 1:", updated_grades_1)
print("Обновленный массив 2:", updated_grades_2)
print("Обновленный массив 3:", updated_grades_3)

