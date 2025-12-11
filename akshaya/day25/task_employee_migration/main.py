import json
from mysql_operation import load_data_to_mysql, read_from_mysql
from mongo_operations import insert_into_mongo, perform_crud_operations
from transform_data import transform_data
# from config import create_database_if_not_exists

def load_json_to_mysql():
    with open("employees.json", "r") as file:
        data = json.load(file)
    load_data_to_mysql([(emp["emp_id"], emp["name"], emp["department"], emp["age"], emp["city"]) for emp in data])

def read_mysql_data():
    data = read_from_mysql()
    print("Data from MySQL:", data)

def transform_employee_data():
    with open("employees.json", "r") as file:
        data = json.load(file)
    transformed_data = transform_data(data)
    return transformed_data

def store_data_to_mongo():
    transformed_data = transform_employee_data()
    insert_into_mongo(transformed_data)

def perform_mongo_crud():
    employees = perform_crud_operations()
    print("Employees after CRUD operations:", employees)

if __name__ == "__main__":
    # create_database_if_not_exists()  # Ensure MySQL database exists
    # load_json_to_mysql()       # Task 1
    read_mysql_data()          # Task 2
    store_data_to_mongo()      # Task 4
    perform_mongo_crud()      # Task 5
    
#Output
# Connection Established with Mysql
# MySQL Table Created (if not exists).
# JSON Data Inserted Into MySQL Successfully.
# Data Read From MySQL: [{'emp_id': 201, 'name': 'Anu Joseph', 'department': 'AI', 'age': 23, 'city': 'Trivandrum'}, {'emp_id': 202, 'name': 'Rahul Menon', 'department': 'Cloud', 'age': 26, 'city': 'Kochi'}, {'emp_id': 203, 'name': 'Sahana R', 'department': 'Testing', 'age': 22, 'city': 'Chennai'}, {'emp_id': 204, 'name': 'Vishnu Prakash', 'department': 'Cybersecurity', 'age': 29, 'city': 'Trivandrum'}, {'emp_id': 205, 'name': 'Maya Kumar', 'department': 'AI', 'age': 25, 'city': 'Bangalore'}]
 
# Modified Employees: [{'emp_id': 201, 'name': 'Anu Joseph', 'department': 'AI', 'age': 23, 'city': 'Trivandrum', 'category': 'Fresher'}, {'emp_id': 202, 'name': 'Rahul Menon', 'department': 'Cloud', 'age': 26, 'city': 'Kochi',
# 'category': 'Experienced'}, {'emp_id': 203, 'name': 'Sahana R', 'department': 'Testing', 'age': 22, 'city': 'Chennai', 'category': 'Fresher'}, {'emp_id': 204, 'name': 'Vishnu Prakash', 'department': 'Cybersecurity', 'age': 29, 'city': 'Trivandrum', 'category': 'Experienced'}, {'emp_id': 205, 'name': 'Maya Kumar', 'department': 'AI', 'age': 25, 'city': 'Bangalore', 'category': 'Experienced'}]
# Connection Established with Mongo
# MongoDB Collection Cleared.
# Inserted Modified Employees Into MongoDB.
# One Employee Inserted.
# All Employees From MongoDB:
# {'_id': ObjectId('6938f476969cd5370cca5db4'), 'emp_id': 201, 'name': 'Anu Joseph', 'department': 'AI', 'age': 23, 'city': 'Trivandrum', 'category': 'Fresher'}
# {'_id': ObjectId('6938f476969cd5370cca5db5'), 'emp_id': 202, 'name': 'Rahul Menon', 'department': 'Cloud', 'age': 26, 'city': 'Kochi', 'category': 'Experienced'}
# {'_id': ObjectId('6938f476969cd5370cca5db6'), 'emp_id': 203, 'name': 'Sahana R', 'department': 'Testing', 'age':
# 22, 'city': 'Chennai', 'category': 'Fresher'}
# {'_id': ObjectId('6938f476969cd5370cca5db7'), 'emp_id': 204, 'name': 'Vishnu Prakash', 'department': 'Cybersecurity', 'age': 29, 'city': 'Trivandrum', 'category': 'Experienced'}
# {'_id': ObjectId('6938f476969cd5370cca5db8'), 'emp_id': 205, 'name': 'Maya Kumar', 'department': 'AI', 'age': 25, 'city': 'Bangalore', 'category': 'Experienced'}
# {'_id': ObjectId('6938f476969cd5370cca5db9'), 'emp_id': 999, 'name': 'New Employee', 'department': 'AI', 'age': 24, 'city': 'Kochi', 'category': 'Fresher'}
# Employee Updated.
# One Employee Deleted.
# Employees From Department Deleted: Testing
# All Employees From MongoDB:
# {'_id': ObjectId('6938f476969cd5370cca5db4'), 'emp_id': 201, 'name': 'Anu Joseph', 'department': 'UpdatedDept', 'age': 23, 'city': 'UpdatedCity', 'category': 'Fresher'}
# {'_id': ObjectId('6938f476969cd5370cca5db5'), 'emp_id': 202, 'name': 'Rahul Menon', 'department': 'Cloud', 'age': 26, 'city': 'Kochi', 'category': 'Experienced'}
# {'_id': ObjectId('6938f476969cd5370cca5db7'), 'emp_id': 204, 'name': 'Vishnu Prakash', 'department': 'Cybersecurity', 'age': 29, 'city': 'Trivandrum', 'category': 'Experienced'}
# {'_id': ObjectId('6938f476969cd5370cca5db8'), 'emp_id': 205, 'name': 'Maya Kumar', 'department': 'AI', 'age': 25, 'city': 'Bangalore', 'category': 'Experienced'}
