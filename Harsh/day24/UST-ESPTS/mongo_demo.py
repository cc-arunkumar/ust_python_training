from pymongo import MongoClient, ASCENDING,ReturnDocument,DESCENDING
from datetime import datetime

client = MongoClient('mongodb://localhost:27017')
db = client['ust_db']
print("Database created successfully")

employees = db['employees']

# Ensure emp_id is unique
employees.create_index([("emp_id", ASCENDING)], unique=True)

counters = db["counters"]
counters.update_one(
    {"_id": "employees_emp_id"},
    {"$setOnInsert": {"seq": 110}},  # start after your seed dataset
    upsert=True
)

def get_next_emp_id():
    doc = counters.find_one_and_update(
        {"_id": "employees_emp_id"},
        {"$inc": {"seq": 1}},
        return_document=ReturnDocument.AFTER
    )
    return doc["seq"]

employees_data = [
    {
        "emp_id": 101,
        "name": "Anu Joseph",
        "age": 23,
        "department": "AI",
        "skills": ["python", "mongodb"],
        "address": {"city": "Trivandrum", "state": "Kerala"},
        "projects": [
            {"name": "VisionAI", "status": "completed"},
            {"name": "DocScan", "status": "in-progress"},
        ],
        "experience_years": 1,
    },
    {
        "emp_id": 102,
        "name": "Rahul Menon",
        "age": 26,
        "department": "Cloud",
        "skills": ["aws", "docker"],
        "address": {"city": "Kochi", "state": "Kerala"},
        "projects": [{"name": "USTCloudPortal", "status": "planned"}],
        "experience_years": 3,
    },
    {
        "emp_id": 103,
        "name": "Sahana R",
        "age": 22,
        "department": "Testing",
        "skills": ["selenium"],
        "address": {"city": "Chennai", "state": "TN"},
        "projects": [],
        "experience_years": 1,
    },
    {
        "emp_id": 104,
        "name": "Vishnu Prakash",
        "age": 29,
        "department": "Cybersecurity",
        "skills": ["networking", "siem"],
        "address": {"city": "Trivandrum", "state": "Kerala"},
        "projects": [{"name": "SecureBank", "status": "in-progress"}],
        "experience_years": 5,
    },
    {
        "emp_id": 105,
        "name": "Maya Kumar",
        "age": 25,
        "department": "AI",
        "skills": ["python", "deep-learning"],
        "address": {"city": "Bangalore", "state": "KA"},
        "projects": [{"name": "VisionAI", "status": "completed"}],
        "experience_years": 2,
    },
    {
        "emp_id": 106,
        "name": "Arjun S",
        "age": 28,
        "department": "Cloud",
        "skills": ["azure"],
        "address": {"city": "Kochi", "state": "Kerala"},
        "projects": [{"name": "DevOpsBoost", "status": "in-progress"}],
        "experience_years": 4,
    },
    {
        "emp_id": 107,
        "name": "Neha Mohan",
        "age": 24,
        "department": "Data",
        "skills": ["sql", "tableau"],
        "address": {"city": "Chennai", "state": "TN"},
        "projects": [{"name": "USTAnalyticsHub", "status": "planned"}],
        "experience_years": 2,
    },
    {
        "emp_id": 108,
        "name": "Suresh B",
        "age": 27,
        "department": "Data",
        "address": {"city": "Kochi", "state": "Kerala"},
        "projects": [],
        "experience_years": 3,
    },
    {
        "emp_id": 109,
        "name": "Lavanya N",
        "age": 21,
        "department": "Testing",
        "skills": [],
        "address": {"city": "Trivandrum", "state": "Kerala"},
        "projects": [{"name": "QualityX", "status": "in-progress"}],
        "experience_years": 0,
    },
    {
        "emp_id": 110,
        "name": "Rakesh Pillai",
        "age": 30,
        "department": "Cybersecurity",
        "skills": ["networking", "firewall", "linux"],
        "projects": [{"name": "SecuritySuite", "status": "deployed"}],
        "experience_years": 7,
    },
]

# Insert all 10 employees
# employees.insert_many(employees_data)
print("Inserted 10 employees successfully.")


