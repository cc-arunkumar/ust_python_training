#data for csv file
import csv
employees = [
    {"id": 201, "name": "Suresh", "department": "Sales", "salary": 58000},
    {"id": 202, "name": "Meena", "department": "IT", "salary": 72000},
    {"id": 203, "name": "Amit", "department": "HR", "salary": 64000}
]

#create or write a new csv file
with open("Day6\employee_data01.csv","w",newline='') as file:

    #step 2:create the filednames(header)
    header = ["id","name","department","salary"]

    #step 3:create a dict writer object
    writer = csv.DictWriter(file,fieldnames=header)

    #step 4:Write the header to the csv file
    writer.writeheader()

    #step 5:write the employees data to the csv file
    writer.writerows(employees)

print("===CSV write with dictionary completed===")

# sample output:

# ===CSV write with dictionary completed===
