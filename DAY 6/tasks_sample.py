import csv

with open("DAY 6/employee_data01.csv", "r") as file:
    csv_reader=csv.reader(file)
    header=next(csv_reader)  
    next(csv_reader) 
    filtered_rows=[]
    
    it_count = 0  
    for row in csv_reader:
        # Print only those employees whose salary is greater than 60000.
        if int(row[3])>60000:
            print("High Salary:",row)
            filtered_rows.append(row)
        # Count how many employees belong to the IT department.
        if row[2]=="IT":
            it_count+=1

print("Total number of employees in IT:", it_count)

#Write the filtered data (salary > 60000) into a new file high_salary.csv
with open("DAY 6/high_salary.csv","w",newline="") as file:
    csv_writer=csv.writer(file)
    csv_writer.writerow(header)  
    csv_writer.writerows(filtered_rows)

print("Filtered data high_salary.csv")


"""
SAMPLE OUTPUT

High Salary: ['102', 'Riya', 'HR', '65000']
Total number of employees in IT: 0
Filtered data high_salary.csv
"""