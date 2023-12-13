import csv

# Open the CSV file in append mode
with open('apple.csv', 'a', newline='') as file:
    writer = csv.writer(file)

    # Tuple to be added to the CSV file
    tup = ("Bob", 20)

    # Write the tuple as a new row in the CSV file
    writer.writerow(tup)

print("Data has been appended to 'apple.csv'.")


# Read data from the CSV file
with open('apple.csv', 'r', newline='') as file:
    reader = csv.reader(file)

    # Iterate through each row in the CSV file
    for row in reader:
        print(row)
    

# Open the CSV file in append mode
with open('apple.csv', 'a', newline='') as file:
    writer = csv.writer(file)

    # Tuple to be added to the CSV file
    tup = ("Bob", 20)

    # Write the tuple as a new row in the CSV file
    writer.writerow(tup)

print("Data has been appended to 'apple.csv'.")
