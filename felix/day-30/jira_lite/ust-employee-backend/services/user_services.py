from database.mysql_connection import SessionLocal, User

def get_all_Users():
    try:
        session = SessionLocal()
        Users = session.query(User).all()      
        session.close()
        if not Users:
            return {"detail":"No Users found"}
        return Users
    except Exception as e:
        print("ERROR: ",e)
    finally:
        print("Completed")
        
def get_User_by_id(emp_id:int):
    try:
        session = SessionLocal()
        user = session.query(User).filter(User.emp_id == emp_id).first()
        session.close()
        
        return user
    except Exception as e:
        print("ERROR: ",e)
    finally:
        print("Completed")

def authenticate_user(emp_id:int, password:str):
    """Verify emp_id and password against the users table.

    Returns the User ORM object on success, or None on failure.
    """

    try:
        user = get_User_by_id(emp_id)
        if not user:
            return None

        # NOTE: passwords are stored in plaintext in this schema. For production,
        # use a hashed password (bcrypt/argon2) and verify here instead.
        if user.password != password:
            return None

        return user
    except Exception as e:
        print("ERROR: ", e)
        return None
        
def create_User(user_data):
    try:
        session = SessionLocal()
        
        new_user = User(
            emp_id=user_data.emp_id,
            password=user_data.password,
            role=user_data.role,  
            status=user_data.status
        )
        
        session.add(new_user)
        session.commit()
        session.refresh(new_user)
    except Exception as e:
        session.rollback()
        print("ERROR: ,",e)
        return None
    finally:
        print("Completed")
    session.close()
    return new_user

def update_User(emp_id, updated_data):
    try:
        session = SessionLocal()
        
        # Fetch the User by ID
        user = session.query(User).filter(User.emp_id == emp_id).first()
        if not user:
            print("User not found")
            return None
        
        # Update fields
        user.password = updated_data.password
        user.role = updated_data.role  # Append new role
        user.status = updated_data.status
        
        session.commit()
        session.refresh(user)
        return user
    except Exception as e:
        session.rollback()
        print("ERROR:", e)
        return None
    finally:
        print("Completed")
        session.close()

def update_user_role(emp_id, new_role):
    try:
        session = SessionLocal()
        
        # Fetch the User by ID
        user = session.query(User).filter(User.emp_id == emp_id).first()
        if not user:
            print("User not found")
            return None
        
        # Update fields
        print("Current roles:", user.role)
        # for role in new_role:
        #     user.role.append(role) # Append new role
        user.role = new_role
        print("Updated roles:", user.role)
        
        session.commit()
        session.refresh(user)
        return user
    except Exception as e:
        session.rollback()
        print("ERROR:", e)
        return None
    finally:
        print("Completed")
        session.close()
        
def delete_User(emp_id,manager_id):
    try:
        session = SessionLocal()
        
        # Fetch the User by ID
        user = session.query(User).filter(User.emp_id == emp_id).filter(User.manager_id == manager_id).first()
        if not user:
            print("User not found")
            return None
        
        session.delete(user)
        session.commit()
        return True
    except Exception as e:
        session.rollback()
        print("ERROR:", e)
        return False
    finally:
        print("Completed")
        session.close()