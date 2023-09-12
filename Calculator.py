# Function to add two numbers
def add(num1, num2):
    return num1 + num2

# Function to subtract two numbers
def subtract(num1, num2):
    return num1 - num2

# Function to multiply two numbers
def multiply(num1,num2):
    return num1 * num2

# Function to divide two numbers
def divide(num1, num2):
    if num2 == 0:
        return "Cannot divide by zero"
    return num1 / num2

# Function to modulo two numbers
def modulo(num1,num2):
    if num2 == 0:
        return "Cannot divide by zero"
    return num1 % num2

# Define a dictionary that maps operation names to functions
operations = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide,
    '%':modulo
}

while True:
    # User menu
    print("Options:")
    print("Enter '+' for addition")
    print("Enter '-' for subtraction")
    print("Enter '*' for multiplication")
    print("Enter '/' for division")
    print("Enter '%' for modulo")
    print("Enter 'quit' to end the program")

    # Take user input
    choice = input("Enter operation: ")
    print("Enter The Input Numbers")

    if choice == "quit":
        break

    # Check if the operation is valid
    if choice in operations:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        # Use the dictionary to call the appropriate function
        result = operations[choice](num1, num2)
        print("Result:", result)
    else:
        print("Invalid input")
