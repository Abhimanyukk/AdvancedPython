numbers = [1, 2, 3, 4, 5]

# Using map with a lambda function
squares = map(lambda x: x * x, numbers)

# Convert map object to list
squares_list = list(squares)
print(squares_list)  # Output: [1, 4, 9, 16, 25]
