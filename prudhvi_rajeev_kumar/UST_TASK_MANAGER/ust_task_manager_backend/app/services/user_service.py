from datetime import timedelta
from app.core.security import verify_password, hash_password, create_access_token

class UserService:
    def __init__(self, db):
        self.db = db

    def authenticate(self, user_id: str, password: str) -> str:
        user = self.db["users"].find_one({"UserId": user_id})
        if not user or user.get("status") != "active":
            raise ValueError("Invalid credentials")
        if not verify_password(password, user["Password"]):
            raise ValueError("Invalid credentials")
        return create_access_token(
            subject=user["UserId"],
            role=user["role"],
            status=user["status"],
            expires_delta=timedelta(minutes=60)
        )

    def create(self, user_id: str, password: str, role: str, status: str):
        if self.db["users"].find_one({"UserId": user_id}):
            raise ValueError("User already exists")
        hashed = hash_password(password)
        user = {"UserId": user_id, "Password": hashed, "role": role, "status": status}
        self.db["users"].insert_one(user)
        return {"user_id": user_id, "role": role, "status": status}

    def update(self, user_id: str, role: str | None, status: str | None):
        user = self.db["users"].find_one({"UserId": user_id})
        if not user:
            raise ValueError("User not found")
        update_fields = {}
        if role: update_fields["role"] = role
        if status: update_fields["status"] = status
        self.db["users"].update_one({"UserId": user_id}, {"$set": update_fields})
        user.update(update_fields)
        return {"user_id": user_id, "role": user["role"], "status": user["status"]}

    def delete(self, user_id: str) -> bool:
        result = self.db["users"].delete_one({"UserId": user_id})
        return result.deleted_count > 0

    def get(self, user_id: str):
        return self.db["users"].find_one({"UserId": user_id})
