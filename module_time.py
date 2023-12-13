import time

# Get the current time as a struct_time object
current_time_struct = time.localtime()

# Format and print the current time
formatted_time = time.strftime("%Y-%m-%d ,%H:%M:%S", current_time_struct)
print("Current Time:", formatted_time)
