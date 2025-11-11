# data = [
#     ["id", "name", "department", "salary"],   # header row
#     [101, "Arun", "IT", 70000],
#     [102, "Riya", "HR", 65000],
#     [103, "John", "Finance", 60000],
#     [104, "Neha", "Marketing", 55000]
# ]
import csv 

# with open('employee_data01.csv','w',newline='') as file:

#     csv_write = csv.writer(file)

#     csv_write.writerows(data)

#     print("Created CSV File Succesfully!")

employees = [
    {"id": 201, "name": "Suresh", "department": "Sales", "salary": 58000},
    {"id": 202, "name": "Meena", "department": "IT", "salary": 72000},
    {"id": 203, "name": "Amit", "department": "HR", "salary": 64000}
]

with open('employee_dict_data.csv','w',newline='') as file:
    #Create the fieldnames list
    header = ['id','name','department','salary']
      
    #Create a DictWriter object
    writer = csv.DictWriter(file,fieldnames=header)

    #write the header to csv
    writer.writeheader()
    
    #write the employee names in csv
    writer.writerows(employees)

#Read Operaation with Dictionary
with open('employee_dict_data.csv','r') as file:
    csv_reader = csv.DictReader(file)
    for rows in csv_reader:
        print(rows)