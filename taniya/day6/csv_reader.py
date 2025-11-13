# csv file == a comma separated values file
import csv
with open('employee_data.csv',mode = 'r') as file:
    csv_reader = csv.reader(file)
    
    # remove header from csv file
    next(csv_reader)
    for row in csv_reader:
        print(row)
        
# output
# ['101', 'Arun', 'IT', '70000']
# ['102', 'Riya', 'HR', '65000']
# ['103', 'John', 'Finance', '60000']
# ['104', 'Neha', 'Marketing', '55000']
