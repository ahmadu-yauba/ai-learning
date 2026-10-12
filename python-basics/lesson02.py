
mark = float(input("Enter your mark: 0 to 100"))
if mark > 100 or mark < 0:
    print("Invalid mark. Please enter a value between 0 and 100.")  
elif mark >= 90: 
    print("Excellent!")
elif mark >= 80:
    print("Very good!")
elif mark >= 70:
    print("Good!")
elif mark >= 60:
    print("credit")
elif mark >= 50:
    print("You passed!")
else:
    print("fail")