#task:2

#Count how many employees belong to the IT department.

import csv

# Initialize a counter for IT department employees
it_count = 0

# Open the file in read mode
with open('employee_data.csv', mode='r') as file:
    # Create a CSV reader object
    csv_reader = csv.DictReader(file)
    
    # Loop through each row in the CSV
    for row in csv_reader:
        # Check if the department is IT
        if row['department'] == 'IT':
            it_count += 1  # Increment the count for IT department employees

# Print the total number of employees in the IT department
print(f"Number of employees in the IT department: {it_count}")


#o/p:
# Number of employees in the IT department: 1