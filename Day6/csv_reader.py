# CSV file ==> A Comma Separated Values file
import csv

path_data = r"Day6\employee_data01.csv"

# Reading CSV file
with open(path_data, 'r') as file:
    csv_reader = csv.reader(file)
    
    # Remove header from CSV File
    next(csv_reader)
    
    for row in csv_reader:
        print(row)

# sample output:

# ['101', 'Arun', 'IT', '70000']
# ['102', 'Riya', 'HR', '65000']
# ['103', 'John', 'Finance', '60000']
# ['104', 'Neha', 'Marketing', '55000']