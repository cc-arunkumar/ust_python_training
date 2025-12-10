from db_connection import get_connection_mongo
from modify_data_python import modify_data
def insert_one(new_employee):
    try:
        collection = get_connection_mongo()
        new_employee = modify_data(new_employee)
        collection.insert_one(new_employee)
        return ("Employee inserted successfully!")
    except Exception as e:
        return f'Error:{e}'
    
def read_all():
    try:
        collection = get_connection_mongo()
        employees =collection.find({})
        return employees 
    except Exception as e:
        return f'Error:{e}'

def update_record(emp_id,city=None,department=None):
    try:
        collection = get_connection_mongo()
        query ={}
        if city:
            query['city'] = city 
        if department:
            query['department'] = department
            
        res = collection.update_one({"emp_id":emp_id},{'$set':query})
        
        if res.matched_count == 0:
            return 'ID not Found to Update'
        
        return 'Updated Succesfully!'
        
    except Exception as e:
        return f'Error: {e}'
    
def delete_employee(emp_id):
    try:
        collection = get_connection_mongo()
        
        res = collection.delete_one({'emp_id':emp_id})
        
        return 'Deleted Successfully!'

    except Exception as e:
        return f'Error: {e}'
    
def delete_employees(dept):
    try:
        collection = get_connection_mongo()
        
        res = collection.delete_many({"department":dept})
        
        return 'Deleted Employees Successfully!'
    
    except Exception as e:
        return f"Error:{e}"
    

        