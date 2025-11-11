# writing dictionary data into csv file

import csv

employees = [
    {"id": 201, "name": "Suresh", "department": "Sales", "salary": 58000},
    {"id": 202, "name": "Meena", "department": "IT", "salary": 72000},
    {"id": 203, "name": "Amit", "department": "HR", "salary": 64000}
]


#step 1 : create or open csv file in write mode
with open("employee_dict_data.csv","w",newline='') as file2:
    # step 2 : create the header
    header = ["id","name","department","Sales","salary"]
    
    # step 3 : create dictwriter object
    writer = csv.DictWriter(file2,header)
    
    writer.writeheader()
    
    writer.writerows(employees)
    
print("Writing completed")