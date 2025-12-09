
# Program: CSV Reader Example

# Description:
# This program reads employee data from a CSV file using Python's csv.reader.
# It safely skips the header row (column names) and prints each row of data.


import csv

# Step 1: Open the CSV file in read mode
with open('employee_data.csv', mode='r') as file:
    # Step 2: Create a CSV reader object
    csv_reader = csv.reader(file)
    
    # Step 3: Safely skip the header row if present
    next(csv_reader)
    
    # Step 4: Loop through each row in the CSV file
    for row in csv_reader:
        # Print the row (list of values)
        print(row)

#output
# ['101', 'Arun', 'IT', '70000']
# ['102', 'Riya', 'HR', '65000']
# ['103', 'John', 'Finance', '60000']
# ['104', 'Neha', 'Marketing', '55000']
