class Descriptor:
    def __init__(self, name):
        self.name = name

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return instance.__dict__.get(self.name)

    def __set__(self, instance, value):
        if not isinstance(value, int):
            raise ValueError(f"{self.name} must be an integer")
        if value < 0:
            raise ValueError(f"{self.name} must be non-negative")
        instance.__dict__[self.name] = value

    def __delete__(self, instance):
        raise AttributeError(f"Can't delete attribute {self.name}")

class MyClass:
    attr = Descriptor("attr") # String attr is the name for the attribute

    def __init__(self, attr):
        self.attr = attr

# Testing the descriptor
obj = MyClass(10)
print(obj.attr)  # Output: 10

try:
    obj.attr = -5  # Raises ValueError: attr must be non-negative
except ValueError as e:
    print(e)

try:
    obj.attr = "string"  # Raises ValueError: attr must be an integer
except ValueError as e:
    print(e)

try:
    del obj.attr  # Raises AttributeError: Can't delete attribute attr
except AttributeError as e:
    print(e)
