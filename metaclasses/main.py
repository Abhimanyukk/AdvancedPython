class MyMeta(type):
    def __new__(cls, name, bases, dct):
        # Add a new method to the class
        dct['greet'] = lambda self: f"Hello from {self.__class__.__name__}!"
        
        # Print a message when the class is created
        print(f"Creating class {name}")
        
        # Call the superclass's __new__ method to create the class
        return super().__new__(cls, name, bases, dct)


class MyClass(metaclass=MyMeta):
    def __init__(self, value):
        self.value = value

    def show(self):
        print(f"Value: {self.value}")

# Instantiate the class
obj = MyClass(42)
obj.show()
print(obj.greet())
