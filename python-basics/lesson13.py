
students = []

# Load previously saved students
try:
    with open("students.txt", "r", encoding="utf-8") as file:
        for line in file:
            line = line.strip()

            if line:
                name, age = line.split(",", 1)

                student = {
                    "name": name,
                    "age": int(age)
                }

                students.append(student)

except FileNotFoundError:
    pass

choice = ""

while choice != "4":
    print("\n===== STUDENT MANAGEMENT =====")
    print("1. Add student")
    print("2. Show students")
    print("3. Search student")
    print("4. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        name = input("Enter student name: ").strip()

        try:
            age = int(input("Enter student age: "))

            if not name:
                print("Name cannot be empty.")

            elif age <= 0:
                print("Age must be greater than zero.")

            else:
                student = {
                    "name": name,
                    "age": age
                }

                students.append(student)

                with open("students.txt", "a", encoding="utf-8") as file:
                    file.write(f"{name},{age}\n")

                print(name, "was added successfully!")

        except ValueError:
            print("Invalid age! Please enter a whole number.")

    elif choice == "2":
        if not students:
            print("No students registered yet.")

        else:
            print("\n--- Student List ---")

            for student in students:
                print("Name:", student["name"])
                print("Age:", student["age"])
                print("-------------------")

    elif choice == "3":
        search_name = input("Enter the student name to search: ")

        found = False

        for student in students:
            if student["name"].lower() == search_name.lower():
                print("\nStudent found!")
                print("Name:", student["name"])
                print("Age:", student["age"])

                found = True
                break

        if not found:
            print("Student not found.")

    elif choice == "4":
        print("Program closed.")

    else:
        print("Invalid option!")
