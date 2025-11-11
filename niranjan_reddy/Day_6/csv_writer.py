import csv
# Data to write
employees=[
    {"id":201,"name":"Suresh","department":"Sales","salary":58000},
    {"id":202,"name":"Meena","department":"IT","salary":72000},
    {"id":203,"name":"Amit","department":"HR","salary":64000}
]

# Step 1: Create or open a csv file in write mode
with open("employee_dictdata.csv","w",newline='') as file:
    # Step 2: Create the filednames (header)
    header=["id","name","department","salary"]
    
    # Step 3: Create A DictWriter object
    writer=csv.DictWriter(file,fieldnames=header)
    
    # Step 4: Write the header to the csv file
    writer.writeheader()
    
    # Step 5: Write the employee data to the CSV file
    writer.writerows(employees)
    
print("==CSV Writing with Dictionay Complted==")
