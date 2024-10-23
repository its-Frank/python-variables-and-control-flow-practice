#Write a Python program that takes two numbers and an operation (+, -, *, /) from the user. Perform the operation and print the result.
# Function to perform the calculation
def calculator(num1, num2, operation):
    if operation == '+':
        return num1 + num2
    elif operation == '-':
        return num1 - num2
    elif operation == '*':
        return num1 * num2
    elif operation == '/':
        if num2 != 0:
            return num1 / num2
        else:
            return "Error: Division by zero is not allowed."
    else:
        return "Error: Invalid operation."
# Take user input
try:
    number1 = float(input("Enter the first number: "))
    number2 = float(input("Enter the second number: "))
    operation = input("Enter the operation (+, -, *, /): ")

    # Perform the calculation
    result = calculator(number1, number2, operation)

    # Print the result
    print("Result:", result)
except ValueError:
    print("Error: Please enter valid numbers.")
