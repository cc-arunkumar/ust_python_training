# Task 3:

# Write the filtered data (salary > 60000) into a new file high_salary.csv.

import csv
# Opening the file
with open('employee_data.csv') as file:
    csv_reader = csv.reader(file)
    header = next(csv_reader)
# Open file
    with open("high_salary.csv",'w',newline='') as file1:
        file1 = csv.writer(file1)
        file1.writerow(header)
# salary more than 60000 
        for row in csv_reader:
            if int(row[3]) > 60000:
                file1.writerow(row)
                
 