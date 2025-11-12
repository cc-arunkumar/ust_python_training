import csv

#Data to write
employees = [
    {"id":201,"name":"Suresh","department":"Sales","salary":"58000"},
    {"id":202,"name":"Meena","department":"IT","salary":"72000"},
    {"id":203,"name":"Amit","department":"HR","salary":"64000"}
    ]

#Step1: Create or open the csv file in write mode
with open('employee_dict_data.csv',mode = 'w',newline = '')as file:
    
    #step2: Create the DictWriter object
    header = ["id" , "name","department","salary"]
    
    #step3: create a DictWriter object
    writer = csv.DictWriter(file, fieldnames=header)
    
    #step4: write the header to the csv file
    writer.writeheader()
    
    #step5:write the employees data to the csv file
    writer.writerows(employees)
    
print("=== CSV Writing with the Dictionary Completed===")

# === CSV Writing with the Dictionary Completed===


#Reading CSV file using DictReader
with open('employee_dict_data.csv',mode ='r')as file:
    csv_dict_reader = csv.DictReader(file)
    
    for row in csv_dict_reader:
        print(row)
        
print