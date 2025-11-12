# Task3
    
# Write the filtered data (salary > 60000) into a new file high_salary.csv.


import csv

with open("employee_data.csv", mode="r") as infile, open("high_salary.csv", mode="w", newline="") as outfile:
    csv_reader = csv.reader(infile)
    csv_writer = csv.writer(outfile)

    header = next(csv_reader)       # read header
    csv_writer.writerow(header)     # write header to new file

    for row in csv_reader:
        if int(row[3]) > 60000:     # salary column
            csv_writer.writerow(row)

print("Filtered data written to high_salary.csv")


# Filtered data written to high_salary.csv
# contents in the high_salary.csv file
# id,name,department,salary
# 101,Arun,IT,70000
# 102,Riya,HR,65000



