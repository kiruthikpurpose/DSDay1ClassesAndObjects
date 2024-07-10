import math

class Circle:
    def __init__(self, radius):
        # Initialize the circle with the given radius
        self.radius = radius

    def perimeter(self):
        # Calculate the perimeter (circumference) and print it
        perimeter = 2 * math.pi * self.radius
        print(f"{perimeter:.2f} units")
    
    def area(self):
        # Calculate the area and print it
        area = math.pi * self.radius**2
        print(f"{area:.2f} square units")

# Create a circle with a radius of 4
c1 = Circle(4)

# Print the perimeter of the circle
c1.perimeter()

# Print the area of the circle
c1.area()
