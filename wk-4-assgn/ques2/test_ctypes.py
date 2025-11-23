import ctypes

# Load the shared library
lib = ctypes.CDLL('./libstrlib.so')

# Define the function signature
lib.reverse_string.argtypes = [ctypes.c_char_p]
lib.reverse_string.restype = None

# Test it
original = b"Hello World"
print(f"Original: {original.decode()}")

# ctypes modifies the buffer in place, so we need a mutable buffer
buf = ctypes.create_string_buffer(original)
lib.reverse_string(buf)
result = buf.value.decode()
print(f"Reversed: {result}")  # Output: Reversed: dlroW olleH