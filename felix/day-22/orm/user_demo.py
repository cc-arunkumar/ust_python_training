from sqlalchemy import create_engine,Column,Integer,String
from sqlalchemy.orm import sessionmaker,declarative_base

DATABASE_URL = "mysql+pymysql://root:felix_123@localhost:3306/ust_db"

engine = create_engine(DATABASE_URL,echo=True)

SessionLocal = sessionmaker(bind=engine,autoflush=False,autocommit=False)

Base = declarative_base()
class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer,primary_key=True,index=True)
    name = Column(String(50))
    email = Column(String(100),unique=True,nullable=False)
    
    def __repr__(self):
        return f"User_id = {self.id}, name = {self.name}' email = {self.email}"

print("Creating tables in mysql DB...")
Base.metadata.create_all(bind=engine)
print("Table creation completed")

def create_user(name:str , email:str):
    try:
        session = SessionLocal()
        
        new_user = User(name=name, email=email)
        
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

def get_all_users():
    try:
        session = SessionLocal()
        
        users = session.query(User).all()
        
        session.close()
        
        
        for user in users:
            # print(user.)
            print(f"ID: {user.id} | Name: {user.name} | Email: {user.email}")
    except Exception as e:
        print("ERROR: ",e)
    finally:
        print("Completed")
        
def get_user_by_id(user_id:int):
    try:
        session = SessionLocal()
        
        user = session.query(User).filter(User.id == user_id).first()
        
        print(f"ID: {user.id} | Name: {user.name} | Email: {user.email}")
        
        session.close()
    except Exception as e:
        print("ERROR: ",e)
    finally:
        print("Completed")
        
def update_user_by_id(user_id,new_email):
    try:
        session = SessionLocal()
        
        user = session.query(User).filter(User.id == user_id).first()
        
        if user is None:
            print("user not found")
            session.close()
            return None
        user.email = new_email
        session.commit()
        session.refresh(user)
        
        print(f"Updated -> ID: {user.id} | Name: {user.name} | Email: {user.email}")
        
        session.close()
    except Exception as e:
        print("ERROR: ",e)
    finally:
        print("Completed")
        
def delete_user_by_id(user_id):
    try:
        session = SessionLocal()
        
        user = session.query(User).filter(User.id == user_id).first()
        
        if user is None:
            print("user not found")
            session.close()
            return None
                
        
        session.delete(user)
        session.commit()
        session.close()
        print("user deleted")
    except Exception as e:
        print("ERROR: ",e)
    finally:
        print("Completed")
        
        
        
if __name__ =="__main__":
    # create_user("Felix","felix@ust.com")
    # create_user("Akhil","akhil@ust.com")
    # create_user("Arjun","arjun@ust.com")
    # create_user("Arun","arun@ust.com")
    # get_all_users()
    # get_user_by_id(1)
    # update_user_by_id(1,"Felix@ust.com")
    delete_user_by_id(1)
    