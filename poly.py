# class Human:
#     def sayHello(self, name=None):
#         if name is not None:
#             print('Hello ' + name)
#         else:
#             print('Hello ')

# # Create an instance
# obj = Human()

# # Call the method
# obj.sayHello()

# # Call the method with a parameter
# obj.sayHello('Guido')
class Parent:
    # define parent class
    def myMethod(self):
        print('Calling parent method')

class Child(Parent):
    # define child class
    def myMethod(self):
        print('Calling child method')

c = Child()  # instance of child
c.myMethod()  # child calls overridden method
