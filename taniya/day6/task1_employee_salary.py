# Task 1:

# Print only those employees whose salary is greater than 60000.
import csv
# Opening the file
with open('employee_data.csv') as file:
    csv_reader = csv.reader(file)
    next(csv_reader)
    
    for row in csv_reader:
       if int(row[3])>60000:
          print(row)
          
# output
# ['101', 'Arun', 'IT', '70000']
# ['102', 'Riya', 'HR', '65000']
            
            
              