# Insert one employee
emp = {
    "name": "Priya Das",
    "age": 26,
    "department": "AI",
    "skills": ["pytorch", "nlp"],
    "address": {"city": "Bangalore", "state": "KA"},
    "projects": [{"name": "ChatAssist", "status": "in-progress"}],
    "experience_years": 3,
}
# employees.insert_one(emp)
records = [
    {
        "name": "Meera K",
        "age": 24,
        "department": "AI",
        "skills": ["python", "tensorflow"],
        "address": {"city": "Bangalore", "state": "KA"},
        "projects": [{"name": "VisionBot", "status": "planned"}],
        "experience_years": 1,
    },
    {
        "name": "Sanjay P",
        "age": 29,
        "department": "Cloud",
        "skills": ["aws", "docker", "kubernetes"],
        "address": {"city": "Hyderabad", "state": "TS"},
        "projects": [{"name": "CloudOpsX", "status": "in-progress"}],
        "experience_years": 4,
    },
    {
        "name": "Aditi R",
        "age": 27,
        "department": "Testing",
        "skills": ["selenium", "jmeter"],
        "address": {"city": "Pune", "state": "MH"},
        "projects": [{"name": "TestSuite", "status": "completed"}],
        "experience_years": 3,
    },
    {
        "name": "Rohan S",
        "age": 31,
        "department": "Cybersecurity",
        "skills": ["firewall", "linux", "siem"],
        "address": {"city": "Delhi", "state": "DL"},
        "projects": [{"name": "SecurePay", "status": "deployed"}],
        "experience_years": 6,
    },
    {
        "name": "Sneha M",
        "age": 22,
        "department": "Data",
        "skills": ["sql", "tableau"],
        "address": {"city": "Chennai", "state": "TN"},
        "projects": [{"name": "AnalyticsHub", "status": "planned"}],
        "experience_years": 1,
    },
    {
        "name": "Vikram N",
        "age": 28,
        "department": "AI",
        "skills": ["pytorch", "nlp"],
        "address": {"city": "Trivandrum", "state": "Kerala"},
        "projects": [{"name": "ChatAssist", "status": "in-progress"}],
        "experience_years": 4,
    },
    {
        "name": "Divya G",
        "age": 25,
        "department": "Cloud",
        "skills": ["azure", "terraform"],
        "address": {"city": "Kochi", "state": "Kerala"},
        "projects": [{"name": "InfraScale", "status": "planned"}],
        "experience_years": 2,
    },
    {
        "name": "Arvind T",
        "age": 30,
        "department": "Data",
        "skills": ["spark", "airflow"],
        "address": {"city": "Bangalore", "state": "KA"},
        "projects": [{"name": "ETLPro", "status": "in-progress"}],
        "experience_years": 5,
    },
    {
        "name": "Nisha L",
        "age": 23,
        "department": "Testing",
        "skills": ["postman"],
        "address": {"city": "Pune", "state": "MH"},
        "projects": [{"name": "APIValidator", "status": "completed"}],
        "experience_years": 1,
    },
    {
        "name": "Karthik J",
        "age": 29,
        "department": "Cybersecurity",
        "skills": ["threat-hunting", "networking"],
        "address": {"city": "Hyderabad", "state": "TS"},
        "projects": [{"name": "ZeroTrust", "status": "planned"}],
        "experience_years": 6,
    },
    {
        "name": "Pooja D",
        "age": 26,
        "department": "AI",
        "skills": ["deep-learning", "computer-vision"],
        "address": {"city": "Delhi", "state": "DL"},
        "projects": [{"name": "VisionAI", "status": "in-progress"}],
        "experience_years": 3,
    },
    {
        "name": "Rahul K",
        "age": 24,
        "department": "Cloud",
        "skills": ["ansible", "docker"],
        "address": {"city": "Chennai", "state": "TN"},
        "projects": [{"name": "AutoOps", "status": "completed"}],
        "experience_years": 2,
    },
    {
        "name": "Geetha P",
        "age": 30,
        "department": "Data",
        "skills": ["tableau", "sql"],
        "address": {"city": "Kochi", "state": "Kerala"},
        "projects": [{"name": "BI360", "status": "deployed"}],
        "experience_years": 6,
    },
    {
        "name": "Thomas V",
        "age": 27,
        "department": "Testing",
        "skills": ["selenium", "jmeter"],
        "address": {"city": "Chennai", "state": "TN"},
        "projects": [{"name": "LoadTestX", "status": "in-progress"}],
        "experience_years": 3,
    },
    {
        "name": "Nisha R",
        "age": 28,
        "department": "AI",
        "skills": ["nlp"],
        "address": {"city": "Trivandrum", "state": "Kerala"},
        "projects": [{"name": "DocAI", "status": "planned"}],
        "experience_years": 4,
    },
]

