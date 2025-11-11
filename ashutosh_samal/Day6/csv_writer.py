import csv
#Data to write
employees = [
    {"id": 201, "name": "Suresh", "department": "Sales", "salary": 58000},
    {"id": 202, "name": "Meena", "department": "IT", "salary": 72000},
    {"id": 203, "name": "Amit", "department": "HR", "salary": 64000}
]

#Step1: Create a CSV file in write mode
with open("employee_dict_data.csv","w",newline='') as file:
    
    #Step2: Create fieldnames (headers)
    headers = ["id","name","department","salary"]
    
    #Step3: Create a dictionary object
    writer = csv.DictWriter(file,fieldnames=headers)
    
    #Step4: Write the header to the csv file
    writer.writeheader()
    
    #step5: Write the data into the csv file
    writer.writerows(employees)
    
print("==== CSV Writing with Dictionary Completed ====")