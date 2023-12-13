# List of numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Lambda function to filter even numbers
filter_even = lambda x: x % 2 == 0

# Use the lambda function to filter even numbers from the list
even_numbers = list(filter(filter_even, numbers))

# Print the result
print("Original numbers:", numbers)
print("Even numbers:", even_numbers)
