# Day 24 - UST ESPTS MongoDB CRUD Coverage
# Run: python esp_ts_mongo.py

from pymongo import MongoClient, ASCENDING, DESCENDING
from pymongo.errors import DuplicateKeyError

# === CONFIG ===


client = MongoClient("mongodb://localhost:27017/")
db = client["ust_db"]
collection = db["talent_management"]


def reset_collection():
    """Drop and recreate collection collection with a unique index on emp_id."""
    db.drop_collection(collection)
    collection.create_index([("emp_id", ASCENDING)], unique=True)
    print("Reset collection and created unique index on emp_id.")
    
def get_last_emp_id():
    last_id =collection.find_one({},{"emp_id":1,"_id":0},sort=[("emp_id",-1)])
    if last_id:
        return last_id
    else:
        return 1



def seed_sample_data():
    docs = [
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
        # Additional 15 collection (111–125)
        {
            "emp_id": 111,
            "name": "Anjali Sharma",
            "age": 27,
            "department": "AI",
            "skills": ["python", "ml", "nlp"],
            "address": {"city": "Delhi", "state": "DL"},
            "projects": [{"name": "ChatAssist", "status": "in-progress"}],
            "experience_years": 4,
        },
        {
            "emp_id": 112,
            "name": "Kiran Patil",
            "age": 25,
            "department": "Cloud",
            "skills": ["aws", "terraform"],
            "address": {"city": "Pune", "state": "MH"},
            "projects": [{"name": "InfraScale", "status": "planned"}],
            "experience_years": 3,
        },
        {
            "emp_id": 113,
            "name": "Divya Nair",
            "age": 23,
            "department": "Data",
            "skills": ["sql", "powerbi"],
            "address": {"city": "Kochi", "state": "Kerala"},
            "projects": [{"name": "RetailInsights", "status": "completed"}],
            "experience_years": 2,
        },
        {
            "emp_id": 114,
            "name": "Rohit Verma",
            "age": 28,
            "department": "Testing",
            "skills": ["selenium", "pytest"],
            "address": {"city": "Bangalore", "state": "KA"},
            "projects": [{"name": "QualityX", "status": "in-progress"}],
            "experience_years": 4,
        },
        {
            "emp_id": 115,
            "name": "Meera Iyer",
            "age": 26,
            "department": "AI",
            "skills": ["python", "pytorch"],
            "address": {"city": "Chennai", "state": "TN"},
            "projects": [{"name": "VisionAI", "status": "planned"}],
            "experience_years": 3,
        },
        {
            "emp_id": 116,
            "name": "Varun Gupta",
            "age": 31,
            "department": "Cloud",
            "skills": ["gcp", "kubernetes"],
            "address": {"city": "Hyderabad", "state": "TS"},
            "projects": [{"name": "CloudNova", "status": "completed"}],
            "experience_years": 7,
        },
        {
            "emp_id": 117,
            "name": "Pooja R",
            "age": 24,
            "department": "Data",
            "skills": ["sql"],
            "address": {"city": "Mumbai", "state": "MH"},
            "projects": [],
            "experience_years": 2,
        },
        {
            "emp_id": 118,
            "name": "Aman Khan",
            "age": 27,
            "department": "Cybersecurity",
            "skills": ["siem", "iam"],
            "address": {"city": "Delhi", "state": "DL"},
            "projects": [{"name": "SecureBank", "status": "planned"}],
            "experience_years": 4,
        },
        {
            "emp_id": 119,
            "name": "Sneha T",
            "age": 22,
            "department": "Testing",
            "skills": ["postman"],
            "address": {"city": "Pune", "state": "MH"},
            "projects": [{"name": "QualityX", "status": "completed"}],
            "experience_years": 1,
        },
        {
            "emp_id": 120,
            "name": "Nitin J",
            "age": 29,
            "department": "Cloud",
            "skills": ["azure", "devops"],
            "address": {"city": "Bangalore", "state": "KA"},
            "projects": [{"name": "DevOpsBoost", "status": "in-progress"}],
            "experience_years": 5,
        },
        {
            "emp_id": 121,
            "name": "Ishita Sen",
            "age": 23,
            "department": "AI",
            "skills": [],
            "address": {"city": "Kolkata", "state": "WB"},
            "projects": [{"name": "NLPStudio", "status": "planned"}],
            "experience_years": 1,
        },
        {
            "emp_id": 122,
            "name": "Harish A",
            "age": 26,
            "department": "Data",
            "address": {"city": "Chennai", "state": "TN"},
            "projects": [{"name": "USTAnalyticsHub", "status": "in-progress"}],
            "experience_years": 3,
        },
        {
            "emp_id": 123,
            "name": "Kavya M",
            "age": 24,
            "department": "Testing",
            "skills": ["selenium", "cypress"],
            "address": {"city": "Hyderabad", "state": "TS"},
            "projects": [],
            "experience_years": 2,
        },
        {
            "emp_id": 124,
            "name": "Pradeep S",
            "age": 32,
            "department": "Cybersecurity",
            "skills": ["networking"],
            "address": {"city": "Trivandrum", "state": "Kerala"},
            "projects": [{"name": "SecuritySuite", "status": "deployed"}],
            "experience_years": 8,
        },
        {
            "emp_id": 125,
            "name": "Shruti R",
            "age": 27,
            "department": "AI",
            "skills": ["ml"],
            "address": {"city": "Pune", "state": "MH"},
            "projects": [{"name": "VisionAI", "status": "in-progress"}],
            "experience_years": 4,
        },
    ]

    collection.insert_many(docs)
    print(f"Inserted {len(docs)} collection.")


