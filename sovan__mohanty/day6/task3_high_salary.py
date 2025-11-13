#Task 3: Write the filtered data (salary > 60000) into a new file high_salary.csv
#importing csv
import csv
#opening employees.csv in read mode and high_salary.csv in write mode
with open('employee_data.csv', 'r') as infile, open('high_salary.csv', 'w', newline='') as outfile:
    reader = csv.DictReader(infile)
    fieldnames = reader.fieldnames
    writer = csv.DictWriter(outfile, fieldnames=fieldnames)
    writer.writeheader()
    #reading the file line by line
    for row in reader:
        if int(row['salary']) > 60000:
            writer.writerow(row)
#Completed the CSV file and written in high_salary.csv
