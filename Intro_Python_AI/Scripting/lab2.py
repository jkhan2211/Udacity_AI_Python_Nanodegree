names = [name.strip() for name in input('Enter names separated by commas: ').split(',')]
assignments = [assignment.strip() for assignment in input('Enter assignment counts separated by commas: ').split(',')]
grades = [grade.strip() for grade in input('Enter grades separated by commas: ').split(',')]

message = "Hi {},\n\nThis is a reminder that you have {} assignments left to submit before you can graduate. Your current grade is {} and can increase to {} if you submit all assignments before the due date.\n\n"

for name, assignment, grade in zip(names, assignments, grades):
        new_grade = int(grade) + int(assignment) * 2
        print(message.format(name, assignment, grade, new_grade))
   