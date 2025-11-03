class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
    
    def display_details(self):
        print(f"Make: {self.make}, Model: {self.model}, Year: {self.year}")

# Create an object and call the method
my_car = Car("Toyota", "Camry", 2020)
my_car.display_details()  # Output: Make: Toyota, Model: Camry, Year: 2020