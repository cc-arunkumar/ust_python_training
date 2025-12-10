from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017')

db = client['ust_db']
employees = db["employees"]

sample_employees = [
    {
        "emp_id": 101,
        "name": "Anu Joseph",
        "age": 23,
        "department": "AI",
        "skills": ["python", "mongodb"],
        "address": {"city": "Trivandrum", "state": "Kerala"},
        "projects": [
            {"name": "VisionAI", "status": "completed"},
            {"name": "DocScan", "status": "in-progress"}
        ],
        "experience_years": 1
    },
    {
        "emp_id": 102,
        "name": "Rahul Menon",
        "age": 26,
        "department": "Cloud",
        "skills": ["aws", "docker"],
        "address": {"city": "Kochi", "state": "Kerala"},
        "projects": [{"name": "USTCloudPortal", "status": "planned"}],
        "experience_years": 3
    },
    {
        "emp_id": 103,
        "name": "Sahana R",
        "age": 22,
        "department": "Testing",
        "skills": ["selenium"],
        "address": {"city": "Chennai", "state": "TN"},
        "projects": [],
        "experience_years": 1
    },
    {
        "emp_id": 104,
        "name": "Vishnu Prakash",
        "age": 29,
        "department": "Cybersecurity",
        "skills": ["networking", "siem"],
        "address": {"city": "Trivandrum", "state": "Kerala"},
        "projects": [{"name": "SecureBank", "status": "in-progress"}],
        "experience_years": 5
    },
    {
        "emp_id": 105,
        "name": "Maya Kumar",
        "age": 25,
        "department": "AI",
        "skills": ["python", "deep-learning"],
        "address": {"city": "Bangalore", "state": "KA"},
        "projects": [{"name": "VisionAI", "status": "completed"}],
        "experience_years": 2
    },
    {
        "emp_id": 106,
        "name": "Arjun S",
        "age": 28,
        "department": "Cloud",
        "skills": ["azure"],
        "address": {"city": "Kochi", "state": "Kerala"},
        "projects": [{"name": "DevOpsBoost", "status": "in-progress"}],
        "experience_years": 4
    },
    {
        "emp_id": 107,
        "name": "Neha Mohan",
        "age": 24,
        "department": "Data",
        "skills": ["sql", "tableau"],
        "address": {"city": "Chennai", "state": "TN"},
        "projects": [{"name": "USTAnalyticsHub", "status": "planned"}],
        "experience_years": 2
    },
    {
        "emp_id": 108,
        "name": "Suresh B",
        "age": 27,
        "department": "Data",
        "address": {"city": "Kochi", "state": "Kerala"},
        "projects": [],
        "experience_years": 3
    },
    {
        "emp_id": 109,
        "name": "Lavanya N",
        "age": 21,
        "department": "Testing",
        "skills": [],
        "address": {"city": "Trivandrum", "state": "Kerala"},
        "projects": [{"name": "QualityX", "status": "in-progress"}],
        "experience_years": 0
    },
    {
        "emp_id": 110,
        "name": "Rakesh Pillai",
        "age": 30,
        "department": "Cybersecurity",
        "skills": ["networking", "firewall", "linux"],
        "projects": [{"name": "SecuritySuite", "status": "deployed"}],
        "experience_years": 7
    }
]

# result = employees.insert_many(sample_employees)
# print("inserted ids:",result.inserted_ids)
# print("total employees:",len(result.inserted_ids))



# count = db.employees.count_documents({})
# print("Total employees:", count)
# Example bulk employees without emp_id
bulk_employees = [
    {
        "name": "Anjali Gupta",
        "age": 26,
        "department": "AI",
        "skills": ["python", "deep-learning", "nlp"],
        "address": {"city": "Hyderabad", "state": "TS"},
        "projects": [{"name": "ChatBotX", "status": "planned"}],
        "experience_years": 2
    },
    {
        "name": "Vishal Singh",
        "age": 29,
        "department": "Testing",
        "skills": ["selenium", "automation"],
        "address": {"city": "Delhi", "state": "DL"},
        "projects": [
            {"name": "QualityX", "status": "in-progress"},
            {"name": "TestSuite", "status": "planned"}
        ],
        "experience_years": 4
    },
    {
        "name": "Sneha Patil",
        "age": 24,
        "department": "Data",
        "skills": ["sql", "tableau"],
        "address": {"city": "Mumbai", "state": "MH"},
        "projects": [],
        "experience_years": 1
    },
    {
        "name": "Arjun Mehta",
        "age": 28,
        "department": "Cloud",
        "skills": ["azure", "kubernetes"],
        "address": {"city": "Chennai", "state": "TN"},
        "projects": [{"name": "DevOpsBoost", "status": "in-progress"}],
        "experience_years": 3
    },
    {
        "name": "Neha Sharma",
        "age": 27,
        "department": "Cybersecurity",
        "skills": ["linux", "siem"],
        "address": {"city": "Pune", "state": "MH"},
        "projects": [{"name": "SecureNet", "status": "planned"}],
        "experience_years": 5
    },
    {
        "name": "Suresh B",
        "age": 27,
        "department": "Data",
        "skills": ["sql", "powerbi"],
        "address": {"city": "Kochi", "state": "Kerala"},
        "projects": [],
        "experience_years": 3
    },
    {
        "name": "Lavanya N",
        "age": 21,
        "department": "Testing",
        "skills": [],
        "address": {"city": "Trivandrum", "state": "Kerala"},
        "projects": [{"name": "QualityX", "status": "in-progress"}],
        "experience_years": 0
    },
    {
        "name": "Rakesh Pillai",
        "age": 30,
        "department": "Cybersecurity",
        "skills": ["networking", "firewall", "linux"],
        "address": {"city": "Bangalore", "state": "KA"},
        "projects": [{"name": "SecuritySuite", "status": "deployed"}],
        "experience_years": 7
    }
]

