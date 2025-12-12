from pymongo import MongoClient

# Connect to MongoDB Atlas cluster
client = MongoClient("mongodb+srv://msovan928_db_user:sovan@clusterfastapi.yrq0el1.mongodb.net/")
db = client["employeess"]

# ---- Auto increment logic ----
def get_next_emp_id(db):
    increments = db.counters.find_one_and_update(
        {"_id": "emp_id"},
        {"$inc": {"sequence_value": 1}},
        upsert=True,
        return_document=True
    )
    return increments["sequence_value"]

# ---- CREATE ----
def create_employee(db, employee):
    emp_id = get_next_emp_id(db)
    employee["emp_id"] = emp_id
    result = db.employees.insert_one(employee)
    print(f" Created single employee")
    return result

def create_employee_many(db, employee_list):
    for emp in employee_list:
        emp["emp_id"] = get_next_emp_id(db)
    result = db.employees.insert_many(employee_list)
    print(f" Created employees in bulk")
    return result

# ---- READ ----
def read_all(db):
    print("\n All employees:")
    for emp in db.employees.find():
        print(emp)

def read_by_department(db, department):
    print(f"\n Employees in department: {department}")
    for emp in db.employees.find({"department": department}):
        print(emp)

def read_by_skill(db, skill):
    print(f"\n Employees with skill: {skill}")
    for emp in db.employees.find({"skills": skill}):
        print(emp)

def read_by_city(db, city):
    print(f"\n Employees in city: {city}")
    for emp in db.employees.find({"address.city": city}):
        print(emp)

def read_missing_skills(db):
    print("\n Employees missing 'skills' field:")
    for emp in db.employees.find({"skills": {"$exists": False}}):
        print(emp)

def read_by_experience_range(db, min_age, max_age):
    print(f"\n Employees with age between {min_age} and {max_age}:")
    for emp in db.employees.find({"age": {"$gte": min_age, "$lte": max_age}}):
        print(emp)

def query_project_status(db, status):
    print(f"\n Employees with project status: {status}")
    for emp in db.employees.find({"project_details.status": status}):
        print(emp)

def projection_limited_fields(db):
    print("\n Projection (only name & department):")
    for emp in db.employees.find({}, {"name": 1, "department": 1, "_id": 0}):
        print(emp)

def sort_employees(db, field, order=1):
    print(f"\n Employees sorted by {field} ({'ASC' if order==1 else 'DESC'}):")
    for emp in db.employees.find().sort(field, order):
        print(emp)

# ---- UPDATE ----
def update_department(db, name, new_dept):
    db.employees.update_one({"name": name}, {"$set": {"department": new_dept}})
    print(f" Updated department to {new_dept}")

def add_skill(db, name, skill):
    db.employees.update_one({"name": name}, {"$addToSet": {"skills": skill}})
    print(f" Added skill {skill} to {name}")

def remove_skill(db, name, skill):
    db.employees.update_one({"name": name}, {"$pull": {"skills": skill}})
    print(f" Removed skill {skill} from {name}")

def update_project_status(db, name, project_name, new_status):
    db.employees.update_one(
        {"name": name, "project_details.name": project_name},
        {"$set": {"project_details.$.status": new_status}}
    )
    print(f" Updated {name}'s project {project_name} status to {new_status}")

def add_project(db, name, project):
    db.employees.update_one({"name": name}, {"$push": {"project_details": project}})
    print(f" Added new project to {name}")

def increment_experience(db, name, years=1):
    db.employees.update_one({"name": name}, {"$inc": {"experience": years}})
    print(f" Incremented {name}'s experience by {years} years")

def rename_field(db, old_field, new_field):
    db.employees.update_many({}, {"$rename": {old_field: new_field}})
    print(f" Renamed field {old_field} to {new_field}")

def delete_field(db, name, field):
    db.employees.update_one({"name": name}, {"$unset": {field: ""}})
    print(f" Deleted field {field} from {name}")

def bulk_update_juniors(db):
    db.employees.update_many({"age": {"$lt": 25}}, {"$set": {"junior": True}})
    print(" Marked all employees under 25 as junior")

def upsert_employee(db, name, profile):
    db.employees.update_one({"name": name}, {"$set": profile}, upsert=True)
    print(f" Upserted employee profile for {name}")

# ---- DELETE ----
def delete_employee(db, name):
    db.employees.delete_one({"name": name})
    print(f" Deleted employee {name}")

def delete_low_experience(db, max_age):
    db.employees.delete_many({"age": {"$lt": max_age}})
    print(f" Deleted employees younger than {max_age}")

def remove_array_element(db, name, field, value):
    db.employees.update_one({"name": name}, {"$pull": {field: value}})
    print(f" Removed array element")


    # Queries
    read_by_experience_range(db, 20, 25)
    query_project_status(db, "Ongoing")
    projection_limited_fields(db)
    sort_employees(db, "age", 1)

    # Updates
    update_department(db, "Harsh", "Data Science")
    add_skill(db, "Sovan", "AWS")
    remove_skill(db, "Sovan", "React")
    
    update_project_status(db, "Sovan", "Frontend", "Finished")
    add_project(db, "Aryan", {"name": "New Project", "status": "Ongoing"})
    increment_experience(db, "Harsh", 2)
    
    rename_field(db, "department", "dept")
    delete_field(db, "Aryan", "email")
    bulk_update_juniors(db)
    upsert_employee(db, "NewGuy", {"age": 30, "department": "AI"})

    # Deletes
    delete_employee(db, "Harsh")
    delete_low_experience(db, 22)
    remove_array_element(db, "Aryan", "skills", "Java")
    remove_array_element(db, "Aryan", "project_details", {"name": "Talent-pool", "status": "Finished"})
    read_all(db)
