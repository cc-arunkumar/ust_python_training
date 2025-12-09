#Task Employee Skills & Project Tracking System (ESPTS)

from pymongo import MongoClient, ReturnDocument

# Connect to MongoDB
client = MongoClient("mongodb+srv://msovan928_db_user:sovan@clusterfastapi.yrq0el1.mongodb.net/")
db = client['employees']

# Auto-increment employee ID
def get_next_emp_id(db):
    counter = db.emp.find_one_and_update(
        {"_id": "emp_id"},
        {"$inc": {"sequence_value": 1}},
        upsert=True,
        return_document=ReturnDocument.AFTER
    )
    return counter["sequence_value"]

# ---------------- CREATE ----------------
def create_record(employee: dict):
    emp_id = get_next_emp_id(db)
    employee["emp_id"] = emp_id
    return db.employees.insert_one(employee)

def create_records(employees: list):
    for emp in employees:
        emp_id = get_next_emp_id(db)
        emp["emp_id"] = emp_id
    return db.employees.insert_many(employees)

# ---------------- READ ----------------
def find_by_dept(dept: str):
    return list(db.employees.find({"department": dept}))

def find_by_skill(skill: str):
    return list(db.employees.find({"skills": skill}))

def find_by_city(city: str):
    return list(db.employees.find({"address.city": city}))

def find_employees_missing_skills():
    return list(db.employees.find({"skills": {"$exists": False}}))

def find_by_experience(min_years=3, max_years=5):
    return list(db.employees.find({"experience_years": {"$gte": min_years, "$lte": max_years}}))

def find_by_project_status(status: str):
    return list(db.employees.find({"projects.status": status}))

def find_by_projection_field():
    return list(db.employees.find({}, {"name": 1, "address.city": 1, "_id": 0}))

def sort_by_age(order=1):
    return list(db.employees.find().sort("age", order))

# ---------------- UPDATE ----------------
def update_department(emp_id, new_dept):
    return db.employees.update_one({"emp_id": emp_id}, {"$set": {"department": new_dept}})

def add_skill(emp_id, skill):
    return db.employees.update_one({"emp_id": emp_id}, {"$addToSet": {"skills": skill}})

def remove_skill(emp_id, skill):
    return db.employees.update_one({"emp_id": emp_id}, {"$pull": {"skills": skill}})

def update_project_status(emp_id, project_name, new_status):
    return db.employees.update_one(
        {"emp_id": emp_id, "projects.name": project_name},
        {"$set": {"projects.$.status": new_status}}
    )

def add_project(emp_id, project_name, status):
    return db.employees.update_one(
        {"emp_id": emp_id},
        {"$push": {"projects": {"name": project_name, "status": status}}}
    )

def increment_experience(years=1):
    return db.employees.update_many({}, {"$inc": {"experience_years": years}})

def rename_field(old_name, new_name):
    return db.employees.update_many({}, {"$rename": {old_name: new_name}})

def delete_field(field_name):
    return db.employees.update_many({}, {"$unset": {field_name: ""}})

def bulk_update_department(dept, new_title):
    return db.employees.update_many({"department": dept}, {"$set": {"title": new_title}})

def upsert_employee(emp_id, data):
    return db.employees.update_one({"emp_id": emp_id}, {"$set": data}, upsert=True)

# ---------------- DELETE ----------------
def delete_employee(emp_id):
    return db.employees.delete_one({"emp_id": emp_id})

def delete_low_experience(threshold=1):
    return db.employees.delete_many({"experience_years": {"$lt": threshold}})

def delete_field_all(field_name):
    return db.employees.update_many({}, {"$unset": {field_name: ""}})

def remove_skill_from_employee(emp_id, skill):
    return db.employees.update_one({"emp_id": emp_id}, {"$pull": {"skills": skill}})

def remove_project_from_employee(emp_id, project_name):
    return db.employees.update_one({"emp_id": emp_id}, {"$pull": {"projects": {"name": project_name}}})

# ---------------- SAMPLE DATA ----------------
employee = {
    "name": "Kiran Patil",
    "age": 27,
    "department": "AI",
    "skills": ["python", "fastapi", "mongodb"],
    "address": {"city": "Pune", "state": "MH"},
    "projects": [
        {"name": "ChatbotX", "status": "in-progress"},
        {"name": "VisionAI", "status": "planned"}
    ],
    "experience_years": 3
}

employees = [
    {
        "name": "Sneha Rao",
        "age": 25,
        "department": "Cloud",
        "skills": ["aws", "docker"],
        "address": {"city": "Bangalore", "state": "KA"},
        "projects": [{"name": "CloudPortal", "status": "completed"}],
        "experience_years": 2
    },
    {
        "name": "Amit Sharma",
        "age": 30,
        "department": "Cybersecurity",
        "skills": ["networking", "linux"],
        "address": {"city": "Delhi", "state": "DL"},
        "projects": [{"name": "SecureBank", "status": "deployed"}],
        "experience_years": 6
    },
    {
        "name": "Priya Nair",
        "age": 23,
        "department": "Testing",
        "skills": [],
        "address": {"city": "Chennai", "state": "TN"},
        "projects": [],
        "experience_years": 1
    }
]

# Example usage
if __name__ == "__main__":
    # Insert one employee
    create_record(employee)

    # Insert multiple employees
    create_records(employees)

    # Query examples
    print(find_by_dept("AI"))
    print(find_by_skill("docker"))
    print(find_by_city("Delhi"))
    print(find_employees_missing_skills())
    print(find_by_experience(2, 5))
    print(find_by_project_status("completed"))
    print(find_by_projection_field())
    print(sort_by_age(-1))
