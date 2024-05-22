import ctypes

# Load the shared library into ctypes
libexample = ctypes.CDLL('./libexample.so')

# Call the add function
add = libexample.add
add.argtypes = (ctypes.c_int, ctypes.c_int)
add.restype = ctypes.c_int

result = add(5, 7)
print(f"Result of add(5, 7): {result}")

# Call the hello function
libexample.hello()
