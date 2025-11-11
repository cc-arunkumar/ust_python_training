# reading from the dictionary  using the csv operations and dictwriter
employees = [
    {"id": 201, "name": "Suresh", "department": "Sales", "salary": 58000},
    {"id": 202, "name": "Meena", "department": "IT", "salary": 72000},
    {"id": 203, "name": "Amit", "department": "HR", "salary": 64000}
]

# importing the csv
import csv


# opening the csv file in the write mode
with open("employee_data02.csv","w",newline='') as file:
    # declaring the header with fieldnames
    header=["id","name","department","salary"]
    # using the dictwriter for writing the values into the csv output file
    writer=csv.DictWriter(file,fieldnames=header)
    # writing the header
    writer.writeheader()
    # writing the dictionary of employee values into th eoutput csv file
    writer.writerows(employees)
    
print("====csv writing with dcitionary is completed")



with open("employee_data02.csv","r") as file:
    csv_dict_reader=csv.DictReader(file)
    for row in csv_dict_reader:
        print(row)

#======sample execution===========
# id,name,department,salary
# 201,Suresh,Sales,58000
# 202,Meena,IT,72000
# 203,Amit,HR,64000

