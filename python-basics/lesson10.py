
students = []


def add_student(name, age, course):
    student = {
        "name": name,
        "age": age,
        "course": course
    }

    students.append(student)
    print(name, "was added successfully!")


def show_students():
    if not students:
        print("No students registered yet.")
        return

    print("\n--- Student List ---")

    for student in students:
        print("Name:", student["name"])
        print("Age:", student["age"])
        print("Course:", student["course"])
        print("--------------------")


def find_student(name):
    for student in students:
        if student["name"].lower() == name.lower():
            print("Student found!")
            print("Name:", student["name"])
            print("Age:", student["age"])
            print("Course:", student["course"])
            return

    print("Student not found.")


add_student("Ahmadu", 24, "Artificial Intelligence")
add_student("Fatima", 22, "Software Engineering")

show_students()

print("\n--- Search for a Student ---")
find_student("Ahmadu")
find_student("Omar")