last_emp = employees.find_one(sort=[("emp_id", -1)])
if last_emp:
    start_index = last_emp["emp_id"] + 1
else:
    start_index = 1


for i, emp in enumerate(bulk_employees, start=start_index):
    emp["emp_id"] = i

# employees.insert_many(bulk_employees)
# print("Bulk employees inserted with auto-generated emp_id")

nested_emp={
    "emp_id":204,
    "name":"Taniya",
    "age":22,
    "department":"data",
    "skills":["Sql","mongodb"],
    "address":{"city":"Trivandrum","state":"Kerala"},
    "projects":[]
}
# employees.insert_one(nested_emp)

employee_projects = {
    "emp_id": 205,
    "name": "Vishal Singh",
    "age": 29,
    "department": "sde",
    "skills": ["python", "sql"],
    "address": {"city": "trivandram", "state": "kerala"},
    "projects": [
        {"name": "ust_emp", "status": "in-progress"},
        {"name": "ust_talent", "status": "planned"}
    ],  
    "experience_years": 4
}

# employees.insert_one(employee_projects)

employee_skills={
    "emp_id":206,
    "name":"Anjali",
    "age":24,
    "department":"AI",
    "skills":["python","AI","ML"],
    "address":{"city":"triavandrum","state":"kerala"},
    "project":[{"name": "QualityX", "status": "in-progress"}],
    "experience_years":2
}
# employees.insert_one(employee_skills)



# for emp in employees.find({"department":"AI"}):
#     print(emp)

# for emp in employees.find({"skills":"python"}):
#     print(emp)
# query = {"address.city": "Trivandrum"}

# for emp in employees.find(query):
#     print(emp)

# for emp in employees.find({}):
#     if "skills" not in emp or len(emp["skills"])==0:
#         print("employee missing skills:",emp)
        
# query = {"experience_years": {"$gte": 2, "$lte": 5}}

# for emp in employees.find(query):
#     print(emp)
        
# query = {"projects.status":"in-progress"}
# for emp in employees.find(query):
#     print(emp)
    
# for emp in employees.find({},{"name":1,"department":1}):
#     print(emp)

# employees.update_one(
#    {"emp_id":101},
#    {"$set":{"department":"AI"}}
# )
# print("Employee updated successully")

# employees.update_many(
#     {"department":"Cloud"},
#     {"$set":{"department":"dev-ops"}})
# print("department updated")

# employees.update_one(
#     {"emp_id": 101, "projects.name": "DocScan"},
#     {"$set": {"projects.$.status": "completed"}}
# )
# print("employee project status updated ")

# employees.update_one(
#     {"emp_id": 102},
#     {"$push": {"projects": {"name": "NewPortal", "status": "planned"}}}
# )
# print("project added to emp")

# employees.update_many({}, {"$inc": {"experience_years": 1}})
# print("project exp incremented")


# employees.update_many({}, {"$rename": {"department": "dept"}})
# print("renamed done")
# employees.update_many({}, {"$unset": {"address.state": ""}})
# print("state field deleted")

employees.update_many(
    {"dept":"Data"},
    {"$set":{"dept":"Technical"}})

employees.update_one(
    {"emp_id":125},
    {"$set":{
        "name":"Manya gupta",
        "age":22,
        "dept":"AI",
        "skills":["Python","java"],
        "experience_years":1
    }},
    upsert=True
)
employees.delete_one({"emp_id": 101})
print("Deleted employee with emp_id 101")
employees.delete_many({"experience_years": {"$lt": 1}})
print("Deleted employees with less than 1 year experience")

employees.update_many({}, {"$unset": {"department": ""}})
print("Removed department field from all employees")

employees.update_one({"emp_id": 102}, {"$pull": {"skills": "docker"}})
employees.update_one({"emp_id": 103}, {"$pull": {"projects": {"name": "talent system"}}})

for emp in employees.find().sort("age",1):
    print(emp)
print("---------------------------------------")   
for emp in employees.find().sort("experience_years",-1):
    print(emp)
    