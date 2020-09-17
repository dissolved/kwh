number_students = int(input("Enter the number of students: "))
print("\n")

names = list()
assignments = list()
grades = list()
for _ in range(number_students):
    names.append(input("Enter the student's name: "))
    assignments.append(int(input("Enter the number of missing assignments: ")))
    grades.append(float(input("Enter the current grade: ")))
    print("\n")

for name, assignment, grade in zip(names, assignments, grades):
    assignment = int(assignment)
    grade = float(grade)
    message = (f"Hi {name},\n\nThis is a reminder that you have {assignment} assignments left to "
        f"submit before you can graduate. You're current grade is {grade}"
    )
    if assignment > 0:
        message += f" and can increase to {grade + 2* assignment} if you submit all assignments before the due date.\n\n"
    else:
        message += ".\n\n"
    print(message)
    print("----------------------------------------------------------")
