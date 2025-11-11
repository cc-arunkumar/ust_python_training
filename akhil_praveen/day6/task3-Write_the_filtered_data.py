# Write the filtered data (salary > 60000) into a new file high_salary.csv.
import csv
with open("employee_data01.csv","r") as file:
    with open("high_salary.csv","w",newline="") as file1:
        csv_file = csv.reader(file)
        csv_high = csv.writer(file1)
        for row in csv_file:
            if row[3]=="salary":
                csv_high.writerow(row)
            elif int(row[3])>60000:
                csv_high.writerow(row)
         
# new csv file output 
# id,name,department,salary
# 101,Arun,IT,70000
# 102,Riya,HR,65000