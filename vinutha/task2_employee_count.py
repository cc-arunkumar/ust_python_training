# # Task 2:
# Count how many employees belong to the IT department.
import csv

#initialization of count variable
it_count = 0

# Reading CSV file
with open('employee_data.csv', mode='r') as file:
    # Create a CSV reader object
    csv_reader = csv.DictReader(file)
    
    # Loop through each row in the CSV
    for row in csv_reader:
        # Check if the department is IT
        if row['department'] == 'IT':
            it_count += 1  # Increment the count for IT department employees

# Print the total number of employees in the IT department
print(f"Number of employees in the IT department: {it_count}")

#Sample output:
# PS C:\Users\Administrator\Desktop\Training\ust_python_training\vinutha\day6> & "C:/Program Files/Python314/python3.14t.exe" c:/Users/Administrator/Desktop/Training/ust_python_training/vinutha/day6/task2_employee_count.py    
# Number of employees in the IT department: 1
# PS C:\Users\Administrator\Desktop\Training\ust_python_training\vinutha\day6> 


