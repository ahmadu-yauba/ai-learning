number = int(input("Enter a number"))
print(f"Multiplication table for {number}")
for i in range(1, 11):
  r = i * number
  print(number, "X", i, "=", r)          