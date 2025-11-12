import csv

# Read the employee data from the CSV file using DictReader
with open('employee_dict_data.csv', mode='r') as file:
    # Create a DictReader object
    csv_reader = csv.DictReader(file)
    
    # Loop through each row in the CSV and print employee data
    for row in csv_reader:
        print(f"ID: {row['id']}, Name: {row['name']}, Department: {row['department']}, Salary: {row['salary']}")


#o/p:
# ID: 201, Name: suresh, Department: sales, Salary: 58000
# ID: 202, Name: meena, Department: IT, Salary: 72000
# ID: 203, Name: amit, Department: HR, Salary: 64000