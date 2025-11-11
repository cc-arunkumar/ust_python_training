import csv

# the program prints the details of the employees having salary more than 60000

with open("employee_data01.csv","r")as file:
    reader=csv.reader(file)
    next(reader)
    for row in reader:
        
        id,name,department,salary=row
        salary=float(salary)
        if salary>60000:
            print(f"{id} |{name} |{department} | has salary more than 60000 with salary {salary}" )
            

# 101 |Arun |IT | has salary more than 60000 with salary 70000.0
# 102 |Riya |HR | has salary more than 60000 with salary 65000.0