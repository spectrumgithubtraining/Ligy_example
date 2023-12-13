# Default Arugmnet
def power(base, exponent=2):
    return base ** exponent

result1 = power(2)     
result2 = power(2, 3)
print("Result 1:", result1)
print("Result 2:", result2)

#Required Arugment
def greet(name, greeting):
    """This function greets a person with a specific greeting."""
    print(f"{greeting}, {name}!")

# Calling the function with required arguments
greet("Alice", "Hello")

KeyWord Arugment
def greet(first_name, last_name):
    print('First Name:', first_name)
    print('Last Name:', last_name)

greet(last_name = 'Cartman', first_name = 'Eric')

#Args Example
def myFun(*argv):  
    for arg in argv:  
        print (arg) 
    
myFun('Hello', 'Welcome', 'to', 'GeeksforGeeks') 

#kwargs Example
def myFun(**kwargs):  
        d={}
        for key,value in kwargs.items(): 
                d[key]=value
        print(d)
  
# Driver code 

myFun(first ='Geeks', mid ='for', last='Geeks')   