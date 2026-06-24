# Creating a mini calculator that can perform basic arithmetic operations (addition, subtraction, multiplication, division) on two numbers. The calculator should take user input for the two numbers and the desired operation, and then output the result.
# 3 steps to implement the calculator functionality
#    1. Functions for operations
#    2. User input
#    3. Print result

# Function to perform the desired operation
def calculate(num1, num2, operation):
    if operation == 'add':
        return num1 + num2
    elif operation == 'subtract':
        return num1 - num2
    elif operation == 'multiply':
        return num1 * num2
    elif operation == 'divide':
        if num2 != 0:
            return num1 / num2
        else:
            return "Error: Division by zero is not allowed."
    elif operation == 'average':
        return (num1 + num2) / 2
    else:
        return "Error: Invalid operation."
# User input
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operation = input("Enter the desired operation: ")

# Print result
print("Result:", calculate(num1, num2, operation))