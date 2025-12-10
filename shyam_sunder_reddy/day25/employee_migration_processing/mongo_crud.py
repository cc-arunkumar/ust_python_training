from pymongo import MongoClient, errors

# --- Database Setup ---
client = MongoClient("mongodb://localhost:27017/")
db = client["ust_mongo_db"]
conn = db["employees"]

# Ensure emp_id is unique
conn.create_index("emp_id", unique=True)

def insert_many_emp(data):
    try:
        conn.insert_many(data)
        print("data inserted into mongo db successfully")
    except :
        print("Error orrured in insertion")


def insert_one_emp(emp):
    try:
        conn.insert_one(emp)
        print("inserted employee successfully")
    except :
        print("Error orrured in insertion")
        
def read_all():
    try:
        data=conn.find()
        return data
    except:
        print("Error occured")

def update_one_emp(id, key, value):
    try:
        # Correct usage of $set
        res = conn.update_one(
            {"emp_id": id}, 
            {"$set": {key: value}}
        )
        if res.matched_count == 1:
            print("updated successfully")
        else:
            print("no matching employee found")
    except Exception as e:
        print("error while updating the", id, ":", e)


def delete_one_employee(id):
    try:
        conn.delete_one({"emp_id":id})
        print("Deleted one employee ",id)
    except:
        print("error while deleting ",id)

def delete_many_employee(dep):
    try:
        conn.delete_many({"department":dep})
        print("Deleted all the employees ",dep)
    except:
        print("error while deleting by department ",dep)
        