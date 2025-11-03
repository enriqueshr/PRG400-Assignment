class A:
    def greet(self):
        print("Hello from A")

class B:
    def greet(self):
        print("Hello from B")

class C(A, B):  # C inherits from A and B
    pass

# Create an object of C and call greet()
obj_c = C()
obj_c.greet()  # Output: Hello from A