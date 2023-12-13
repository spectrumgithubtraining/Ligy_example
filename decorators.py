# def hello():         # here, we are creating a function named hello  
#     def hi():         # here, we are creating a function named hi  
#         print("Hello")             # here, we are printing the output of the function  
#     return hi         # here, we are returning the output of the function  
# new = hello()    
# new()    


# def my_decorator(func):
#     def wrapper():
#         print("Something is happening before the function is called.")
#         func()
#         print("Something is happening after the function is called.")
#     return wrapper

# @my_decorator
# def add():
#     return x + y

# result = add(3, 5)
# print("Result:", result)


def make_pretty(func):
    def inner():
        print("I got decorated")
        func()
    return inner
@make_pretty
def ordinary():
    print("I am ordinary")
ordinary()

def decorator(func):
    def wrapper(*args, **kwargs):
        print("Decorator is called before the function.")
        result = func(*args, **kwargs)  # Call the original function
        print("Decorator is called after the function.")
        return result
    return wrapper

@decorator
def add_numbers(x, y):
    """This function adds two numbers."""
    return x + y

result = add_numbers(3, 5)
print("Result:", result)