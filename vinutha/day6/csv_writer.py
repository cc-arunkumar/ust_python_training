# Writing data into the file
import csv   # Import the CSV module to handle CSV file operations

# Sample data: a list of lists
# First sublist is the header row (column names)
# Remaining sublists are employee records
data = [
    ["id", "name", "department", "salary"],
    [101, "Vinnu", "IT", "20000"],
    [102, "hima", "IT", "300000"],
    [103, "siri", "banking", "200000"]
]

# Writing the data into a CSV file
with open('employee_data2.csv', mode='w', newline='') as file:
    # Create a CSV writer object
    csv_writer = csv.writer(file)

    # Write all rows (header + employee records) into the file
    csv_writer.writerows(data)

print("csv writing completed")  # Confirmation message

# #sample output
# id,name,department,salary
# 101,Vinnu,IT,20000
# 102,hima,IT,300000
# 103,siri,banking,200000
