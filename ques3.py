class Animal:
    def speak(self):
        print("Animal makes a sound")

class Dog(Animal):
    def speak(self):
        print("Woof!")

# Create an object of Dog and call speak()
my_dog = Dog()
my_dog.speak()  # Output: Woof!