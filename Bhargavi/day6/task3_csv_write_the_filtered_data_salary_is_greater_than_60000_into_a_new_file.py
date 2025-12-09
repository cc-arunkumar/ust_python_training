# Task 3:

import csv

# Open the input CSV file in read mode and output CSV file in write mode
with open("employee_data.csv", mode="r") as infile, open("high_salary.csv", mode="w", newline="") as outfile:
    csv_reader = csv.reader(infile)   # create a CSV reader object
    csv_writer = csv.writer(outfile)  # create a CSV writer object

    header = next(csv_reader)         # read the header row from input file
    csv_writer.writerow(header)       # write the header row to output file

    # Loop through each row in the input CSV
    for row in csv_reader:
        # Check if salary (column index 3) is greater than 60000
        if int(row[3]) > 60000:
            # Write the row to the new output file
            csv_writer.writerow(row)

# Confirmation message
print("Filtered data written to high_salary.csv")

#output

# Filtered data written to high_salary.csv
#contents in high_slary.csv
# id,name,department,salary
# 101,Arun,IT,70000
# 102,Riya,HR,65000
