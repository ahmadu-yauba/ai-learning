
while True:
    try:
        number = int(input("Enter a whole number: "))

        print("Double:", number * 2)
        break

    except ValueError:
        print("Invalid input! Please try again.")
