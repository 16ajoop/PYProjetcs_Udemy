
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


# SAMPLE 3 HOW TO ITERATE OVER A PANDAS DATA FRAME
import pandas as pd
student_data_frame = pd.DataFrame(student_dict)
print(student_data_frame)
# Loop through rows of a data frame
for (index, row) in student_data_frame.items():
  print(row)
