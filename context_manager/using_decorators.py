import contextlib

@contextlib.contextmanager
def open_file(file, mode):
    f = open(file, mode)
    try:
        yield f
    finally:
        f.close()

# Using the context manager
with open_file('example.txt', 'w') as f:
    f.write('Hello, World!')

# No need to explicitly close the file
