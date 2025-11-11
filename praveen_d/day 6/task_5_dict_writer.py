import csv
# Data to write
employees = [
    {"id": 101, "name": "Arun", "department": "IT", "salary": 70000},
    {"id": 102, "name": "Riya", "department": "HR", "salary": 65000},
    {"id": 103, "name": "John", "department": "Finance", "salary": 60000},
    {"id": 104, "name": "Neha", "department": "Marketing", "salary": 55000}
]

with open('employee_data02.csv','w',newline='') as file:
    header=["id","name","department","salary"]
    csv_dict_writer= csv.DictWriter(file,fieldnames=header)

    csv_dict_writer.writeheader()
    csv_dict_writer.writerows(employees)
   
