import csv

# Reading csv file
with open('employee_data.csv', mode='r') as file:
    csv_reader = csv.reader(file)
    
    # Safely skip header if present
    next(csv_reader)
    
    for row in csv_reader:
        print(row)
