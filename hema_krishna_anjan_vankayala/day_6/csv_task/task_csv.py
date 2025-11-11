# Task 1:
# Print only those employees whose salary is greater than 60000.
import csv 
with open("employee_data01.csv",'r') as file:
    csv_read = csv.reader(file)
    
    #Remove Header from CSV
    next(csv_read)
    
    for row in csv_read:
        if int(row[3])>60000:
            print(row[1])
            
# Sample Output 
# Arun
# Riya
            
# Task 2:
# Count how many employees belong to the IT department.
with open("employee_data01.csv",'r') as file:
    csv_read = csv.reader(file)
    next(csv_read)
    count = 0 
    for row in csv_read:
        if row[2]=="IT":
            count += 1 
    print("Employees in IT Department:", count)

#Sample Output
#Employees in IT Department: 1

# Task 3:
# Write the filtered data (salary > 60000) into a new file high_salary.csv.
with open("employee_data01.csv",'r') as file:
    csv_read = csv.reader(file)
    li=[]
    #Remove Header from CSV
    next(csv_read)
    
    for row in csv_read:
        if int(row[3])>60000:
            li.append(row)

with open('high_salary.csv','w') as file:
    for i in li:
        file.write(",".join(i)+"\n")
    print("File Created Successfully!")

#Sample Output
#File Created Successfully!