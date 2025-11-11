import csv

#data to write
data=[["id","name","department","salary"],
[101,"Arun","IT",70000],
[102,"Riya","HR",65000],
[103,"John","Finance",60000],
[104,"Neha","Marketing",55000]]

#open the file for writing
with open("employee_data02.csv",mode="w",newline="") as file:
    csv_writer=csv.writer(file)
    csv_writer.writerows(data)

print("=== CSV WRITING COMPLETED ===")

#Sample output
#=== CSV WRITING COMPLETED ===
 
#employee_data02.csv
#  id,name,department,salary
# 101,Arun,IT,70000
# 102,Riya,HR,65000
# 103,John,Finance,60000
# 104,Neha,Marketing,55000

#data to write
employees=[
    {"id":201,"name":"shyam","department":"IT","salary":50000},
    {"id":202,"name":"sunder","department":"Sales","salary":60000},
    {"id":203,"name":"reddy","department":"HR","salary":40000}
]

#step 1 :create or open a csv file in write mode
with open("employee_dict_data.csv",mode="w",newline="") as file:
    #step 2:create the filedname(header)
    header=["id","name","department","salary"]

    #step 3: create a Dictwriter object
    writer=csv.DictWriter(file,fieldnames=header)
    
    #step 4: write the header to csv file
    writer.writeheader()
    
    #step 5: write the employee data to the csv file
    writer.writerows(employees)

print("=== csv writing with dictionary completed ===")
     
#sample output
# === csv writing with dictionary completed ===
#employee_dict_data.csv
# id,name,department,salary
# 201,shyam,IT,50000
# 202,sunder,Sales,60000
# 203,reddy,HR,40000


#opening the csv file in read mode
with open("employee_dict_data.csv","r") as file:
    #opening in DictReader
    reader=csv.DictReader(file)
    
    #for printing the rows
    for row in reader:
        print(row)
        
#Sample output
# {'id': '201', 'name': 'shyam', 'department': 'IT', 'salary': '50000'}
# {'id': '202', 'name': 'sunder', 'department': 'Sales', 'salary': '60000'}
# {'id': '203', 'name': 'reddy', 'department': 'HR', 'salary': '40000'}