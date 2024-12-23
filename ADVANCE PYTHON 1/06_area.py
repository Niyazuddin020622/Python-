def calculate_area():
    shape = input("Enter the shape (circle, rectangle, square): ").lower()

    match shape:
        case "circle":
            radius = float(input("Enter the radius of the circle: "))
            area = 3.14159 * radius**2
            print(f"The area of the circle is: {area:.2f}")
        case "rectangle":
            length = float(input("Enter the length of the rectangle: "))
            width = float(input("Enter the width of the rectangle: "))
            area = length * width
            print(f"The area of the rectangle is: {area:.2f}")
        case "square":
            side = float(input("Enter the side of the square: "))
            area = side**2
            print(f"The area of the square is: {area:.2f}")
        case _:
            print("Invalid shape! Please enter 'circle', 'rectangle', or 'square'.")

# Call the function
calculate_area()
