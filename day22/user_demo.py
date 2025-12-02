from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.orm import sessionmaker, declarative_base

# Database connection string (MySQL with PyMySQL driver)
DATABASE_URL = 'mysql+pymysql://root:password1@localhost:3306/ust_db'

# Create engine (echo=True prints SQL statements executed to console)
engine = create_engine(DATABASE_URL, echo=True)

# Session factory for DB transactions
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)

# Base class for ORM models
Base = declarative_base()

# ORM model mapped to 'user' table
class Users(Base):
    __tablename__ = 'user'
    
    id = Column(Integer, primary_key=True, index=True)   # Primary key
    name = Column(String(50))                            # User name
    email = Column(String(100), unique=True, nullable=False)  # Unique email
    
    def __repr__(self):
        return f"User(id={self.id}, name='{self.name}', email='{self.email}')"
    

# Function to insert a new user
def create_user(name: str, email: str):
    session = SessionLocal()
    try:
        new_user = Users(name=name, email=email)
        session.add(new_user)        # Add to session
        session.commit()             # Commit transaction
        session.refresh(new_user)    # Refresh to get auto-generated id
        print("User created:", new_user)
        return new_user
    except Exception as e:
        session.rollback()
        print("Exception:", e)
        return None
    finally:
        session.close()
        

# Function to update an existing user
def update_user(user_id: int, name: str = None, email: str = None):
    session = SessionLocal()
    try:
        user = session.query(Users).filter(Users.id == user_id).first()
        if user is None:
            print("Person not found")
            return None
        if name:
            user.name = name
        if email:
            user.email = email
        session.commit()
        session.refresh(user)
        print("Updated:", user)
        return user
    except Exception as e:
        session.rollback()
        print("Exception:", e)
        return None
    finally:
        session.close()
        

# Function to get all users
def get_all_users():
    session = SessionLocal()
    try:
        users = session.query(Users).all()
        return users
    except Exception as e:
        print("Exception:", e)
        return []
    finally:
        session.close()
        

# Function to get a user by ID
def get_user_by_id(user_id: int):
    session = SessionLocal()
    try:
        person = session.query(Users).filter(Users.id == user_id).first()
        return person
    except Exception as e:
        print("exception", e)
        return None
    finally:
        session.close()
        

# Function to delete a user
def delete_user(person_id: int):
    session = SessionLocal()
    try:
        person = session.query(Users).filter(Users.id == person_id).first()
        if person is None:
            print("Person not found")
            return None
        
        session.delete(person)
        session.commit()
        print("Deleted:", person)
        return person
    except Exception as e:
        session.rollback()
        print("Exception:", e)
        return None
    finally:
        session.close()
        

# ---------------- Main Execution ----------------
# Base.metadata.create_all(bind=engine)   # Uncomment to create table if not exists
if __name__ == "__main__":
    
    # Create a new user
    create_user("tharun","tharun@gmail.co")
    
    # Try updating user with id=3
    updated_user = update_user(3, name="Varsha Updated", email="varsha_updated@gmail.com")
    print(updated_user)
    
   
    
    # Delete user with id=2
    deleted_user = delete_user(2)
    print(deleted_user)
    
    # Fetch all users
    users = get_all_users()
    for u in users:
        print(u)
        
    # Try updating user with id=2
    updated_user = update_user(2, name="Varsha Upda", email="varsha_uped@gmail.com")
    print(updated_user)


# Output:

# 1.
# User created: User(id=1, name='tharun', email='tharun@gmail.co')

# 2.
# Updated: User(id=2, name='Varsha Upda', email='varsha_uped@gmail.com')
# User(id=2, name='Varsha Upda', email='varsha_uped@gmail.com')

# 3.
# Deleted: User(id=2, name='Varsha Upda', email='varsha_uped@gmail.com')
# User(id=2, name='Varsha Upda', email='varsha_uped@gmail.com')

# 4.
# User(id=1, name='tharun', email='tharun@gmail.co')
# User(id=3, name='Varsha Updated', email='varsha_updated@gmail.com')

# 5.
# Person not found
# None
