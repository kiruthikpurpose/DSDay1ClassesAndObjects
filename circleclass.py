import math 

class Circle:
    def __init__(self, radius): 
        self.radius = radius

    def perimeter(self):
        print(f"{2*math.pi*self.radius: .2f} units")
    
    def area(self):
        print(f"{math.pi*self.radius**2: .2f} square units")
    
c1 = Circle(4)
c1.perimeter()
c1.area()