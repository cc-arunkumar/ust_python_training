# Sample employee data represented as a list of dictionaries

import csv
employees = [
    {"id": 201, "name": "Abhi", "department": "Sales", "salary": 58000},  # Employee 1 data
    {"id": 202, "name": "Abzal", "department": "IT", "salary": 75000},    # Employee 2 data
    {"id": 203, "name": "Vikram", "department": "HR", "salary": 65000},   # Employee 3 data
    {"id": 204, "name": "Priya", "department": "Marketing", "salary": 59000}  # Employee 4 data
]

# Open the CSV file in write mode
with open('employee_dict_data.csv', mode='w', newline='') as file:
    # Define the header (column names) for the CSV file
    header = ["id", "name", "department", "salary"]
    
    # Initialize a DictWriter to write dictionaries to the CSV file with the specified headers
    writer = csv.DictWriter(file, fieldnames=header)
    
    # Write the header row to the CSV file
    writer.writeheader()
    
    # Write the employee data to the CSV file, where each dictionary in the list is a row
    writer.writerows(employees)

# Confirmation message for writing to the file
print("**** CSV Writing with Dictionary Completed ****")

# Open the CSV file in read mode
with open('employee_dict_data.csv', mode='r', newline='') as file:
    # Initialize a DictReader to read the CSV file as dictionaries, using the header row as keys
    reader = csv.DictReader(file)
    
    # Loop through each row in the CSV file
    for row in reader:
        print(row)


# Sample output:
#     **** CSV Writing with Dictionary Completed ****
# {'id': '201', 'name': 'Abhi', 'department': 'Sales', 'salary': '58000'}
# {'id': '202', 'name': 'Abzal', 'department': 'IT', 'salary': '75000'}
# {'id': '203', 'name': 'Vikram', 'department': 'HR', 'salary': '65000'}
# {'id': '204', 'name': 'Priya', 'department': 'Marketing', 'salary': '59000'}