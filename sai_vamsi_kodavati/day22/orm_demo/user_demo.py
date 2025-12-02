from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, declarative_base
 

DATABASE_URL = "mysql+pymysql://root:12345@localhost:3306/ust_db"

engine = create_engine(DATABASE_URL, echo=True)

SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)
 

Base = declarative_base()
 

class User(Base):
    __tablename__ = 'users'  
   
    id = Column(Integer, primary_key=True, index=True)  
    name = Column(String(50))
    email = Column(String(100), unique=True, nullable=False)
   
    def __repr__(self):
        return f"User(id={self.id}, name='{self.name}', email='{self.email}')"
   
print("Creating tables in MySQL DB......")
 
# Create tables
Base.metadata.create_all(bind=engine)
 
print("Table creation completed")
 
 
# def create_user(name: str, email: str):
#     try:
#         session = SessionLocal()  
       
#         new_user = User(name=name, email=email)  
       
#         session.add(new_user)
       
#         session.commit()
       
#         session.refresh(new_user)
       
#     except Exception as e:
#         session.rollback()
       
#         print("Exception: ", e)  
       
#         return None
   
#     finally:
#         session.close()
   
#     return new_user

# if __name__ == "__main__":
#     create_user("Vikash", "vikas@gmail.com")
 
# def get_all_users():
#     try:
#         session = SessionLocal()
       
#         users = session.query(User).all()  
       
#         return users  
       
#     except Exception as e:
#         session.rollback()
       
#         print("Exception: ", e)
       
#         return None
   
#     finally:
#         session.close()
 
# if __name__ == "__main__":
#     data = get_all_users()
#     print(data)

# def get_user_by_id(user_id: int):  
#     try:
#         session = SessionLocal()
#         user = session.query(User).filter(User.id == user_id).first() 
#     except Exception as e:
#         session.rollback()
#         print("Exception: ", e)
#         return None
#     finally:
#         session.close()
   
#     return user
 
# if __name__ == "__main__":
#     data = get_user_by_id(1)
#     print(data)
    
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

if __name__ == "__main__":
        updated_user = User(1)  
        update_user_by_id(updated_user)
 
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
        delete_user(5)
 