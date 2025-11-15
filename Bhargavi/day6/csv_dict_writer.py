# Program: CSV DictWriter Example

# Description:
# This program demonstrates how to write employee data into a CSV file 
# using Python's csv.DictWriter and then read it back using csv.DictReader.
# DictWriter allows writing rows as dictionaries, while DictReader reads them back as dictionaries.


import csv

# Data to write into the CSV file
employees = [
    {"id": 201, "name": "Suresh", "department": "Sales", "salary": "58000"},
    {"id": 202, "name": "Meena", "department": "IT", "salary": "72000"},
    {"id": 203, "name": "Amit", "department": "HR", "salary": "64000"}
]

# Step 1: Create or open the CSV file in write mode
with open('employee_dict_data.csv', mode='w', newline='') as file:
    
    # Step 2: Define the header fields
    header = ["id", "name", "department", "salary"]
    
    # Step 3: Create a DictWriter object
    writer = csv.DictWriter(file, fieldnames=header)
    
    # Step 4: Write the header row to the CSV file
    writer.writeheader()
    
    # Step 5: Write the employee data rows to the CSV file
    writer.writerows(employees)

print("=== CSV Writing with the Dictionary Completed ===")

with open('employee_dict_data.csv', mode='r') as file:
    csv_dict_reader = csv.DictReader(file)
    
    # Loop through each row and print as dictionary
    for row in csv_dict_reader:
        print(row)

#output
# === CSV Writing with the Dictionary Completed===
# {'id': '201', 'name': 'Bhargavi', 'department': 'Sales', 'salary': '58000'}
# {'id': '202', 'name': 'Meena', 'department': 'IT', 'salary': '72000'}
# {'id': '203', 'name': 'shero', 'department': 'HR', 'salary': '64000'}