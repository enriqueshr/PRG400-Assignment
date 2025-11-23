import arraylib

# Create an array object
arr = arraylib.Array()

# Initialize with size 5
arr.init(5)

# Set values
arr.set(0, 10)
arr.set(1, 20)
arr.set(4, 50)

# Get values
print(f"arr[0] = {arr.get(0)}")  # 10
print(f"arr[1] = {arr.get(1)}")  # 20
print(f"arr[4] = {arr.get(4)}")  # 50

# Free (optional, as dealloc handles it)
arr.free()      