class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def calculate_area(self):
        return self.length * self.width
    
    def calculate_perimeter(self):
        return 2 * (self.length + self.width)

# Instantiate the class and print both values
rect = Rectangle(5, 3)
print(f"Area: {rect.calculate_area()}")        # Output: Area: 15
print(f"Perimeter: {rect.calculate_perimeter()}")  # Output: Perimeter: 16