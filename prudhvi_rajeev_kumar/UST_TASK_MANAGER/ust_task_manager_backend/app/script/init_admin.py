from argon2 import PasswordHasher
from pymongo import MongoClient

ph = PasswordHasher()
client = MongoClient("mongodb://localhost:27017")
db = client["ust_auth_db"]

admin_user = {
    "UserId": "admin1",
    "Password": ph.hash("yourpassword"),
    "role": "admin",
    "status": "active"
}

db.users.insert_one(admin_user)
print("Admin user created")

