class Counter:
    instance_count = 0  # Class variable
    
    def __init__(self):
        Counter.instance_count += 1

# Test by creating multiple objects
obj1 = Counter()
obj2 = Counter()
obj3 = Counter()

print(f"Number of instances: {Counter.instance_count}")  # Output: Number of instances: 3