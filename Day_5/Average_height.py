# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


#Write your code below this row 👇

sumHeight = 0
for studentHeight in student_heights:
    sumHeight += studentHeight

sumHeight /= len(student_heights)
sumHeight = round(sumHeight)

print(sumHeight)