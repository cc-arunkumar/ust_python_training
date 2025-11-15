# Task 2:

# Count how many employees belong to the IT department.

import csv

# Reading csv file
with open('employee_data.csv', mode='r') as file:
    csv_reader = csv.reader(file)   # create a CSV reader object
    
    # Skip header row (first line of column names)
    next(csv_reader, None)
    
    # Initialize counter for IT department employees
    it_count = 0
    
    # Loop through each row in the CSV file
    for row in csv_reader:
        department = row[2].strip().lower()   # get department column, clean spaces, convert to lowercase
        if department == 'it':                # check if department is IT
            it_count += 1                     # increment counter
    
    # Print the final count of IT employees
    print(f"Number of employees in IT department: {it_count}")


# Output
# Number of employees in IT department: 1