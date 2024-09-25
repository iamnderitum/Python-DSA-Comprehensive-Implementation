if __name__ == '__main__':

    n = int(input("Enter The Number Of Students: "))
    students = []

    for _ in range(n):
        name = input(f"Enter student {_} name: ")
        score = float(input(f"Enter student {_} marks: "))

        students.append([name, score])

    print("Student List:")
    print("---------------")
    print(students)

    # Extract all grades
    sorted_grades = sorted(set([student[1] for student in students]))
    print(sorted_grades)

    # Second lowest grade
    second_lowest_grade = sorted_grades[1]
    print(second_lowest_grade)

    # Finding all students with the second lowest grade
    second_lowest_students = [student[0] for student in students if student[1] == second_lowest_grade]

    # Sorting names alphabetically
    second_lowest_students.sort()

    # Printing names
    for name in second_lowest_students:
        print(name)