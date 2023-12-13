import threading  
   
def print_message():  
    print("Hello, world!")  
   
t = threading.Timer(5.0, print_message)  
t.start()  