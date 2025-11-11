# employees salary greater than 60000
import csv

with open("employee_data.csv","r") as file:
    csv_reader = csv.reader(file)
    
    
    # remove first row
    next(csv_reader)
    
    print("Employees whose salary greater than 60000: ")
    
    # iterating through each row of data
    for row in csv_reader:
        if int(row[3])>60000:
            print(row[1])
            
# output

# Employees whose salary greater than 60000: 
# Arun
# Riya