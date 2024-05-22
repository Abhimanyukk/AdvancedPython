from typing import Optional, Union, Dict

def find_student(name: str) -> Optional[Dict[str, Union[str, int]]]:
    students = {
        "Alice": {"age": 25, "grade": "A"},
        "Bob": {"age": 22, "grade": "B"}
    }
    return students.get(name)

# Example usage
student_info = find_student("Alice")
if student_info:
    print(student_info)
else:
    print("Student not found")

student_info = find_student("Charlie")
if student_info:
    print(student_info)
else:
    print(student_info)
    print("Student not found")
