# CSV file => A comma separated values file

import csv

# Reading csv file
with open('employee_data01.csv',mode='r') as file:
    csv_reader=csv.reader(file)
    
    next(csv_reader)
    
    for row in csv_reader:
        print(row)

# Sample output
# ['101', 'Arun', 'IT', '70000']
# ['102', 'Riya', 'HR', '65000']
# ['103', 'John', 'Finance', '60000']
# ['104', 'Neha', 'Marketing', '55000']


# Reading csv file using DictReader

with open("employee_dictdata.csv","r") as file:
    csv_dict_reader=csv.DictReader(file)
    for row in csv_dict_reader:
        print(row)

# Sample output
# {'id': '201', 'name': 'Suresh', 'department': 'Sales', 'salary': '58000'}
# {'id': '202', 'name': 'Meena', 'department': 'IT', 'salary': '72000'}
# {'id': '203', 'name': 'Amit', 'department': 'HR', 'salary': '64000'}

        