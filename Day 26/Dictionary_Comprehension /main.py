
# SAMPLE 1
import random
names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
students_scores = {student:random.randint(1,100) for student in names}
print(students_scores)
# passed_student = {new_key:new_value for (key, value) in students_score.items() if test} --------------SYNTAX
passed_student = {student:score for (student,score) in students_scores.items() if score >= 60}
print(passed_student)

# SAMPLE 2 LOOPING THROUGH DICTIONARY
student_dict = {
  "student": ["Angela", "James", "Lily"],
  "score": [56, 76, 98]
}

for (key,value) in student_dict.items():
  print(key)
  print(value)
