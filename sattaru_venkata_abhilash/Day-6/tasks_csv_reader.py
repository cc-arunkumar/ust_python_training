import csv

# Task 1: Print only those employees whose salary is greater than 60000
print("**** Task 1: Employees with Salary > 60000 ****")
with open("employee_data01.csv", mode='r') as file:
    csv_reader = csv.reader(file)
    # Skip the header row
    next(csv_reader) 
    for row in csv_reader:
        salary = float(row[3]) 
         # Convert the salary from string to float
        if salary > 60000:
            print(f"Salary greater than 60000: {row[1]} (Department: {row[2]}, Salary: {salary})")
            

# Task 2: Count how many employees belong to the IT department
print("\n**** Task 2: Employee Count in IT Department ****")
count = 0
with open("employee_data01.csv", mode='r') as file:
    csv_reader = csv.reader(file)
    next(csv_reader)  
    for row in csv_reader:
        if row[2] == "IT": 
            count += 1

print(f"Employee count in IT department: {count}")


# Task 3: Write the filtered data (salary > 60000) into a new file high_salary.csv
print("\n**** Task 3: Write Employees with Salary > 60000 to a New File ****")
with open("employee_data01.csv", mode='r') as file:
    csv_reader = csv.reader(file)
    header = next(csv_reader) 

    # Filtered data will be stored here
    filtered_data = [header]  

    for row in csv_reader:
        salary = float(row[3]) 
        if salary > 60000:
            filtered_data.append(row)  

# Write the filtered data into a new CSV file
with open("high_salary.csv", mode='w', newline='') as file:
    csv_writer = csv.writer(file)
    # Write all rows to the new file
    csv_writer.writerows(filtered_data)  

print("******* CSV Writing Completed for high_salary.csv ******")




# Sample output:
#     **** Task 1: Employees with Salary > 60000 ****
# Salary greater than 60000: Arun (Department: IT, Salary: 70000.0)
# Salary greater than 60000: Riya (Department: HR, Salary: 65000.0)

# **** Task 2: Employee Count in IT Department ****
# Employee count in IT department: 1

# **** Task 3: Write Employees with Salary > 60000 to a New File ****
# ******* CSV Writing Completed for high_salary.csv ******