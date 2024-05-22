numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Using filter with a lambda function
even_numbers = filter(lambda x: x % 2 == 0, numbers)

# Convert filter object to list
even_numbers_list = list(even_numbers)
print(even_numbers_list)  # Output: [2, 4, 6, 8]
