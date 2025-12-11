# Importing necessary functions from the mysql_crud and mongo_crud modules
from mysql_crud import read_data_from_mysql, modify_data_from_mysql, load_json_to_mysql
from mongo_crud import insert_employees_bulk, insert_one_employee, get_all, update_employee_by_city, update_employee_by_dept
from mongo_crud import delete_employee_by_department, delete_employee_by_emp_id
from db_connection import db_mongo_connection

# Establish a MongoDB connection
db = db_mongo_connection()

# Load employee data from a JSON file and insert it into MySQL
load_json_to_mysql()

# Read all employee data from MySQL
read_data_from_mysql() 
    
# Modify the employee data (e.g., adding a category)
modified_data = modify_data_from_mysql()

# Print the modified employee data
for employee in modified_data:
    print(employee)       

# Insert the modified employee data into MongoDB
insert_employees_bulk(db, modified_data)

# Create a new employee record
employee = {
    "emp_id": 206,
    "name": "Arun",
    "department": "Testing",
    "age": 28,
    "city": "Bangalore"
}

# Insert a single employee record into MongoDB
insert_one_employee(db, employee)

# Retrieve all employee records from MongoDB
employees = get_all(db)

# Print all employee records from MongoDB
for emp in employees:
    print(emp)

# Update the city of the employee with emp_id 202 to "Hyderabad"
update_employee_by_city(db, 202, "Hyderabad")

# Update the department of the employee with emp_id 206 to "Trainer"
update_employee_by_dept(db, 206, "Trainer")

# Delete the employee with emp_id 206 from MongoDB
delete_employee_by_emp_id(db, 206)

# Delete all employees in the "Trainer" department from MongoDB
delete_employee_by_department("Trainer")
