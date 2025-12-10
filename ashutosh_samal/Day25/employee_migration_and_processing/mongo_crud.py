from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/") 
db = client['ust_db']
collection = db['employees']

# Create a new employee document
new_employee = {
    "emp_id": 206,
    "name": "Amit",
    "department": "HR",
    "age": 28,
    "city": "Mumbai"
}

# Insert the new employee document into the collection
insert_result = collection.insert_one(new_employee)
print(f"Inserted Employee with emp_id: {new_employee['emp_id']}")

# Retrieve all employee documents from the collection
all_employees = collection.find()
print("\nAll Employees:")
for emp in all_employees:
    print(emp)

# Update employee document 
emp_id_to_update = 206
updated_employee = collection.update_one(
    {"emp_id": emp_id_to_update},       # Filter condition
    {"$set": {"city": "Pune", "department": "Finance"}}  # Fields to update
)
print(f"\nUpdated Employee with emp_id {emp_id_to_update}:")
print(updated_employee.modified_count, "document updated.")

# Delete employee document with emp_id = 206
emp_id_to_delete = 206
delete_result = collection.delete_one({"emp_id": emp_id_to_delete})
print(f"\nDeleted Employee with emp_id {emp_id_to_delete}:")
print(delete_result.deleted_count, "document deleted.")

# Delete all employees belonging to department 'AI'
department_to_delete = "AI"
delete_many_result = collection.delete_many({"department": department_to_delete})
print(f"\nDeleted Employees in {department_to_delete} department:")
print(delete_many_result.deleted_count, "document(s) deleted.")
