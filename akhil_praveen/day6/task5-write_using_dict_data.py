# write using dictionary data
import csv
# actual data
employees = [
    {"id": 201, "name": "Suresh", "department": "Sales", "salary": 58000},
    {"id": 202, "name": "Meena", "department": "IT", "salary": 72000},
    {"id": 203, "name": "Amit", "department": "HR", "salary": 64000}
]

# creating file and opening to write
with open("empl_dict_data.csv","w",newline="") as file:
    # creating header
    header = employees[0].keys()
    
    # create dictwriter object
    csv_file = csv.DictWriter(file,fieldnames=header)
    
    # write the header into the csv file
    csv_file.writeheader()
    
    # write the actual data into the csv file
    csv_file.writerows(employees)
    

with open("empl_dict_data.csv","r",newline="") as file:    
    csv_read = csv.DictReader(file)
    for row in csv_read:
        print(row)
    
print("=== csv writing using dictwriter completed ===")
    
# Output

# === csv writing using dictwriter completed ===

# output from created file

# id,name,department,salary
# 201,Suresh,Sales,58000
# 202,Meena,IT,72000
# 203,Amit,HR,64000
