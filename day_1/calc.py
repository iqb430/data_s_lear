print("Welcome to the Simple Calculator!")
print("You can perform operations like this: 'number operator number'")
print("Supported operators: +, -, *, /")
print("Type 'exit' to quit the calculator.")

while True:
    user_input = input("Enter your expression: ")

    if user_input.lower() == 'exit':
        print("Exiting the calculator. Goodbye!")
        break

    # Split the input into parts
    parts = user_input.split()

    # Check if the input is valid
    if len(parts) != 3:
        print("Error: Please enter an expression in the format 'number operator number'.")
        continue

    # Get the numbers and operator
    num1 = parts[0]
    operator = parts[1]
    num2 = parts[2]

    # Try to convert the numbers to float
    try:
        num1 = float(num1)
        num2 = float(num2)
    except ValueError:
        print("Error: Invalid number format.")
        continue

    # Perform the operation based on the operator
    if operator == '+':
        result = num1 + num2
        print("Result:", result)
    elif operator == '-':
        result = num1 - num2
        print("Result:", result)
    elif operator == '*':
        result = num1 * num2
        print("Result:", result)
    elif operator == '/':
        if num2 == 0:
            print("Error: Division by zero!")
        else:
            result = num1 / num2
            print("Result:", result)
    else:
        print("Error: Unsupported operator. Use +, -, *, or /.")