# === CREATE OPERATIONS ===
def create_individual():
    """Insert a single employee (unique emp_id enforced)."""
    try:
        doc = {
            "emp_id": 200,
            "name": "Temporary User",
            "age": 23,
            "department": "AI",
            "skills": ["python"],
            "address": {"city": "Sengaon", "state": "MH"},
            "projects": [{"name": "TempProj", "status": "planned"}],
            "experience_years": 1,
        }
        collection.insert_one(doc)
        print("Inserted individual employee with emp_id 200.")
    except DuplicateKeyError:
        print("emp_id 200 already exists; skipping.")


def create_bulk():
    """Bulk insert multiple collection; some intentionally missing fields."""
    docs = [
        {
            "emp_id": 201,
            "name": "Bulk One",
            "age": 24,
            "department": "Cloud",
            "skills": ["aws"],
            "address": {"city": "Mumbai", "state": "MH"},
            "projects": [],
            "experience_years": 2,
        },
        {
            "emp_id": 202,
            "name": "Bulk Two",
            "age": 22,
            "department": "Testing",
            # missing skills
            "address": {"city": "Chennai", "state": "TN"},
            "projects": [{"name": "BulkTest", "status": "planned"}],
            "experience_years": 1,
        },
    ]
    collection.insert_many(docs, ordered=False)
    print("Bulk inserted 2 collection (201–202).")


# === READ OPERATIONS ===
def read_examples():
    """Demonstrate queries: filters, projections, sorting, arrays, nested."""

    print("\n-- Department: Cloud --")
    for d in collection.find({"department": "Cloud"}):
        print(d["emp_id"], d["name"])

    print("\n-- Skill: selenium --")
    for d in collection.find({"skills": "selenium"}):
        print(d["emp_id"], d["name"], d.get("skills"))

    print("\n-- City: Chennai --")
    for d in collection.find({"address.city": "Chennai"}):
        print(d["emp_id"], d["name"], d["address"])


    print("\n-- Missing skills field --")
    for d in collection.find({"skills": {"$exists": False}}):
        print(d["emp_id"], d["name"])


    print("\n-- Experience 2 to 4 years --")
    for d in collection.find(
        {"experience_years": {"$gte": 2, "$lte": 4}}
    ).sort("experience_years", ASCENDING):
        print(d["emp_id"], d["name"], d["experience_years"])

    print("\n-- Project status: in-progress --")
    for d in collection.find({"projects.status": "in-progress"}):
        print(d["emp_id"], d["name"])

    print("\n-- >1 project --")
    for d in collection.find({"$where": "this.projects && this.projects.length > 1"}):
        print(d["emp_id"], d["name"], len(d.get("projects", [])))

    print("\n-- Projection: name + department only --")
    for d in collection.find({}, {"_id": 0, "name": 1, "department": 1}).limit(5):
        print(d)

    # Sorting examples
    print("\n-- Sort by age desc --")
    for d in collection.find({}).sort("age", DESCENDING).limit(5):
        print(d["emp_id"], d["name"], d["age"])

    print("\n-- Sort by name asc --")
    for d in collection.find({}).sort("name", ASCENDING).limit(5):
        print(d["emp_id"], d["name"])


