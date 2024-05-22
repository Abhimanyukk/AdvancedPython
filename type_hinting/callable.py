from typing import Callable

def apply_function(func: Callable[[int, int], int], a: int, b: int) -> int:
    return func(a, b)

def add(a: int, b: int) -> int:
    return a + b

# Example usage
result = apply_function(add, 5, 10)  # Using the previously defined `add` function
print(result)
