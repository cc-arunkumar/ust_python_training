from pymongo import MongoClient,ReturnDocument

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["ust"]
counters = db["counters"]
counters.delete_one({"_id": "emp_id"})
counters.insert_one({"_id": "emp_id", "sequence_value": 106})


def get_next_emp_id():
    counter = counters.find_one_and_update(
        {"_id": "emp_id"},
        {"$inc": {"sequence_value": 1}},
        return_document=ReturnDocument.AFTER
    )
    return counter["sequence_value"]

#function for single insert with auto id increament
def insert_employee(emp_doc):
    emp_doc["emp_id"] = get_next_emp_id()
    result = db.employees.insert_one(emp_doc)
    return result.inserted_id

# function for Bulk insert
def insert_multiple_employees(employee_list):
    docs_with_ids = []
    for emp in employee_list:
        emp["emp_id"] = get_next_emp_id()
        docs_with_ids.append(emp)
    
    result = db.employees.insert_many(docs_with_ids)
    return result.inserted_ids


#----------------------- READ ---------------------------
# Find employees by department
def find_emp_by_dept(dept):
    for emp in db.employees.find({"department":dept}):
        print(emp)

# Find employees by skills
def find_emp_by_skill(skill):
    for emp in db.employees.find({"skills":skill}):
        print(emp)

# Find employees by city
def find_emp_by_city(city):
    for emp in db.employees.find({"address.city":city}):
        print(emp)

# Find employees missing particular fields (e.g., skills missing)
def find_employees_missing_skills():
    for emp in db.employees.find({"skills": {"$exists": False}}):
        print(emp)

# Filter by experience range
def find_employees_by_experience(min_years, max_years):
    for emp in db.employees.find({"experience_years": {"$gte": min_years, "$lte": max_years}}):
        print(emp)

# Query nested fields (e.g., project-status)
def find_employees_by_project_status(status):
    for emp in db.employees.find({"projects.status": status}):
        print(emp)

# Sorting by age, experience, name
def find_employees_sorted(sort_field="age", ascending=True):
    order = 1 if ascending else -1
    return list(db.employees.find().sort(sort_field, order))


# ----------------------- UPDATE -------------------------
# Modify employee department ($set)
def update_department(emp_id, new_department):
    db.employees.update_one({"emp_id": emp_id}, {"$set": {"department": new_department}})

# Add new skill ($push or $addToSet)
def add_skill(emp_id, skill, unique=False):
    if unique:
        db.employees.update_one({"emp_id": emp_id}, {"$addToSet": {"skills": skill}})
    else:
        db.employees.update_one({"emp_id": emp_id}, {"$push": {"skills": skill}})

# Remove skill ($pull)
def remove_skill(emp_id, skill):
    db.employees.update_one({"emp_id": emp_id}, {"$pull": {"skills": skill}})

# Update nested project status ($set with positional operator)
def update_project_status(emp_id, project_name, new_status):
    db.employees.update_one(
        {"emp_id": emp_id, "projects.name": project_name},
        {"$set": {"projects.$.status": new_status}}
    )

# Add new project entry ($push)
def add_project(emp_id, project):
    db.employees.update_one({"emp_id": emp_id}, {"$push": {"projects": project}})

# Increment experience counter ($inc)
def increment_experience(emp_id, years=1):
    db.employees.update_one({"emp_id": emp_id}, {"$inc": {"experience_years": years}})

# Rename a field ($rename)
def rename_field(old_field, new_field):
    db.employees.update_many({}, {"$rename": {old_field: new_field}})

# Delete a field ($unset)
def delete_field(field_name):
    db.employees.update_many({}, {"$unset": {field_name: ""}})

# Bulk update based on conditions (update_many)
def bulk_update_department(old_dept, new_dept):
    db.employees.update_many({"department": old_dept}, {"$set": {"department": new_dept}})

# ---------------- DELETE ----------------
# Delete individual employee profile
def delete_employee(emp_id):
    db.employees.delete_one({"emp_id": emp_id})

# Delete employees matching conditions (e.g., low experience)
def delete_low_experience(threshold=1):
    db.employees.delete_many({"experience_years": {"$lt": threshold}})

# Delete specific fields
def delete_field(field_name):
    db.employees.update_many({}, {"$unset": {field_name: ""}})

# Remove array elements (projects)
def remove_project(emp_id, project_name):
    db.employees.update_one({"emp_id": emp_id}, {"$pull": {"projects": {"name": project_name}}})



#single insert
new_id = insert_employee({
    "name": "Amit",
    "age": 23,
    "department": "AI",
    "skills": ["python", "mongodb", "java"],
    "address": {"city": "Trivandrum", "state": "Kerala"},
    "projects": [
        {"name": "VisionAI", "status": "completed"},
        {"name": "DocScan", "status": "in-progress"}
    ],
    "experience_years": 1
})
print("Inserted employee with _id:", new_id)


#Bulk insert
new_ids = insert_multiple_employees([
    {
        "name": "Rahul Menon",
        "age": 26,
        "department": "Cloud",
        "skills": ["aws", "docker"],
        "address": {"city": "Kochi", "state": "Kerala"},
        "projects": [{"name": "USTCloudPortal", "status": "planned"}],
        "experience_years": 3
    },
    {
        "name": "Sahana R",
        "age": 22,
        "department": "Testing",
        "skills": ["selenium"],
        "address": {"city": "Chennai", "state": "TN"},
        "projects": [],
        "experience_years": 1
    }
])
print("Inserted employee IDs:", new_ids)

find_emp_by_dept("AI")

find_emp_by_skill("python")

find_employees_by_experience(2,5)

find_employees_by_project_status("in-progress")

update_department(101, "Data Science")

add_skill(102, "machine-learning", unique=True)

remove_skill(107, "mongodb")

delete_employee(103)
