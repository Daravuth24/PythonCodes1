student_id = input("Student's ID:")
student_name = input("Student's Name:")
mark1 = int(input("Mark 1:"))
mark2 = int(input("Mark 2:"))
mark3 = int(input("Mark 3:"))

total = mark1 + mark2 + mark3
average = total/3

print("Student's ID:", student_id)
print("Student's Name:", student_name)
print("The Total is:", total)
print("The Average is:", average)