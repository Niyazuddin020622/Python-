def calculator():
    # Take inputs from the user
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    operation = input("Enter the operation (add, sub, mul, div): ").lower()

    # Use match-case to determine the operation
    match operation:
        case "add":
            print(f"The result of addition is: {num1 + num2}")
        case "sub":
            print(f"The result of subtraction is: {num1 - num2}")
        case "mul":
            print(f"The result of multiplication is: {num1 * num2}")
        case "div" if num2 != 0:
            print(f"The result of division is: {num1 / num2}")
        case "div" if num2 == 0:
            print("Error: Division by zero is not allowed.")
        case _:
            print("Invalid operation. Please enter add, sub, mul, or div.")

# Call the function
calculator()
