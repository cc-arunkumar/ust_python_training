from motor.motor_asyncio import AsyncIOMotorClient
import pymongo
import gridfs 

client = AsyncIOMotorClient("mongodb+srv://303391_db_user:5IhrghdRaiXTR22b@cluster0.i0ih74y.mongodb.net/?appName=Cluster0")
db = client.talent_management


# Use pymongo's synchronous client for GridFS
sync_client = pymongo.MongoClient("mongodb+srv://303391_db_user:5IhrghdRaiXTR22b@cluster0.i0ih74y.mongodb.net/?appName=Cluster0")
sync_db = sync_client.talent_management

# Use synchronous GridFS with pymongo
fs = gridfs.GridFS(sync_db)

collections = {
    "employees": db.employees,
    "jobs": db.jobs,
    "applications": db.applications,
    "users": db.users,
    "refresh_tokens": db.refresh_tokens,
    "audit_logs": db.audit_logs,
    "block_list_tokens":db.block_list_tokens
}


def get_gridfs():
    return fs

applications = db.applications
jobs = db.jobs
employees = db.employees
