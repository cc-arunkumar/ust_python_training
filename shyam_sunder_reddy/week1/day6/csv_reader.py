# CSV file ==> A Comma Separated Values file


import csv


# Reading CSV file
with open('employee_data.csv', mode='r') as file:
    csv_reader = csv.reader(file)
    
    # Remove header from CSV File
    next(csv_reader)
    
    for row in csv_reader:
        print(row)
        
# Sample output:
# ['id', 'name', 'department', 'salary']
# ['101', 'Arun', 'IT', '70000']
# ['102', 'Riya', 'HR', '65000']
# ['103', 'John', 'Finance', '60000']
# ['104', 'Neha', 'Marketing', '55000']

# print("=== CSV Reading Completed ===")

