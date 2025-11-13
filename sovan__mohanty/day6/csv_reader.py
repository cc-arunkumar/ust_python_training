#CSV file reader of an employee data csv file
import csv
#opening the employee data csv file
with open("employee_data.csv",'r') as file:
    csv_reader=csv.reader(file)
    #removing header from CSV File 
    next(csv_reader)
    for row in csv_reader:
        print(row)
        
#Sample Execution
# ['101', 'Arun', 'IT', '70000']
# ['102', 'Riya', 'HR', '65000']
# ['103', 'John', 'Finance', '60000']
# ['104', 'Neha', 'Marketing', '55000']