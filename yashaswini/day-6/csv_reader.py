import csv

#opening the file in read mode
with open('employee_data.csv',mode='r') as file:
    csv_reader=csv.reader(file)
    
    #to remove header from CSV file 
    next(csv_reader)
    
    for row in csv_reader:
        print(row)
        

#o/p:
# ['101', 'Arun', 'IT', '70000']
# ['102', 'Riya', 'HR', '65000']
# ['103', 'John', 'Finance', '60000']
# ['104', 'Neha', 'Marketing', '55000']