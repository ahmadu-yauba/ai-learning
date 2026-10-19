
try:
    name = input("Enter your name")
    age = int(input("Enter your age: "))
    print("Hello:", name)
    print("Next year, you will be", age + 1)
    

except ValueError:
    print("Invalid input! Please enter a number.")
