#employee data using read write
import csv

employees = []
it_department_count = 0

with open('employee_data.csv', mode='r', newline='') as f:
    csv_reader = csv.reader(f)
    header = next(csv_reader)  

    for row in csv_reader:
        emp_id, name, dept, salary = row
        salary = int(salary) 

        # Task 1: Print employees with salary > 60000
        if salary > 60000:
            print(row) 

        # Task 2: Count how many employees belong to the IT department
        if dept == 'IT':
            it_department_count += 1

        # Collect employees with salary > 60000 to write to a new file later
        if salary > 60000:
            employees.append(row)

print(f"\nNumber of employees in the IT department: {it_department_count}")

with open('high_salary.csv', mode='w', newline='') as f:
    csv_writer = csv.writer(f)
    csv_writer.writerow(header)
    csv_writer.writerows(employees)

print("\nFiltered data with salary > 60000 has been written to 'high_salary.csv'.")

# sample output
# ['101', 'Arun', 'IT', '700000']
# ['102', 'Riya', 'HR', '650000']
# ['103', 'John', 'Finance', '600000']

# Number of employees in the IT department: 1

# Filtered data with salary > 60000 has been written to 'high_salary.csv'.