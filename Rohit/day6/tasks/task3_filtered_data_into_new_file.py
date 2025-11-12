# Task3
# Write the filtered data (salary > 60000) into a new file high_salary.csv.   
import csv


# step1 :create or open CSV file in read mode
with open('employee_data.csv', mode='r') as file:
    
    # step2 :create a csv_reader object
    reader = csv.reader(file)
    
    # step3: it will iterate to next line and wil skip the first line
    header = next(reader)  
  
 # step4 :create or open CSV file in write mode

    with open("high_salary.csv", mode='w', newline='') as second_file:
        # step5  :create a csv_writer object
        
        writer = csv.writer(second_file)
        
        # step5 : header has been updated in the high_salary.csv
        writer.writerow(header)
        
        #  step6 : data has been updated on high_salary.csv  where salary is greater than 60000 
        for row in reader:
            if int(row[3]) > 60000:  
                writer.writerow(row)
                
                
                
                
                
# ================sample output=============
# 101,Arun,IT,70000
# 102,Riya,HR,65000


