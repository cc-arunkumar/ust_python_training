import csv

data = [
    ["id", "name", "department", "salary"],   # header row
    [101, "Arun", "IT", 70000],
    [102, "Riya", "HR", 65000],
    [103, "John", "Finance", 60000],
    [104, "Neha", "Marketing", 55000]
]

with open("employee_data01.csv","w",newline="") as new_file:
    new_csv = csv.writer(new_file)
    for d in data:
        new_csv.writerow(d)