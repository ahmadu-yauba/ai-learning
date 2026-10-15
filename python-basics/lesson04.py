
marks = [80, 65, 90, 75, 55]

# 1. Print the list
print(marks)
# 2. Calculate the average
average = sum(marks) / len(marks)
# 3. Create a student dictionary
student = {
    "name": "Alice",
    "marks": marks,
    "average": average
}
# 4. Print the student's name and average
print(f"Student: {student['name']}, Average: {student['average']}")
