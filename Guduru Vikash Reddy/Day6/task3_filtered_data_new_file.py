# Task 3:

# Write the filtered data (salary > 60000) into a new file high_salary.csv.
import csv  # Step 1: Import CSV module

data = []

# Step 2: Read data from employee_data.csv
with open("employee_data.csv", 'r') as file:
    csv_reader = csv.reader(file)
    next(csv_reader)  # Skip header
    for row in csv_reader:
        data.append(row)

# Step 3: Write filtered data to filtered_data.csv
with open("filtered_data.csv", "w", newline='') as file:
    csv_writer = csv.writer(file)

# Step 4: Filter employees with salary > 60000
    for i in data:
        salary = float(i[3])
        if salary > 60000:
            csv_writer.writerow(i)


# sample output
# 101,Arun,IT,70000
# 102,Riya,HR,65000