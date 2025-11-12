# Task 2:

# Count how many employees belong to the IT department
import csv


# step1 :create or open CSV file in read mode
with open('employee_data.csv', mode='r') as file:
    count =0
       
# step2 :create a csv_reader object
    csv_reader =csv.reader(file)
    # step3: it will iterate to next line and wil skip the first line
    next(csv_reader)
    
    # step4: each line will be traversed 
    for row in csv_reader:
        
        
        #  step5 : counting and printing the row's whose department is IT
        if row[2]=='IT':
            count+=1
    print("count is ",count)
    
    
# ================sample output==============
# count is  1