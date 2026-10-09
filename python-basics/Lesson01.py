
# Lesson 1: Student Profile Program

name = input("Enter your name: ")
course = input("Enter your course: ")

mark1 = float(input("Enter your first mark: "))
mark2 = float(input("Enter your second mark: "))
mark3 = float(input("Enter your third mark: "))

average = (mark1 + mark2 + mark3) / 3

print("\n--- STUDENT PROFILE ---")
print(f"Name: {name}")
print(f"Course: {course}")
print(f"Average mark: {average:.2f}")