# Task 2:

# Count how many employees belong to the IT department.
# Step 1: Import the csv module
import csv

# Step 2: Open the CSV file and prepare to read its contents
with open('employee_data.csv', mode='r') as file:
    csv_reader = csv.reader(file)

# Step 3: Skip header and count employees in IT department
    next(csv_reader)
    count = 0
    for row in csv_reader:
        if row[2] == "IT":
            count += 1

    print("The number of employees belongs to IT", count)
    
    
    # sample output
    # The number of employees belongs to IT 1