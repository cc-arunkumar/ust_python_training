
# Program: CSV DictReader Example

# Description:
# This program reads employee data from a CSV file using Python's csv.DictReader.
# DictReader allows accessing each row as a dictionary with column names as keys.

import csv

# Reading the file
with open('employee_dict_data.csv', mode='r') as file:
    # Create a DictReader object to read rows as dictionaries
    csv_dict_reader = csv.DictReader(file)
    
    # Loop through each row in the CSV file
    for row in csv_dict_reader:
        # Print the row dictionary (keys are column headers)
        print(row)

# Print confirmation after reading is complete
print("CSV Reading complete")


# output
# {'id': '201', 'name': 'Suresh', 'department': 'Sales', 'salary': '58000'}
# {'id': '202', 'name': 'Meena', 'department': 'IT', 'salary': '72000'}
# {'id': '203', 'name': 'Amit', 'department': 'HR', 'salary': '64000'}
# CSV Reading complete