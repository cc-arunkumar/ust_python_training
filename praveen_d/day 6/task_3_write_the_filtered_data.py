import csv
# TASK 3:write the filtered data (salary>60000) 
# into a new file high_salary.csv

# id,name,department,salary
# 101,Arun,IT,70000
# 102,Riya,HR,65000
# 103,John,Finance,60000
# 104,Neha,Marketing,55000
import csv

# Read employee data and write only those with salary > 60000
with open('employee_data01.csv', mode='r') as file:
    csv_reader = csv.reader(file)
    header = next(csv_reader)  # skip header row

    with open('high_salary.csv', mode='w', newline='') as s_file:
        writer = csv.writer(s_file)
        writer.writerow(header)  # write header first

        for line in csv_reader:
            # Convert salary to int and check condition
            try:
                if int(line[3]) > 60000:
                    writer.writerow(line)
            except ValueError:
                # Skip if salary is not a valid number
                continue

print("high_salary.csv file created successfully!")
