from sqlalchemy import create_engine,Column,Integer,String
from sqlalchemy.orm import sessionmaker,declarative_base

DATABASE_URL = "mysql+pymysql://root:password123@localhost:3306/ust_db"
engine = create_engine(DATABASE_URL,echo = True)
SessionLocal = sessionmaker(bind=engine,autoflush=False,autocommit = False)

Base = declarative_base()

class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True,index=True)
    name = Column(String(50))
    email = Column(String(100),unique=True,nullable=False)
    
    def __repr__(self):
        return f"Userid = {self.id},name = {self.name},email = {self.email}"
    
print("Creating tables in Mysql DB...")
Base.metadata.create_all(bind=engine)
print("Table creation completed")

def create_user(name:str,email:str):
    try:
        
        session = SessionLocal()
        new_user = User(name = name,email =email)
        session.add(new_user)
        session.commit()
        session.refresh(new_user)
        
    except Exception as e:
        session.rollback()
        print("Exception: ",e)
        return None
    finally:
        session.close()
    return new_user.__dict__

def get_all():
    try:
        
        session = SessionLocal()
        users = session.query(User).all()
        for p in users:
            print(p)
        return users
    except Exception as e:
        session.rollback()
        print("Exception: ",e)
        return None
    finally:
        session.close()

def get_by_id():
    try:
        
        session = SessionLocal()
        user = session.query(user).filter(user.id==1).first()
        
        print(user)
        return user
    except Exception as e:
        session.rollback()
        print("Exception: ",e)
        return None
    finally:
        session.close()

def update_user(id:int,email:str):
    try:
        
        session = SessionLocal()
        user = session.query(User).filter(User.id==id).first()
        if not user:
            print("user not found !")
            return None
        user.email = email
        session.commit()
        session.refresh(user)
        return user
    except Exception as e:
        session.rollback()
        print("Exception: ",e)
        return None
    finally:
        session.close()

def delete_user(id:int):
    try:
        
        session = SessionLocal()
        user = session.query(User).filter(User.id==id).first()
        if not user:
            print("user not found !")
            return None
        session.delete(user)
        session.commit()
        return user
    except Exception as e:
        session.rollback()
        print("Exception: ",e)
        return None
    finally:
        session.close()


# create_user("arjun","arjun@gmail.com")
# create_user("felix","felix@gmail.com")
# create_user("arumukesh","aru@gmail.com")
# create_user("praveen","praveen@gmail.com")
get_all()
# get_by_id(1)
# update_user(5,"praveen123@gmail.com")
delete_user(5)