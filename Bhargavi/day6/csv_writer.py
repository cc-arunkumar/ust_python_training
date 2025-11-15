
# Program: CSV Writer Example


# Description:
# This program demonstrates how to write employee data into a CSV file 
# using Python's csv.writer. The data is stored in a list of lists, 
# where the first row represents the header and the following rows 
# represent employee records.

import csv

# Data to write into the CSV file
data = [
    ["id", "name", "department", "salary"],   # header row
    [101, "Bhargavi", "IT", "20000"],         # employee record 1
    [102, "Meena", "IT", "300000"],           # employee record 2
    [103, "shero", "banking", "200000"]       # employee record 3
]

# Step 1: Open the CSV file in write mode
with open('employee_data2.csv', mode='w', newline='') as file:
    # Step 2: Create a CSV writer object
    csv_writer = csv.writer(file)
    
    # Step 3: Write all rows (header + data) into the file
    csv_writer.writerows(data)

# Confirmation message
print("csv writing completed")

#output
# csv writing completed

#output in the employee_data2.csv
# id,name,department,salary
# 101,Bhargavi,IT,20000
# 102,Meena,IT,300000
# 103,shero,banking,200000
