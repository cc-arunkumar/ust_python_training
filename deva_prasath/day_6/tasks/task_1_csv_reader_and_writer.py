# Task 1

# Print only those employees whose salary is greater than 60000.

import csv

# Reading CSV file
with open('deva_prasath\day-6\employee_data.csv', mode='r') as file:
    csv_reader = csv.reader(file)
    # Remove header from CSV File
    
    next(csv_reader)
    #initialising count variable to 0
    count=0
    for row in csv_reader:
        #invalid literal error so changing to int
        if int(row[3])>60000:  
            print("Salary greater than 60000: ",row)
            
#Sample output
# Salary greater than 60000:  ['101', 'Arun', 'IT', '70000']
# Salary greater than 60000:  ['102', 'Riya', 'HR', '65000'] 


#-------------------------------------------------------------------------------#
# Task 2:

# Count how many employees belong to the IT department.

#opening in read mode
with open('deva_prasath\day-6\employee_data.csv', mode='r') as file:
    csv_reader = csv.reader(file)
    for i in csv_reader:
        if i[2]=="IT":
            count+=1  #incrementing count
    print("Number of IT employees ",count)
    
#Sample output
# Number of IT employees  1


#---------------------------------------------------------------------------------------#
# Task 3:

# Write the filtered data (salary > 60000) into a new file high_salary.csv.

#opening in read mode
with open('deva_prasath\day-6\employee_data.csv', mode='r') as file:
    #storing in this variable
    csv_reader = csv.reader(file)
    next(csv_reader)
    for row in csv_reader:
        if int(row[3])>60000:
            #writing in a new file with append mode
            with open('high_salary.csv',mode='a') as f1: 
                
            #write argument must be string so converting to string
                f1.write(f"{str(row)}\n")
                
    print("The high salary values are dumped in high_salry.csv\n")
        
#Sample output
# The high salary values are dumped in high_salry.csv
