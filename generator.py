# def simpleGeneratorFun():
#     yield 1
#     yield 2
#     yield 3

# # x is a generator object
# x = simpleGeneratorFun()

# # Iterating over the generator object using next
# print(next(x))
# print(next(x))
# print(next(x))

def square_generator(n):
    for i in range(n):
        yield i ** 2
# Using the generator
n_values = 5
squares = square_generator(n_values)
# Iterating over the generator
for square in squares:
    print(square)
