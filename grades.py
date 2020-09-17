names = input("Please enter student names separated by commas: ").split(',')
assignments = input("Please enter the corresponding number\nof missing assignments separated by commas: ").split(',')
grades = input("Please enter the grades separated by commas: ").split(',')

for name, assignment, grade in zip(names, assignments, grades):
    assignment = int(assignment)
    grade = float(grade)
    message = (f"Hi {name},\n\nThis is a reminder that you have {assignment} assignments left to "
        f"submit before you can graduate. You're current grade is {grade} and can increase "
        f"to {grade + 2* assignment} if you submit all assignments before the due date.\n\n"
    )
    print(message)
