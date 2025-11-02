# Demonstration of Object-Oriented Programming (OOP) in Python
# This code showcases inheritance, polymorphism, and encapsulation.

# Base class: Animal
# Encapsulation: Using private attributes (__name) to hide internal state.
class Animal:
    def __init__(self, name):
        self.__name = name  # Private attribute for encapsulation
    
    def get_name(self):
        return self.__name  # Public method to access private attribute
    
    def speak(self):
        return "Some generic animal sound"  # Default method for polymorphism

# Inheritance: Dog class inherits from Animal
class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)  # Call parent constructor
        self.breed = breed  # Additional attribute
    
    # Polymorphism: Overriding the speak method
    def speak(self):
        return f"{self.get_name()} says Woof! (Breed: {self.breed})"

# Inheritance: Cat class inherits from Animal
class Cat(Animal):
    def __init__(self, name, color):
        super().__init__(name)  # Call parent constructor
        self.color = color  # Additional attribute
    
    # Polymorphism: Overriding the speak method
    def speak(self):
        return f"{self.get_name()} says Meow! (Color: {self.color})"

# Demonstration of the concepts
if __name__ == "__main__":
    # Create instances
    dog = Dog("Buddy", "Golden Retriever")
    cat = Cat("Whiskers", "Black")
    generic_animal = Animal("Unknown")
    
    # Encapsulation: Accessing private attribute via public method
    print(f"Dog's name: {dog.get_name()}")
    print(f"Cat's name: {cat.get_name()}")
    
    # Polymorphism: Same method name, different behavior
    animals = [dog, cat, generic_animal]
    for animal in animals:
        print(animal.speak())
    
    # Inheritance: Dog and Cat have access to Animal's methods
    print(f"Dog breed: {dog.breed}")  # Additional attribute from Dog
    print(f"Cat color: {cat.color}")  # Additional attribute from Cat
