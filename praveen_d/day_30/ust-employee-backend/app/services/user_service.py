from database.mongodb import user_collection
from schemas.users import UserSchema
from bson import ObjectId


# CREATE
def create_user(user: UserSchema):
    if user_collection.find_one({"emp_id": user.emp_id}):
        return None
    user_collection.insert_one(user.dict())
    return user.dict()


# READ BY ID
def get_user(emp_id: str):
    user = user_collection.find_one({"emp_id": emp_id}, {"_id": 0})
    return user


# UPDATE (PUT)
def update_user(emp_id: str, user: UserSchema):
    result = user_collection.update_one(
        {"emp_id": emp_id},
        {"$set": user.dict()}
    )
    if result.matched_count == 0:
        return None
    return user_collection.find_one({"emp_id": emp_id}, {"_id": 0})


# PATCH (role / status)
def patch_user(emp_id: str, data: dict):
    result = user_collection.update_one(
        {"emp_id": emp_id},
        {"$set": data}
    )
    if result.matched_count == 0:
        return None
    return user_collection.find_one({"emp_id": emp_id}, {"_id": 0})


# DELETE
def delete_user(emp_id: str):
    result = user_collection.delete_one({"emp_id": emp_id})
    return result.deleted_count > 0
