#task count how many employee belong to IT department
#importing csv
import csv
#opening the csv in read mode
with open("employee_data.csv",'r') as file:
    csv_reader=csv.DictReader(file)
    #counter initialization
    cout=0
    for row in csv_reader:
        if(row['department']=='IT'):
            cout+=1
    print("Number of employees in IT department",cout)

#Sample Execution
# Number of employees in IT department 1