import csv

with open("employee_data01.csv","r") as file:
    csv_reader=csv.reader(file)
    next(csv_reader)
    
    count=0
    for line in csv_reader:
        
#Task 1:

# Print only those employees whose salary is greater than 60000.

        if int(line[3])>60000:
            print(line)

# Task 3:

# Write the filtered data (salary > 60000) into a new file high_salary.csv.            

            with open("high_salary.csv","a") as f:
                f.write(f"{line[0]},{line[1]},{line[2]},{line[3]}\n")

# Task 2:

# Count how many employees belong to the IT department.            
        if line[2]=="IT":
            count+=1
    print("Number of employees in IT: ",count)
  
  
#Sample output
  
# ['101', 'Arun', 'IT', '70000']
# ['102', 'Riya', 'HR', '65000']
# Number of employees in IT:  1
    
#Sample high_salary.csv
# 101,Arun,IT,70000
# 102,Riya,HR,65000