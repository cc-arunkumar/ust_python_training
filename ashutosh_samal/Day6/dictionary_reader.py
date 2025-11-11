#Reading a CSV file using DictReader
import csv
with open("employee_dict_data.csv","r",) as file:
    csv_dict_reader = csv.DictReader(file)
    for row in csv_dict_reader:
        print(row)
        
#Output
# {'id': '201', 'name': 'Suresh', 'department': 'Sales', 'salary': '58000'}
# {'id': '202', 'name': 'Meena', 'department': 'IT', 'salary': '72000'}
# {'id': '203', 'name': 'Amit', 'department': 'HR', 'salary': '64000'} 