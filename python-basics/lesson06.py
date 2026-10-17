with open("student.txt", "w", encoding="utf-8") as file:
    file.write(input("Enter student name: ") + "\n")
    file.write(input("Enter student course: ") + "\n")


with open("student.txt", "r", encoding="utf-8") as file:
    content = file.read()

print("Student information from file:")
print("name: " + content.splitlines()[0])
print("course: " + content.splitlines()[1])