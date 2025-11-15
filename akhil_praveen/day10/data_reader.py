import csv

employees = [
    {"id": 201, "name": "Suresh", "department": "Sales", "salary": 58000},
    {"id": 202, "name": "Meena", "department": "IT", "salary": 72000},
    {"id": 203, "name": "Amit", "department": "HR", "salary": 64000}
]
with open("C:/Users/Administrator/Desktop/ust_python_training/akhil_praveen/day10/data/emp_details.csv","w",newline="") as file:
    header = employees[0].keys()
    csv_file1 = csv.DictWriter(file,fieldnames=header)
    csv_file1.writeheader()
    csv_file1.writerows(employees)
    
with open("C:/Users/Administrator/Desktop/ust_python_training/akhil_praveen/day10/data/emp_details.csv","r",) as file:
    csv_file1 = csv.DictReader(file)
    for row in csv_file1:
        print(row)