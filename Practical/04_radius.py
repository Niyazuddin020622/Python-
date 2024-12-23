import math

class Circle:
    def __init__(self, radius):
        """Initialize the radius of the circle."""
        self.radius = radius

    def area(self):
        """Calculate and return the area of the circle."""
        return math.pi * self.radius ** 2

    def circumference(self):
        """Calculate and return the circumference of the circle."""
        return 2 * math.pi * self.radius

# Example usage
circle1 = Circle(5)
circle2 = Circle(7)

print(f"Circle 1:")
print(f"Radius: {circle1.radius}")
print(f"Area: {circle1.area():.2f}")
print(f"Circumference: {circle1.circumference():.2f}")

print("\nCircle 2:")
print(f"Radius: {circle2.radius}")
print(f"Area: {circle2.area():.2f}")
print(f"Circumference: {circle2.circumference():.2f}")
