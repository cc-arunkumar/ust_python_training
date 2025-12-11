from db_connection import get_mongo_connection
 
class MongoService:
 
    def __init__(self):
        self.collection = get_mongo_connection()
 
    def clear_collection(self):
        self.collection.delete_many({})
        print("MongoDB Collection Cleared.")
 
    def insert_many(self, docs):
        self.collection.insert_many(docs)
        print("Inserted Modified Employees Into MongoDB.")
 
    # CRUD Operations ------------------------
 
    def insert_one(self, doc):
        self.collection.insert_one(doc)
        print("One Employee Inserted.")
 
    def read_all(self):
        employees = list(self.collection.find())
        print("All Employees From MongoDB:")
        for e in employees:
            print(e)
        return employees
 
    def update_one(self, emp_id, updates):
        self.collection.update_one({"emp_id": emp_id}, {"$set": updates})
        print("Employee Updated.")
 
    def delete_one(self, emp_id):
        self.collection.delete_one({"emp_id": emp_id})
        print("One Employee Deleted.")
 
    def delete_many(self, department):
        self.collection.delete_many({"department": department})
        print("Employees From Department Deleted:", department)
 
 