# === UPDATE OPERATIONS ===
def update_examples():
    """Demonstrate $set, $inc, $unset, array ops ($push, $addToSet, $pull), nested updates, bulk, upsert."""

    collection.update_one({"emp_id": 103}, {"$set": {"department": "QA"}})
    print("Updated emp_id 103 department to QA.")


    collection.update_many({}, {"$inc": {"experience_years": 1}})
    print("Incremented experience_years for all collection by +1.")

    # $unset: remove address.state for all
    collection.update_many({}, {"$unset": {"address.state": ""}})
    print("Unset address.state for all collection.")

    # Array: add new skill using $push (duplicates allowed)
    collection.update_one({"emp_id": 105}, {"$push": {"skills": "mlops"}})
    print("Pushed 'mlops' to skills of emp_id 105.")

    # Array: add new skill using $addToSet (dedupe)
    collection.update_one({"emp_id": 102}, {"$addToSet": {"skills": "kubernetes"}})
    print("AddToSet 'kubernetes' to skills of emp_id 102.")

    # Array: remove a skill using $pull
    collection.update_one({"emp_id": 110}, {"$pull": {"skills": "linux"}})
    print("Pulled 'linux' from skills of emp_id 110.")

    # Nested array update: positional operator $ to update project status
    collection.update_one(
        {"emp_id": 101, "projects.name": "DocScan"},
        {"$set": {"projects.$.status": "completed"}},
    )
    print("Updated project 'DocScan' status to completed for emp_id 101.")

    # Bulk update: mark all cloud collection as 'Cloud-Engineer' title field
    collection.update_many({"department": "Cloud"}, {"$set": {"title": "Cloud-Engineer"}})
    print("Set title='Cloud-Engineer' for all Cloud department collection.")

    # Upsert: create/update if not found
    index =get_last_emp_id()
    collection.update_one(
        {"emp_id": 999},
        {
            "$set": {
                "name": "Upsert User",
                "age": 25,
                "department": "AI",
                "skills": ["python"],
                "address": {"city": "Pune"},
                "projects": [{"name": "UpsertProj", "status": "planned"}],
                "experience_years": 1,
            }
        },
        upsert=True,
    )
    print("Upserted employee with emp_id 999.")


# === DELETE OPERATIONS ===
def delete_examples():
    """Demonstrate deletion of docs, fields, and array elements."""
    # Delete precise by emp_id
    collection.delete_one({"emp_id": 200})
    print("Deleted employee with emp_id 200.")

    # Department-based deletion (e.g., Testing with experience <= 1)
    res = collection.delete_many({"department": "Testing", "experience_years": {"$lte": 1}})
    print(f"Deleted {res.deleted_count} Testing collection with <=1 year experience.")

    # Delete a field (simulate cleanup): remove 'title' field from all
    collection.update_many({}, {"$unset": {"title": ""}})
    print("Unset 'title' field from all collection.")

    # Remove array entry: remove a specific skill
    collection.update_one({"emp_id": 105}, {"$pull": {"skills": "mlops"}})
    print("Pulled 'mlops' from emp_id 105 skills.")

    # Remove a project by name
    collection.update_one({"emp_id": 101}, {"$pull": {"projects": {"name": "VisionAI"}}})
    print("Removed project 'VisionAI' from emp_id 101.")

    # Delete collection with no skills
    res = collection.delete_many({"$or": [{"skills": {"$exists": False}}, {"skills": {"$size": 0}}]})
    print(f"Deleted {res.deleted_count} collection with no skills.")
    # Delete collection with experience <= 1
    res = collection.delete_many({"experience_years": {"$lte": 1}})
    print(f"Deleted {res.deleted_count} collection with <=1 year experience.")

    # Delete collection with no ongoing projects (no 'in-progress')
    res = collection.delete_many({"projects.status": {"$ne": "in-progress"}})
    print(f"Deleted {res.deleted_count} collection with no 'in-progress' projects.")


def main():
    reset_collection()
    seed_sample_data()

    create_individual()
    create_bulk()

    read_examples()


    update_examples()


    delete_examples()

    print("\nAll CRUD demonstrations completed.")


if __name__ == "__main__":
    main()