# Assign emp_id automatically

for rec in records:
    rec["emp_id"] = get_next_emp_id()
    
# employees.insert_many(records)
print("Inserted", len(records), "employees successfully.")

print("\n--- Find by Department ---")
for emp in employees.find({"department": "Cloud"}):
    print(emp)

print("\n--- Find by Skillset ---")
for emp in employees.find({"skills": "python"}):
    print(emp)

print("\n--- Find by City ---")
for emp in employees.find({"address.city": "Chennai"}):
    print(emp)

print("\n--- Missing Skills Field ---")
for emp in employees.find({"skills": {"$exists": False}}):
    print(emp)

print("\n--- Empty Skills Array ---")
for emp in employees.find({"skills": {"$size": 0}}):
    print(emp)

print("\n--- Experience Range (2-5 years) ---")
for emp in employees.find({"experience_years": {"$gte": 2, "$lte": 5}}):
    print(emp)

print("\n--- Query Nested Field (project status) ---")
for emp in employees.find({"projects.status": "in-progress"}):
    print(emp)

print("\n--- Projection (name & department only) ---")
for emp in employees.find({}, { "name": 1, "department": 1}):
    print(emp)

print("\n--- Sort by Age Ascending ---")
for emp in employees.find().sort("age", ASCENDING):
    print(emp)

print("\n--- Sort by Experience Descending ---")
for emp in employees.find().sort("experience_years", DESCENDING):
    print(emp)

print("\n--- Sort by Name Ascending ---")
for emp in employees.find().sort("name", ASCENDING):
    print(emp)
    
# 1. Modify employee department
employees.update_one(
    {"name": "Rahul Menon"},
    {"$set": {"department": "Cloud-Engineer"}}
)

# 2. Add a new skill
employees.update_one(
    {"name": "Anu Joseph"},
    {"$push": {"skills": "data-modeling"}}
)

# 3. Remove a skill
employees.update_one(
    {"name": "Rakesh Pillai"},
    {"$pull": {"skills": "linux"}}
)

# 4. Update nested project status
employees.update_one(
    {"projects.name": "SecureBank"},
    {"$set": {"projects.$.status": "completed"}}
)

# 5. Add new project entries
employees.update_one(
    {"name": "Maya Kumar"},
    {"$push": {"projects": {"name": "AIResearch", "status": "planned"}}}
)

# 6. Increment experience counter
employees.update_many(
    {},
    {"$inc": {"experience_years": 1}}
)

# 7. Rename a field
employees.update_many(
    {},
    {"$rename": {"department": "dept"}}
)

# 8. Delete a field
employees.update_many(
    {},
    {"$unset": {"address.state": ""}}
)

# 9. Bulk update based on conditions
employees.update_many(
    {"dept": "Cloud"},
    {"$set": {"dept": "Cloud-Engineer"}}
)

# 10. Upsert employee profile if not found
employees.update_one(
    {"emp_id": 200},
    {"$set": {
        "name": "New Employee",
        "age": 25,
        "dept": "AI",
        "skills": ["python"],
        "address": {"city": "Mumbai"},
        "projects": [],
        "experience_years": 0
    }},
    upsert=True
)

print("All update operations executed successfully.")


# 1. Delete individual employee profile (by emp_id)
employees.delete_one({"emp_id": 105})
print("Deleted employee with emp_id 105")

# 2. Delete employees matching conditions (e.g., low experience < 1 year)
employees.delete_many({"experience_years": {"$lt": 1}})
print("Deleted employees with experience < 1 year")

# 3. Delete specific fields (not entire document)
# Example: remove the 'dept' field from all employees
employees.update_many({}, {"$unset": {"dept": ""}})
print("Removed 'dept' field from all employees")

# 4. Remove array elements (skills, projects)
# Remove a skill from a specific employee
employees.update_one({"name": "Rakesh Pillai"}, {"$pull": {"skills": "linux"}})
print("Removed 'linux' skill from Rakesh Pillai")

# Remove a project from a specific employee
employees.update_one({"name": "Maya Kumar"}, {"$pull": {"projects": {"name": "VisionAI"}}})
print("Removed 'VisionAI' project from Maya Kumar")