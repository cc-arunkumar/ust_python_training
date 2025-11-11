# Data to write
import csv
employees = [
    {"id": 201, "name": "Suresh", "department": "Sales", "salary": 58000},
    {"id": 202, "name": "Meena", "department": "IT", "salary": 72000},
    {"id": 203, "name": "Amit", "department": "HR", "salary": 64000}
]

# Step 1: Create or open a CSV file in write mode
with open("employee_dict_data.csv","w",newline='')as file:
    
    # Step 2: Create the fieldname(header)
    header = ["id","name","department","salary"]
    
    # Step 3: Create a DictWriter object
    writer = csv.DictWriter(file,fieldnames=header)
    
    # Step 4: Write the header to the CSV file
    writer.writeheader()
    
    # Step 5:Write the employee data to the CSV file
    writer.writerows(employees)
    
print("===CSV Writing Completed===")