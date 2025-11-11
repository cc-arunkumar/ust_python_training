# Questions:
# - What format is the CSV file in (e.g., what columns does it contain)?
# - Are there any specific conditions for filtering or processing the employee data?
# - Should the data be processed or saved elsewhere after reading?

import csv

# Open the CSV file in read mode
with open("employee_data01.csv", mode='r') as file:
    # Create a CSV reader object
    csv_reader = csv.reader(file)
    
    # Skip the header row (first row in the file)
    next(csv_reader)
    
    # Loop through the remaining rows and print them
    for row in csv_reader:
        print(row)

# Sample output:
#     ['101', 'John Doe', 'Marketing', '50000']
# ['102', 'Jane Smith', 'Engineering', '75000']
# ['103', 'Tom Brown', 'HR', '45000']
# ['104', 'Amy White', 'Engineering', '80000']
