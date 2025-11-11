import csv
with open('employee_data01.csv', mode='r') as file:
    csv_reader = csv.reader(file)

    next(csv_reader)
    for id,name,department,salary in csv_reader:
        salary=float(salary)
        if salary > 60000:
            print(f"the {id} has greater salary than 60000---{salary}")
            
# the 101 has greater salary than 60000---70000.0
# the 102 has greater salary than 60000---65000.0