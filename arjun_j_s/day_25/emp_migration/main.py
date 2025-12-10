from mysql_service import MySQLService
from mongo_service import MongoService


mysql = MySQLService()
mysql.create_table()
mysql.load_json_to_mysql("employees.json")
employees = mysql.read_employees()

# Transform Data -----------------
modified = []
for emp in employees:
    emp['category'] = "Fresher" if emp['age'] < 25 else "Experienced"
    modified.append(emp)

print("\nModified Employees:", modified)

mongo = MongoService()
mongo.clear_collection()
mongo.insert_many(modified)

mongo.insert_one({
    "emp_id": 999,
    "name": "New Employee",
    "department": "AI",
    "age": 24,
    "city": "Kochi",
    "category": "Fresher"
})

mongo.read_all()

mongo.update_one(201, {"city": "UpdatedCity", "department": "UpdatedDept"})
mongo.delete_one(203)
mongo.delete_many("Testing")

mongo.read_all()

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
# {'_id': ObjectId('6938f476969cd5370cca5db9'), 'emp_id': 999, 'name': 'New Employee', 'department': 'AI', 'age': 24, 'city': 'Kochi', 'category': 'Fresher'}