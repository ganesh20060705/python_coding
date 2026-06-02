a=int(input("Enter the NUmber(a):"))
b=int(input("Enter the NUmber(b):"))
print("Select operation")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
choice = input("Enter choice: ")
if choice == '1':
    print("Result:", a + b)
elif choice == '2':
    print("Result:", a - b)
elif choice == '3':
    print("Result:", a * b)
elif choice == '4':
    print("Result:", a / b)
else:
    print("Invalid input")  