from functools import reduce

numbers = [1, 2, 3, 4, 5]

# Using reduce with a lambda function
product = reduce(lambda x, y: x * y, numbers)
print(product)  # Output: 120
