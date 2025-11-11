import csv
# Data to write
employees = [				
    {"id": 201,	 "name": "Suresh",	 "department": "Sales",	 "salary": 58000},	
    {"id": 202,	 "name": "Meena",	 "department": "IT",	 "salary": 72000},	
    {"id": 203,	 "name": "Amit",	 "department": "HR",	 "salary": 64000}	
]				


#Writing csv file using Dictwriter

#step 1 create a new csv file in write mode

# with open("employee_dict_data.csv","w",newline='') as file:
    
#     #step 2: Create a feild names (header)
#     header=["id","name","department","salary"]
    
#     #step 3: create a Dictwriter object
#     writer=csv.DictWriter(file,fieldnames=header)
    
#     #step 4: write the header to csv file
#     writer.writeheader()
    
#     #step 5 : write the employees data to the CSV File
#     writer.writerows(employees)
    
# print("=== CSv Writing with dictionary completed===")



#Reading CSV file using DictReader

# with open('employee_dict_data.csv',"r") as file:
#     csv_dict_reader = csv.DictReader(file)
    
#     for row in csv_dict_reader:
#         print(row)
# print