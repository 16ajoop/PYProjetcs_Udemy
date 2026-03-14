import random

names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]

students_scores = {student:random.randint(1,100) for student in names}
print(students_scores)

# passed_student = {new_key:new_value for (key, value) in students_score.items() if test} --------------SYNTAX

passed_student = {student:score for (student,score) in students_scores.items() if score >= 60}
print(passed_student)
