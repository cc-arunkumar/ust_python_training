
# Print only those employees whose salary is greater than 60000.

import csv

# step1:Open the CSV file for reading
with open('employee_data.csv', mode='r') as file:
    csv_reader = csv.reader(file)

    # step2:Skip the header row
    next(csv_reader)

    for row in csv_reader:
        # step3:Convert salary to float for comparison
        salary = float(row[3])

        # step4:Check if salary is greater than 60000
        if salary > 60000:
            print("the greater than", row)



# sample output
# the greater than ['101', 'Arun', 'IT', '70000']
# the greater than ['102', 'Riya', 'HR', '65000']
        