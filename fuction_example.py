
##USING PRINT##
def add(x,y):
    print(x+y)
add(5,7)

##Arithmetric Operations##
# def add(x, y):
#     """This function adds two numbers."""
#     return x + y

# def subtract(x, y):
#     """This function subtracts y from x."""
#     return x - y

# def multiply(x, y):
#     """This function multiplies two numbers."""
#     return x * y

# def divide(x, y):
#     """This function divides x by y, handling division by zero."""
#     if y != 0:
#         return x / y
#     else:
#         return "Cannot divide by zero."

# # Application using the calculator functions
# num1 = float(input("Enter the first number: "))
# num2 = float(input("Enter the second number: "))

# print("\nResults:")
# print("Adding:", add(num1,num2))
# print("Subtraction:", subtract(num1, num2))
# print("Mulitiplication:", multiply(num1, num2))
# print("Division:", divide(num1, num2))


##USING RETURN##
def add(a,b):
    return a+b
x=int(input("Enter the Number1:"))
y=int(input("Enter the Number2:"))
print(add(x,y))
