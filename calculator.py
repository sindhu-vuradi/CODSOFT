def calculator():
    print(" Simple Calculator")
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
    except ValueError:
        print(" Invalid input. Please enter numeric values.")
        return

    print("\nChoose an operation:")
    print(" + for Addition")
    print(" - for Subtraction")
    print(" * for Multiplication")
    print(" / for Division")

    operation = input("Enter operation: ")
    if operation == '+':
        result = num1 + num2
        print(f"Result: {num1} + {num2} = {result}")
    elif operation == '-':
        result = num1 - num2
        print(f"Result: {num1} - {num2} = {result}")
    elif operation == '*':
        result = num1 * num2
        print(f" Result: {num1} * {num2} = {result}")
    elif operation == '/':
        if num2 == 0:
            print(" Error: Division by zero is not allowed.")
        else:
            result = num1 / num2
            print(f" Result: {num1} / {num2} = {result}")
    else:
        print(" Invalid operation. Please choose from +, -, *, /.")
calculator()
