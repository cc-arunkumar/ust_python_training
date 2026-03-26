import csv

employees = [
    {"id": 201, "name": "Suresh", "department": "Sales", "salary": 58000},
    {"id": 202, "name": "Meena", "department": "IT", "salary": 72000},
    {"id": 203, "name": "Amit", "department": "HR", "salary": 64000}
]

with open("DAY 6/employee_dict_data.csv","w",newline="") as file:
    header=["id","name","department","salary"]

    writer = csv.DictWriter(file,fieldnames=header)

    writer.writeheader()
    writer.writerows(employees)

print("CSV Writing in Dictionary Done")


# Dict Reader

with open("DAY 6/employee_dict_data.csv","r") as f:
    csv_reader=csv.DictReader(f)

    for row in f:
        print(row)