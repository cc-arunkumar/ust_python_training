from pymongo import MongoClient
from datetime import datetime

# Connect to MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['ust_db']

print("Database created successfully.")

# Create or switch to a collection
employees = db['employees']

# Create or switch to counters collection
counters = db['counters']


employee_details = [
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
        "projects": [
            {"name": "USTCloudPortal", "status": "planned"}
        ],
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
        "projects": [
            {"name": "SecureBank", "status": "in-progress"}
        ],
        "experience_years": 5
    },
    {
        "emp_id": 105,
        "name": "Maya Kumar",
        "age": 25,
        "department": "AI",
        "skills": ["python", "deep-learning"],
        "address": {"city": "Bangalore", "state": "KA"},
        "projects": [
            {"name": "VisionAI", "status": "completed"}
        ],
        "experience_years": 2
    },
    {
        "emp_id": 106,
        "name": "Arjun S",
        "age": 28,
        "department": "Cloud",
        "skills": ["azure"],
        "address": {"city": "Kochi", "state": "Kerala"},
        "projects": [
            {"name": "DevOpsBoost", "status": "in-progress"}
        ],
        "experience_years": 4
    },
    {
        "emp_id": 107,
        "name": "Neha Mohan",
        "age": 24,
        "department": "Data",
        "skills": ["sql", "tableau"],
        "address": {"city": "Chennai", "state": "TN"},
        "projects": [
            {"name": "USTAnalyticsHub", "status": "planned"}
        ],
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
        "projects": [
            {"name": "QualityX", "status": "in-progress"}
        ],
        "experience_years": 0
    },
    {
        "emp_id": 110,
        "name": "Rakesh Pillai",
        "age": 30,
        "department": "Cybersecurity",
        "skills": ["networking", "firewall", "linux"],
        "projects": [
            {"name": "SecuritySuite", "status": "deployed"}
        ],
        "experience_years": 7
    }
]
employees.insert_many(employee_details)


if counters.find_one({"_id": "emp_id"}) is None:
    counters.insert_one({"_id": "emp_id", "sequence_value": 111}) 

def get_next_sequence(name):
    counter = counters.find_one_and_update(
        {"_id": name},
        {"$inc": {"sequence_value": 1}},
        return_document=True
    )
    return counter["sequence_value"]

