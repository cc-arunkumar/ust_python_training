import csv

#The Values that are provided in Dictionary format
employees = [
    {"id": 201, "name": "Suresh", "department": "Sales", "salary": 58000},
    {"id": 202, "name": "Meena", "department": "IT", "salary": 72000},
    {"id": 203, "name": "Amit", "department": "HR", "salary": 64000}
]


#Taking the dictionary values from here and making a new file and dumping the values over there. 
with open('employee_dict_data.csv', 'w', newline='') as file:
    header = ["id", "name", "department", "salary"]
    writer = csv.DictWriter(file, fieldnames=header)
    writer.writeheader()
    writer.writerows(employees)