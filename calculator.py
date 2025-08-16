import os
os.system('cls')

num1 = None
num2 = None

while True:
    if num1 is None:
        user_input = input("Enter first number: ")
        try:
            num1 = float(user_input)
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            continue
    if num2 is None:
        user_input = input("Enter second number: ")
        try:
            num2 = float(user_input)
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            continue
    if num1 is not None and num2 is not None:
        break
operation = input("Enter operation (+, -, *, /): ")
if operation == '+':
    result = num1 + num2
elif operation == '-':
    result = num1 - num2
elif operation == '*':
    result = num1 * num2
elif operation == '/':
    if num2 == 0:
        result = "Error: Division by zero is not allowed."
    else:
        result = num1 / num2


else:    result = "Invalid operation. Please enter one of +, -, *, /."  


if result is not None:
    print("Result:", result)