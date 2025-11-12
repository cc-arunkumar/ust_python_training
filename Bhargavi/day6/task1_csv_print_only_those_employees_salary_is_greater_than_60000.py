# Task 1:

# Print only those employees whose salary is greater than 60000.

import csv

# Open the file in read mode
with open('employee_data.csv', mode='r') as file:
    
    # Create a CSV reader object
    csv_reader = csv.DictReader(file)
    
    # Loop through each row in the CSV
    for row in csv_reader:
        
        # Check if the salary is greater than 60000
        if float(row['salary']) > 60000:
            
            
            # Print the employee's information
            print(f"Employee Name: {row['name']}, salary: {row['salary']}")
            
# Output            
# Employee Name: Arun, salary: 70000
# Employee Name: Riya, salary: 65000