def calculate_average(marks):
    return sum(marks) / len(marks)

def get_grade(average):
    if average >= 80:
        return "A"
    elif average >= 70:
        return "B"
    elif average >= 60:
        return "C"
    elif average >= 50:
        return "D"
    else:
        return "F"

marks = [80, 65, 90, 75, 55]
average = calculate_average(marks)
grade = get_grade(average)

print(f"The average mark is: {average}")
print(f"The grade is: {grade}")