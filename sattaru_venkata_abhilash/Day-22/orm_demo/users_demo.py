from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, declarative_base

# Correct DATABASE_URL
DATABASE_URL = "mysql+pymysql://root:1234@localhost:3306/ust_db"

# Create the engine
engine = create_engine(DATABASE_URL, echo=True)

# Session local for managing the DB session
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)

# Base class for model definitions
Base = declarative_base()

# Define the User model (renaming from Person to User)
class User(Base):
    __tablename__ = 'users'  # Updated table name from 'persons' to 'users'
    
    id = Column(Integer, primary_key=True, index=True)  # Corrected `column` to `Column`
    name = Column(String(50))
    email = Column(String(100), unique=True, nullable=False)
    
    def __repr__(self):
        return f"User(id={self.id}, name='{self.name}', email='{self.email}')"
    
print("Creating tables in MySQL DB......")

# Create tables
Base.metadata.create_all(bind=engine)

print("Table creation completed")


def create_user(name: str, email: str):
    try:
        session = SessionLocal()  
        
        new_user = User(name=name, email=email) 
        
        session.add(new_user)
        
        session.commit()
        
        session.refresh(new_user)
        
    except Exception as e:
        session.rollback()
        
        print("Exception: ", e)  
        
        return None
    
    finally:
        session.close()
    
    return new_user


def get_all_users():
    try:
        session = SessionLocal()
        
        users = session.query(User).all()  
        
        return users  
        
    except Exception as e:
        session.rollback()
        
        print("Exception: ", e)
        
        return None
    
    finally:
        session.close()


def get_user_by_id(user_id: int):  
    try:
        session = SessionLocal()
        user = session.query(User).filter(User.id == user_id).first()  
    except Exception as e:
        session.rollback()
        print("Exception: ", e)
        return None
    finally:
        session.close()
    
    return user


def update_user_by_id(id: int, updated_user: User):  
    try:
        session = SessionLocal()
        user = session.query(User).filter(User.id == id).first()  
 
        if user is None:
            print("User not found!")
            return None
       
        user.email = updated_user.email
        session.commit()
        session.refresh(user)
    except Exception as e:
        session.rollback()
        print("Error:", e)
   
    finally:
        session.close()


def delete_user(user_id: int):  
    try:
        session = SessionLocal()
        user = session.query(User).filter(User.id == user_id).first() 
    
        if user is None:
            print("User not found!")
            return None 
        
        session.delete(user)
        session.commit()
    
    except Exception as e:
        session.rollback()
        print("Error:", e)
    
    finally:
        session.close()


if __name__ == "__main__":
    # Example usage:
    # Create user
    create_user("Deepika", "deepika@gmial.com")
    
    # Fetch all users
    data = get_all_users()
    print("All users:", data)
    
    # Fetch user by ID
    user_id = 2  
    user_by_id = get_user_by_id(user_id)
    print(f"\nUser with ID {user_id}: {user_by_id}")
    
    # Update user by ID
    updated_user = User(name="Deepika", email="deepika@gmial.com")  # Renamed from 'Person' to 'User'
    update_user_by_id(user_id, updated_user)
    
    # Delete user by ID
    delete_user(user_id)