# Normal variable declaration with type hinting
age: int = 25
name: str = "Alice"
is_student: bool = True

#########################################################
# Type Hinting for Collections
from typing import List, Dict, Tuple

# List of integers
numbers: List[int] = [1, 2, 3, 4, 5]

# Dictionary with string keys and integer values
student_scores: Dict[str, int] = {"Alice": 90, "Bob": 85}

# Tuple with a string and an integer
person: Tuple[str, int] = ("Alice", 25)

#########################################################
# Type hinting for function arguments and returns
def add(a: int, b: int) -> int:
    return a + b

def display_info(name: str, age: int, is_student: bool) -> str:
    return f"Name: {name}, Age: {age}, Student: {is_student}"

# Example usage
result = add(3, 5)
info = display_info("Alice", 25, True)

