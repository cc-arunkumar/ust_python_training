# from motor.motor_asyncio import AsyncIOMotorClient
from pymongo import MongoClient

# client = AsyncIOMotorClient("mongodb+srv://303391_db_user:5IhrghdRaiXTR22b@cluster0.i0ih74y.mongodb.net/?appName=Cluster0")
# db = client.file_upload_test
client = MongoClient('mongodb://localhost:27017/')
db = client['file_upload_db']

collections = {
    "employees": db.employees,
    "jobs": db.jobs,
    "resource_request":db.resource_request,
    "applications": db.applications,
    "users": db.users,
    "refresh_tokens": db.refresh_tokens,
    "audit_logs": db.audit_logs
}