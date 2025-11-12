import csv
employees = [				
    {"id": 201,	 "name": "Suresh"	, "department": "Sales"	, "salary": 58000}	,
    {"id": 202,	 "name": "Meena"	, "department": "IT"	, "salary": 72000}	,
    {"id": 203,	 "name": "Amit"	, "department": "HR"	 ,"salary": 64000}	
]	



# step1 :create or open CSV file in read mode
with open('employee_dict_data.csv', mode='r') as file:
    # step2 :create a DictReader object
    csv_dict_reader = csv.DictReader(file)
    # step5: print row while iterating
    for row in csv_dict_reader:
        print(row)
        
        
        
# ==========sample output==============
# {'id': '101', 'name': 'Arun', 'department': 'IT', 'salary': '70000'}
# {'id': '102', 'name': 'Riya', 'department': 'HR', 'salary': '65000'}
# {'id': '103', 'name': 'John', 'department': 'Finance', 'salary': '60000'}
# {'id': '104', 'name': 'Neha', 'department': 'Marketing', 'salary': '55000'}