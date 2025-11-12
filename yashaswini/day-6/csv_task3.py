#task:3

# Write the filtered data (salary > 60000) into a new file high_salary.csv.

import csv

# Open the original employee data file in read mode
with open('employee_data.csv', mode='r') as file:
    
    # Create a CSV reader object
    csv_reader = csv.DictReader(file)
    
    # Open the new file to store the filtered data (salary > 60000)
    with open('high_salary.csv', mode='w', newline='') as outfile:
        
        # Get the fieldnames from the input file (columns)
        fieldnames = csv_reader.fieldnames
        
        # Create a CSV writer object
        csv_writer = csv.DictWriter(outfile, fieldnames=fieldnames)
        
        # Write the header (field names) to the new file
        csv_writer.writeheader()
        
        # Loop through each row in the original CSV file
        for row in csv_reader:
            
            # Check if the salary is greater than 60000
            if float(row['salary']) > 60000:
                
                # Write the row to the new file
                csv_writer.writerow(row)
                
                #printing the employee's information
                print(f"Employee Name: {row['name']}, salary: {row['salary']}")


#o/p:
# Employee Name: Arun, salary: 70000
# Employee Name: Riya, salary: 65000
