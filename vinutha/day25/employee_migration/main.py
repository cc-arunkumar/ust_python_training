import json
from mysql_crud import create_mysql_table, insert_employee_data, fetch_all_employees
from mongo_crud import insert_employees_to_mongo, fetch_all_employees_from_mongo

def load_json_data():
    with open('employees.json', 'r') as file:
        return json.load(file)

def add_category_to_data(employee_data):
    for employee in employee_data:
        if employee['age'] < 25:
            employee['category'] = 'Fresher'
        else:
            employee['category'] = 'Experienced'
    return employee_data

def main():
    print("hello")
    
    # Step 1: Create MySQL table if it doesn't exist
    create_mysql_table()
    print("1")
    
    # Step 2: Load employee data from JSON file
    employee_data = load_json_data()
    print("2")
    
    # Step 3: Add category field to the employee data
    employee_data = add_category_to_data(employee_data)
    print("3")

    # Step 4: Insert employee data into MySQL
    insert_employee_data(employee_data)

    # Step 5: Insert employee data into MongoDB
    insert_employees_to_mongo(employee_data)

    # Step 6: Fetch all employees from MongoDB
    mongo_employees = fetch_all_employees_from_mongo()
    print(f"Employees in MongoDB: {mongo_employees}")

    # Step 7: Fetch all employees from MySQL
    mysql_employees = fetch_all_employees()
    print(f"Employees in MySQL: {mysql_employees}")

if __name__ == "__main__":
    main()



#output
# hello
# Connecting to MySQL...
# MySQL table created successfully.
# 1
# 2
# 3
# Inserting data: [{'emp_id': 201, 'name': 'Anu Joseph', 'department': 'AI', 'age': 23, 'city': 'Trivandrum', 'category': 'Fresher'}, {'emp_id': 202, 'name': 'Rahul Menon', 'department': 'Cloud', 'age': 26, 'city': 'Kochi', 'category': 'Experienced'}, {'emp_id': 203, 'name': 'Sahana R', 'department': 'Testing', 'age': 22, 'city': 'Chennai', 'category': 'Fresher'}, {'emp_id': 204, 'name': 'Vishnu Prakash', 'department': 'Cybersecurity', 'age': 29, 'city': 'Trivandrum', 'category': 'Experienced'}, {'emp_id': 205, 'name': 'Maya Kumar', 'department': 'AI', 'age': 25, 'city': 'Bangalore', 'category': 'Experienced'}]
# Employee data inserted into MySQL.
# MongoDB connection successful
# Employee data inserted into MongoDB.
# MongoDB connection successful
# Employees in MongoDB: [{'_id': ObjectId('69391831ce30bd2d3c37221e'), 'emp_id': 201, 'name': 'Anu Joseph', 'department': 'AI', 'age': 23, 'city': 'Trivandrum', 'category': 'Fresher'}, {'_id': ObjectId('69391831ce30bd2d3c37221f'), 'emp_id': 202, 'name': 'Rahul Menon', 'department': 'Cloud', 'age': 26, 'city': 'Kochi', 'category': 'Experienced'}, {'_id': ObjectId('69391831ce30bd2d3c372220'), 'emp_id': 203, 'name': 'Sahana R', 'department': 'Testing', 'age': 22, 'city': 'Chennai', 'category': 'Fresher'}, {'_id': ObjectId('69391831ce30bd2d3c372221'), 'emp_id': 204, 'name': 'Vishnu Prakash', 'department': 'Cybersecurity', 'age': 29, 'city': 'Trivandrum', 'category': 'Experienced'}, {'_id': ObjectId('69391831ce30bd2d3c372222'), 'emp_id': 205, 'name': 'Maya Kumar', 
# 'department': 'AI', 'age': 25, 'city': 'Bangalore', 'category': 'Experienced'}, {'_id': ObjectId('693918a63f156967f47be861'), 'emp_id': 201, 'name': 'Anu Joseph', 'department': 'AI', 'age': 23, 'city': 'Trivandrum', 'category': 'Fresher'}, {'_id': ObjectId('693918a63f156967f47be862'), 'emp_id': 202, 'name': 'Rahul Menon', 'department': 'Cloud', 'age': 26, 'city': 'Kochi', 'category': 'Experienced'}, {'_id': ObjectId('693918a63f156967f47be863'), 'emp_id': 203, 'name': 'Sahana R', 'department': 'Testing', 'age': 22, 'city': 'Chennai', 'category': 'Fresher'}, {'_id': ObjectId('693918a63f156967f47be864'), 'emp_id': 204, 'name': 'Vishnu 
# Prakash', 'department': 'Cybersecurity', 'age': 29, 'city': 'Trivandrum', 'category': 'Experienced'}, {'_id': ObjectId('693918a63f156967f47be865'), 'emp_id': 205, 'name': 'Maya Kumar', 'department': 'AI', 'age': 25, 'city': 'Bangalore', 'category': 'Experienced'}]
# Employees in MySQL: [{'emp_id': 1, 'name': 'Anu Joseph', 'department': 'AI', 'age': 23, 'city': 'Trivandrum'}, {'emp_id': 2, 'name': 'Rahul Menon', 'department': 'Cloud', 'age': 26, 'city': 'Kochi'}, {'emp_id': 3, 'name': 'Sahana R', 'department': 'Testing', 'age': 22, 'city': 'Chennai'}, {'emp_id': 4, 'name': 'Vishnu Prakash', 'department': 'Cybersecurity', 'age': 29, 'city': 'Trivandrum'}, {'emp_id': 5, 'name': 'Maya Kumar', 'department': 'AI', 'age': 25, 'city': 'Bangalore'}, {'emp_id': 6, 'name': 'Anu Joseph', 'department': 'AI', 'age': 23, 'city': 'Trivandrum'}, {'emp_id': 7, 'name': 'Rahul Menon', 'department': 'Cloud', 'age': 26, 'city': 'Kochi'}, {'emp_id': 8, 'name': 'Sahana R', 'department': 'Testing', 'age': 22, 'city': 'Chennai'}, {'emp_id': 9, 'name': 'Vishnu Prakash', 'department': 'Cybersecurity', 'age': 29, 'city': 'Trivandrum'}, {'emp_id': 10, 'name': 'Maya Kumar', 'department': 'AI', 'age': 25, 'city': 'Bangalore'}, {'emp_id': 11, 'name': 'Anu Joseph', 'department': 'AI', 'age': 23, 'city': 
# 'Trivandrum'}, {'emp_id': 12, 'name': 'Rahul Menon', 'department': 'Cloud', 'age': 26, 'city': 'Kochi'}, {'emp_id': 13, 'name': 
# 'Sahana R', 'department': 'Testing', 'age': 22, 'city': 'Chennai'}, {'emp_id': 14, 'name': 'Vishnu Prakash', 'department': 'Cybersecurity', 'age': 29, 'city': 'Trivandrum'}, {'emp_id': 15, 'name': 'Maya Kumar', 'department': 'AI', 'age': 25, 'city': 'Bangalore'}]