class FileOpener:
    def __init__(self, file, mode):
        self.file = file
        self.mode = mode
        self.file_obj = None

    def __enter__(self):
        self.file_obj = open(self.file, self.mode)
        return self.file_obj

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file_obj:
            self.file_obj.close()

# Using the context manager
with FileOpener('example.txt', 'w') as f:
    f.write('Hello, World!')

# No need to explicitly close the file
