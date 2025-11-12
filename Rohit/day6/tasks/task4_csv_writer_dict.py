import csv
employees = [				
    {"id": 201,	 "name": "Suresh"	, "department": "Sales"	, "salary": 58000}	,
    {"id": 202,	 "name": "Meena"	, "department": "IT"	, "salary": 72000}	,
    {"id": 203,	 "name": "Amit"	, "department": "HR"	 ,"salary": 64000}	
]	

# step1 :create or open CSV file in write mode

with open('employee_dict_data.csv', mode='w',newline='') as file:
    # step2: create the fieldname(header)
    header = ["id","name","department","salary"]
    
    # step3 :create a dictwriter object
    writer = csv.DictWriter(file,fieldnames=header)
    
    # step4: write the header to the csv file 
    writer.writeheader()
    
    # step5 write the employee data to csv file 
    writer.writerows(employees)
    
print("===========CSV writing with dictionary completed===========")