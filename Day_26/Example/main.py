import random
import pandas as pd

numbers = [1, 2, 3]
new_items = [n+1 for n in numbers]
print(new_items)

listtest = [n*2 for n in range(1, 5)]
print(listtest)

names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
maj_names = [name.upper() for name in names if len(name) > 5]
print(maj_names)

students_score = {key_score: random.randint(0, 100) for key_score in names}
print(students_score)

passed_student = {key_student: student_score for (key_student, student_score) in students_score.items() if
                  student_score > 50}
print(passed_student)

student_dict = {
    "student": ["Alex", "Beth", "Caroline"],
    "score": [56, 76, 98],
}

student_data_frame = pd.DataFrame(student_dict)
print(student_data_frame)

for (index, value) in student_data_frame.iterrows():
    student_score = value.score
    print(student_score)

student_score = {index: value.score for (index, value) in student_data_frame.iterrows() if value.score > 70}
print(student_score)