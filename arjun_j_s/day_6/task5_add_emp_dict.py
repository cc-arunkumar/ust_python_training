import csv

employees = [
    {"id": 201, "name": "Suresh", "department": "Sales", "salary": 58000},
    {"id": 202, "name": "Meena", "department": "IT", "salary": 72000},
    {"id": 203, "name": "Amit", "department": "HR", "salary": 64000}
]

#Open new file in write mode
with open("employee_data03.csv","w",newline="") as new_file:

    #Obtain the header
    header = employees[0].keys()

    #Define the writer for the new_file
    new_csv = csv.DictWriter(new_file,header)

    #Write the header
    new_csv.writeheader()

    #Write the data
    new_csv.writerows(employees)

    new_file.close()

    #Open new file in reader mode
    with open("employee_data03.csv","r") as new_file:

        #Define the reader
        read_csv = csv.DictReader(new_file)

        #Print the data
        for i in read_csv:
            print(i)


#print the completed stmt
print("======Success======")

#Output
# {'id': '201', 'name': 'Suresh', 'department': 'Sales', 'salary': '58000'}
# {'id': '202', 'name': 'Meena', 'department': 'IT', 'salary': '72000'}
# {'id': '203', 'name': 'Amit', 'department': 'HR', 'salary': '64000'}
# ======Success======