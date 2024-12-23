def divide_numbers():
    try:
        num1 = float(input("Enter the numerator: "))

        num2 = float(input("Enter the denominator: "))

        result = num1/num2

        print(f"The result is: {result}")

    except ZeroDivisionError:
        print(f"Error: Division by zero is not allowed.")

    except ValueError:
        print("Error: Please enter a valid number.v")

    except Exception as e:
        print(f"An unexpected error occured: {e}")

    finally:
        print("Execution complete. Cleanup if necessary.")

divide_numbers() # call the function