new_employees = [
    {
        "emp_id": get_next_sequence("emp_id"),
        "name": "Joseph Mathew",
        "age": 27,
        "department": "AI",
        "skills": ["python", "ml"],
        "address": {"city": "Mumbai", "state": "MH"},
        "projects": [{"name": "SmartVision", "status": "planned"}],
        "experience_years": 2
    },
    {
        "emp_id": get_next_sequence("emp_id"),
        "name": "Devika Nair",
        "age": 26,
        "department": "AI",
        "skills": ["python", "nlp"],
        "address": {"city": "Trivandrum", "state": "Kerala"},
        "projects": [{"name": "ChatBotX", "status": "planned"}],
        "experience_years": 3
    },
    {
        "emp_id": get_next_sequence("emp_id"),
        "name": "Karthik R",
        "age": 28,
        "department": "Cloud",
        "skills": ["aws", "terraform"],
        "address": {"city": "Bangalore", "state": "KA"},
        "projects": [{"name": "InfraBoost", "status": "in-progress"}],
        "experience_years": 4
    },
    {
        "emp_id": get_next_sequence("emp_id"),
        "name": "Snehal Patil",
        "age": 24,
        "department": "Testing",
        "skills": ["selenium", "pytest"],
        "address": {"city": "Pune", "state": "MH"},
        "projects": [{"name": "AutoTestSuite", "status": "completed"}],
        "experience_years": 2
    },
    {
        "emp_id": get_next_sequence("emp_id"),
        "name": "Rohan Gupta",
        "age": 30,
        "department": "Cybersecurity",
        "skills": ["linux", "firewall"],
        "address": {"city": "Delhi", "state": "DL"},
        "projects": [{"name": "SecureVault", "status": "deployed"}],
        "experience_years": 6
    },
    {
        "emp_id": get_next_sequence("emp_id"),
        "name": "Aishwarya S",
        "age": 22,
        "department": "Data",
        "skills": ["sql", "powerbi"],
        "address": {"city": "Chennai", "state": "TN"},
        "projects": [{"name": "DataInsights", "status": "planned"}],
        "experience_years": 1
    },
    {
        "emp_id": get_next_sequence("emp_id"),
        "name": "Vivek Sharma",
        "age": 27,
        "department": "AI",
        "skills": ["deep-learning", "opencv"],
        "address": {"city": "Hyderabad", "state": "TS"},
        "projects": [{"name": "VisionTrack", "status": "in-progress"}],
        "experience_years": 3
    },
    {
        "emp_id": get_next_sequence("emp_id"),
        "name": "Megha Rao",
        "age": 25,
        "department": "Cloud",
        "skills": ["azure", "docker"],
        "address": {"city": "Kochi", "state": "Kerala"},
        "projects": [{"name": "CloudSync", "status": "completed"}],
        "experience_years": 2
    },
    {
        "emp_id": get_next_sequence("emp_id"),
        "name": "Siddharth Jain",
        "age": 29,
        "department": "Data",
        "skills": ["hadoop", "spark"],
        "address": {"city": "Noida", "state": "UP"},
        "projects": [{"name": "BigDataHub", "status": "in-progress"}],
        "experience_years": 5
    },
    {
        "emp_id": get_next_sequence("emp_id"),
        "name": "Priyanka Das",
        "age": 23,
        "department": "Testing",
        "skills": ["manual-testing"],
        "address": {"city": "Kolkata", "state": "WB"},
        "projects": [],
        "experience_years": 1
    },
    {
        "emp_id": get_next_sequence("emp_id"),
        "name": "Harish K",
        "age": 31,
        "department": "Cybersecurity",
        "skills": ["siem", "threat-hunting"],
        "address": {"city": "Trivandrum", "state": "Kerala"},
        "projects": [{"name": "ThreatShield", "status": "planned"}],
        "experience_years": 7
    },
    {
        "emp_id": get_next_sequence("emp_id"),
        "name": "Anjali Verma",
        "age": 26,
        "department": "AI",
        "skills": ["mlops"],
        "address": {"city": "Pune", "state": "MH"},
        "projects": [{"name": "MLPipeline", "status": "in-progress"}],
        "experience_years": 3
    },
    {
        "emp_id": get_next_sequence("emp_id"),
        "name": "Rajesh Iyer",
        "age": 28,
        "department": "Cloud",
        "skills": ["gcp", "kubernetes"],
        "address": {"city": "Bangalore", "state": "KA"},
        "projects": [{"name": "CloudOps", "status": "completed"}],
        "experience_years": 4
    },
    {
        "emp_id": get_next_sequence("emp_id"),
        "name": "Divya Menon",
        "age": 22,
        "department": "Data",
        "skills": ["excel"],
        "address": {"city": "Kochi", "state": "Kerala"},
        "projects": [],
        "experience_years": 1
    },
    {
        "emp_id": get_next_sequence("emp_id"),
        "name": "Manoj Kumar",
        "age": 32,
        "department": "Cybersecurity",
        "skills": ["networking", "ids"],
        "address": {"city": "Delhi", "state": "DL"},
        "projects": [{"name": "SecureNet", "status": "deployed"}],
        "experience_years": 8
    }
    ]

employees.insert_many(new_employees)
print("Inserted 14 more employees with auto-increment emp_id.")
# Insert all documents at once
insert_many_result = employees.insert_many(employee_details)
print("Inserted IDs:", insert_many_result.inserted_ids)

# Print all documents in the collection
print("\nAll employees in collection:")
for emp in employees.find():
    print(emp)

#find employees by department:
print("\nEmployees in AI Department:")
for emp in employees.find({"department": "AI"}):
    print(emp)

print("\nEmployees with skill 'python':")
for emp in employees.find({"skills": "python"}):
    print(emp)

print("\nEmployees from city Kochi:")
for emp in employees.find({"address.city": "Kochi"}):
    print(emp)

print("\nEmployees with experience between 2 and 5 years:")
for emp in employees.find({"experience_years": {"$gte": 2, "$lte": 5}}):
    print(emp)

print("\nEmployees missing skills field:")
for emp in employees.find({"skills": {"$exists": False}}):
    print(emp)

print("\nEmployees with project status 'in-progress':")
for emp in employees.find({"projects.status": "in-progress"}):
    print(emp)

print("\nEmployees sorted by age descending:")
for emp in employees.find().sort("age", -1):
    print(emp)
    

employees.update_one({"emp_id": 101}, {"$set": {"department": "Data Science"}})
employees.update_one({"emp_id": 102}, {"$push": {"skills": "kubernetes"}})

employees.update_one(
    {"emp_id": 104, "projects.name": "SecureBank"},
    {"$set": {"projects.$.status": "completed"}}
)

employees.update_many({}, {"$inc": {"experience_years": 1}})
employees.update_many({}, {"$unset": {"address.state": ""}})
employees.update_many({"department": "Cloud"}, {"$set": {"department": "Cloud-Engineer"}})

employees.update_one(
    {"emp_id": 120},
    {"$set": {"name": "New Employee", "age": 22, "department": "AI", "experience_years": 0}},
    upsert=True
)


employees.delete_one({"emp_id": 109})

employees.delete_many({"experience_years": {"$lt": 2}})

employees.update_many({}, {"$unset": {"department": ""}})

employees.update_many({}, {"$pull": {"skills": "mongodb"}})
