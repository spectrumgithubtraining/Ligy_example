# import math_operations

# # Using functions from the math_operations module
# result_add = math_operations.add(5, 3)
# result_subtract = math_operations.subtract(10, 4)
# result_multiply = math_operations.multiply(2, 6)
# result_divide = math_operations.divide(8, 2)

# # Printing the results
# print("Addition:", result_add)
# print("Subtraction:", result_subtract)
# print("Multiplication:", result_multiply)
# print("Division:", result_divide)

import calendar

def print_calendar(year, month):
    # Generate a text calendar for the specified month and year
    cal_text = calendar.month(year, month)

    # Print the calendar
    print(f"Calendar for {calendar.month_name[month]} {year}:\n")
    print(cal_text)

# Example usage:
year_input = int(input("Enter the year: "))
month_input = int(input("Enter the month (1-12): "))

print_calendar(year_input, month_input)
