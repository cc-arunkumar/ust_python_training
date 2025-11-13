employees = [				
    {"id": 201,	 "name": "Suresh",	 "department": "Sales",	 "salary": 58000},	
    {"id": 202,	 "name": "Meena",	 "department": "IT",	 "salary": 72000},	
    {"id": 203,	 "name": "Amit",	 "department": "HR",	 "salary": 64000}	
]		
import csv
# Step 1: create or open a csv file in write mode
with open('employee_dict_data.csv',mode='r') as file:
    # step 2: reading a file
    csv_dict_reader = csv.DictReader(file)
    
    # step 3:printing file
    for row in csv_dict_reader:
        print(row)
print("CSV WRITING WITH DICTIONARY COMPLETED")
