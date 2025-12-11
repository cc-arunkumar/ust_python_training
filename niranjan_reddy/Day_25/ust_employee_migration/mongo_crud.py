# Function to insert multiple employee records into the MongoDB collection, after clearing the existing ones
def insert_employees_bulk(db, employee):
    
    # Access the 'employees' collection in the database
    collection = db.employees
    
    # Delete all existing records in the collection before inserting new ones
    collection.delete_many({})
    
    # Insert multiple employee records into the collection
    collection.insert_many(employee)
    
    # Return the inserted ID of the collection (though 'inserted_id' will only exist for one document, insert_many returns a list of inserted_ids)
    return collection.inserted_id


# Function to insert a single employee record into the MongoDB collection
def insert_one_employee(db, employee):
    
    # Access the 'employees' collection in the database
    collection = db.employees
    
    # Insert a single employee record into the collection
    collection.insert_one(employee)
    
    # Return the inserted ID of the employee
    return collection.inserted_id

# Function to retrieve all employee records from the MongoDB collection
def get_all(db):
    
    # Access the 'employees' collection in the database
    collection = db.employees
    
    # Find all employee documents in the collection
    emp = collection.find()
    
    # Return the employee records
    return emp
    

# Function to update an employee's city based on their emp_id
def update_employee_by_city(db, emp_id, city):
    
    # Access the 'employees' collection in the database
    collection = db.employees
    
    # Update the city field of the employee with the given emp_id
    collection.update_one(
        {"emp_id": emp_id},  # Search by emp_id
        {"$set": {"city": city}}  # Set the new city
    )
    
    # Return the number of modified documents (should be 1 if the employee exists)
    return collection.modified_count
   

# Function to update an employee's department based on their emp_id
def update_employee_by_dept(db, emp_id, department):
    
    # Access the 'employees' collection in the database
    collection = db.employees
    
    # Update the department field of the employee with the given emp_id
    collection.update_one(
        {"emp_id": emp_id},  # Search by emp_id
        {"$set": {"department": department}}  # Set the new department
    )
    
    # Return the number of modified documents (should be 1 if the employee exists)
    return collection.modified_count
    
    
# Function to delete an employee based on their emp_id
def delete_employee_by_emp_id(db, emp_id):
    
    # Delete a single employee document with the given emp_id
    result = db.employees.delete_one({"emp_id": emp_id}) 



# Function to delete multiple employees based on their department
def delete_employee_by_department(db, department):
    
    # Delete all employee documents with the given department
    result = db.employees.delete_many({"department": department})  
    
    # Return the number of deleted documents
    return result.deleted_count
