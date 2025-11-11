import csv

data=[
    ["id", "name","dept","salary"],
    [101,"Arun","IT",70000],
    [102,"Riya","HR",65000],
    [103,"John","Finance",60000],
    [104,"Neha","Marketing",55000]
]

#Writing to csv

with open("employee_data02.csv", "w", newline='') as file:
    csv_writer=csv.writer(file)
    
    csv_writer.writerows(data)
print("====CSV completed=====")

#Data to write

employees =[
    {"id": 201,"name": "Suresh", "department": "Sales","salary": 50000},
    {"id": 202,"name": "Meena", "department": "IT","salary": 72000},
    {"id": 203,"name": "Amit", "department": "HR","salary": 64000},
]

# #Create your own csv file

with open("employee_dict_data.csv", "w", newline='') as file:
    
    #Create fieldnames header
    header=["id","name","department","salary"]
    
    #Step 3 : Create a dictwriter object
    writer = csv.DictWriter(file,fieldnames=header)
    
    #Step 4 : write the header to csv
    writer.writeheader()
    
    #Step 5 : Write the employee data to csv file 
    writer.writerows(employees)
print("===Csv writing completed=====")



# Dict Reader 

employees =[
    {"id": 201,"name": "Suresh", "department": "Sales","salary": 50000},
    {"id": 202,"name": "Meena", "department": "IT","salary": 72000},
    {"id": 203,"name": "Amit", "department": "HR","salary": 64000},
]
with open("employee_dict_data.csv", "r", newline='') as file:
    
    #Create a dict writer object
    reader = csv.DictReader(file)
    
    for row in reader:
        print(row)
        
#Output
# {'id': '201', 'name': 'Suresh', 'department': 'Sales', 'salary': '50000'}
# {'id': '202', 'name': 'Meena', 'department': 'IT', 'salary': '72000'}
# {'id': '203', 'name': 'Amit', 'department': 'HR', 'salary': '64000'} 
    
