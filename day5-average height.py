# # 🚨 Don't change the code below 👇
# student_heights = input("Input a list of student heights ").split()
# for n in range(0, len(student_heights)):
#   student_heights[n] = int(student_heights[n])
# # 🚨 Don't change the code above 👆
# total_heights = 0
# for num in student_heights:
#     total_heights += num
# print(f"sum of students height: {total_heights}")
# number_of_students = 0
# for student in student_heights:
#     number_of_students +=1
# print(f"number of students: {number_of_students}")

# average_height = total_heights/number_of_students
# print(round(average_height))

import json, time

fixed_name = "vpc"
result = {
    "name": f"{fixed_name}-{int(time.time())}",
} 
print(time.time())
print(json.dumps(result))