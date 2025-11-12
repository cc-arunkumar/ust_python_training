# csv reader
import csv

# Reading csv file
with open('employee_data.csv', mode='r') as file:
    csv_reader = csv.reader(file)
    
    # Safely skip header if present
    next(csv_reader)
    
    for row in csv_reader:
        print(row)


# ['101', 'Arun', 'IT', '70000']
# ['102', 'Riya', 'HR', '65000']
# ['103', 'John', 'Finance', '60000']
# ['104', 'Neha', 'Marketing', '55000']
