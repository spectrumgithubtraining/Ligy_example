
import operator  
# Take two input numbers from user  
x = int(input("Enter first integer number: "))  
y = int(input("Enter second integer number: "))  
# Multiply both input numbers
add=operator.add(x,y)
sub=operator.sub(x,y) 
mul = operator.mul(x, y)  
# Print result 
print("Adding result of numbers given by you is: ", add) 
print("Subtraction result of numbers given by you is: ", sub)   
print("Multiplication result of numbers given by you is: ", mul)  