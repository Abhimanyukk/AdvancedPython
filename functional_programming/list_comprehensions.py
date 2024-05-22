numbers = [1, 2, 3, 4, 5]

# List comprehension for mapping
squares_list = [x * x for x in numbers]
print(squares_list)  # Output: [1, 4, 9, 16, 25]

# List comprehension for filtering
even_numbers_list = [x for x in numbers if x % 2 == 0]
print(even_numbers_list)  # Output: [2, 4]
