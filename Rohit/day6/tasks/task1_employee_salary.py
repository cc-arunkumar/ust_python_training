# Task 1:

# Print only those employees whose salary is greater than 60000.



import csv


# step1 :create or open CSV file in read mode
with open('employee_data.csv', mode='r') as file:
    
    
# step2 :create a csv_reader object
    csv_reader =csv.reader(file)
    # step3: it will iterate to next line and wil skip the first line
    next(csv_reader)
    
    
    # step4: each line will be traversed 
    for row in csv_reader:
        # print(row[3])
        
        
        # step5 : printing the row's whose salary is greater than 60000
        if int(row[3])>60000:
            print(row)
            
            
            
# # ======sample output=================
# ['101', 'Arun', 'IT', '70000']
# ['102', 'Riya', 'HR', '65000']
        
    
    
    
    