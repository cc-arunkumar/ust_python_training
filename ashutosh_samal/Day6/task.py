import csv
#Task 1: Print only those employees whose salary is greater than 60000.
with open("ashutosh_samal\Day6\employee_data01.csv","r") as file:
    csv_reader = csv.reader(file)
    next(csv_reader)
    for row in csv_reader:
        if int(row[3])>60000:
            print(row)
            
#Sample Output
# ['101', 'Arun', 'IT', '70000']
# ['102', 'Riya', 'HR', '65000']


#Task 2: Count how many employees belong to the IT department.
with open("ashutosh_samal\Day6\employee_data01.csv","r") as file:
    csv_reader = csv.reader(file)
    next(csv_reader)
    for row in csv_reader:
        if row[2] == "IT":
            print(row)
            
#Sample Output
# ['101', 'Arun', 'IT', '70000']


# Task 3: Write the filtered data (salary > 60000) into a new file high_salary.csv.
with open("ashutosh_samal\Day6\employee_data01.csv","r") as infile, open('ashutosh_samal\Day6\high_salary.csv','w',newline='') as outfile:
    reader = csv.DictReader(infile)
    fieldnames = reader.fieldnames
    writer = csv.DictWriter(outfile,fieldnames=fieldnames)
    writer.writeheader()
    #reading the file line by line
    for row in reader:
        if int(row['salary'])>60000:
            writer.writerow(row)
#Created the csv file named high_salary.csv