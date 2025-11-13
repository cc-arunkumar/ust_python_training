#task 1 find employee name using employee salary
#importing csv
import csv
#opening the csv file in read mode
with open("employee_data.csv",'r') as file:
    csv_reader=csv.DictReader(file)
    for row in csv_reader:
        if(float(row['salary']) > 60000):
            print(row['name'])

#Sample Exception
# Arun
# Riya