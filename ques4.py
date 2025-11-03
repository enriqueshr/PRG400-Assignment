class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.__salary = salary  # Private attribute
    
    def get_salary(self):
        return self.__salary
    
    def set_salary(self, new_salary):
        if new_salary > 0:
            self.__salary = new_salary
        else:
            print("Invalid salary")

# Demonstration of encapsulation
emp = Employee("John", 50000)

# Trying direct access (will raise AttributeError)
try:
    print(emp.__salary)  # This will fail
except AttributeError as e:
    print(f"Direct access failed: {e}")

# Using getter and setter
print(f"Salary via getter: {emp.get_salary()}")  # Output: Salary via getter: 50000
emp.set_salary(60000)
print(f"Updated salary via getter: {emp.get_salary()}")  # Output: Updated salary via getter: 60000