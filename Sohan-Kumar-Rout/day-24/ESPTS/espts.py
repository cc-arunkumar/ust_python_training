from pymongo import MongoClient

client = MongoClient("mongodb+srv://msovan928_db_user:sovan@clusterfastapi.yrq0el1.mongodb.net/")
db = client["employeess"]

employees = [
    {
        "name": "Harsh",
        "age": 23,
        "email": "harsh@gmail.com",
        "skills": ["Java", "React"],
        "department" : "AI",
        "address": {
            "state": "Odisha",
            "city": "Rourkela"
        }
    },
    {
        "name": "Sovan",
        "age": 23,
        "department" : "Cloud",
        "project-details": [
            {
                "name": "Frontend",
                "status": "Ongoing"
            }
        ],
        "skills": ["Java", "React", "Nextjs"],
        "email": "sovan@gmail.com",
        "address": {
            "state": "Maharastra",
            "city": "Mumbai"
        }
    },
    {
        "name": "Aryan",
        "age": 23,
        "email": "aryan@gmail.com",
        "department" : "GenAI",
        "project-details": [
            {
                "name": "Talent-pool",
                "status": "Finished"
            }
        ],
        "address": {
            "state": "Odisha",
            "city": "Devgarh"
        }
    }
]

def get_next_emp_id(db):
    increments = db.counters.find_one_and_update(
        {"_id": "emp_id"},
        {"$inc": {"sequence_value": 1}},
        upsert=True,
        return_document=True
    )
    return increments["sequence_value"]

def create_employee(db, employee):
    emp_id = get_next_emp_id(db)
    employee["emp_id"] = emp_id
    result = db.employees.insert_one(employee)
    print("Created single employee")
    return result

def create_employee_many(db, employee_list):
    for emp in employee_list:
        emp["emp_id"] = get_next_emp_id(db)
    result = db.employees.insert_many(employee_list)
    print("Created bulk employees")
    return result

def read_all(db):
    for emp in db.employees.find():
        print(emp)
        
def read_by_department(db,department):
    for emp in db.employees.find({"department" : department}):
        print(emp)
        

# Example usage
# create_employee(db, {"name": "Itishree", "age": 34, "email": "itu@gmail.com"})
create_employee_many(db, employees)
# read_all(db)
read_by_department(db,"Cloud")

print("\nAll employees:")
for emp in db.employees.find():
    print(emp)
