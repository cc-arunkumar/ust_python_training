#importing csv 
import csv

#reading csv file 
with open("employee_data.csv","r") as file:
    csv_reader= csv.reader(file)
    
    next(csv_reader)
    
    for row in csv_reader:
        print(row)
        
#Output
# ['101', 'Arun', 'IT', '70000']
# ['102', 'Riya', 'HR', '65000']     
# ['103', 'John', 'Finance', '60000']
# ['104', 'Neha', 'Marketing', '55000']

    #Create a dict writer object
    reader = csv.DictReader(file)
    
    for row in reader:
        print(row)
        
#Output
# {'id': '201', 'name': 'Suresh', 'department': 'Sales', 'salary': '50000'}
# {'id': '202', 'name': 'Meena', 'department': 'IT', 'salary': '72000'}
# {'id': '203', 'name': 'Amit', 'department': 'HR', 'salary': '64000'} 

