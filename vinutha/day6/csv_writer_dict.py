import csv   # Import the CSV module to handle CSV file operations

# List of employee records, each represented as a dictionary
employees = [
    {"id": 401, "name": "hima", "department": "Development", "salary": 800000},
    {"id": 402, "name": "chakitha", "department": "Development", "salary": 900000},
    {"id": 404, "name": "siri", "department": "Testing", "salary": 1800000},
    {"id": 406, "name": "vinnu", "department": "support", "salary": 100000}   
]

# Open a CSV file in write mode
# 'newline=""' ensures rows are written correctly without extra blank lines
with open('employee_dict_data.csv', mode='w', newline='') as file:
    # Define the header (column names)
    header = ["id", "name", "department", "salary"]

    # Create a DictWriter object which writes dictionaries into CSV format
    writer = csv.DictWriter(file, fieldnames=header)

    # Write the header row (column names)
    writer.writeheader()

    # Write multiple employee records (each dictionary becomes a row)
    writer.writerows(employees)

print("csv writing completed")

#output:
# csv writing completed