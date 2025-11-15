#CSV File ==>Comma Separated Values file

import csv   # Import the CSV module to handle CSV file operations

# Reading CSV File
with open('employee_data01.csv', mode='r') as file:   # Open the CSV file in read mode
    csv_reader = csv.reader(file)   # Create a CSV reader object

    next(csv_reader)   # Skip the header row (first line of the CSV file)

    # Loop through each remaining row in the CSV file
    for row in csv_reader:
        # Each row is returned as a list of values
        print(row)     # Print the row (list of column values)


#sample Output
# PS C:\Users\Administrator\Desktop\Training\ust_python_training\vinutha> & 
# "C:/Program Files/Python314/python3.14t.exe" c:/Users/Administrator/Desktop/Training/ust_python_training/vinutha/day6/csv_reader.py
# ['101', 'Arun', 'IT', '70000']
# ['102', 'Riya', 'HR', '65000']
# ['103', 'John', 'Finance', '60000']
# ['104', 'Neha', 'Marketing', '55000']
# PS C:\Users\Administrator\Desktop\Training\ust_python_training\vinutha> 
