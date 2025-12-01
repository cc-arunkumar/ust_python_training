from sqlalchemy import create_engine,Column,String,Integer
from sqlalchemy.orm import sessionmaker,declarative_base

DATABASE_URL="mysql+pymysql://root:pass%40word1@localhost:3306/ust_db"
engine=create_engine(DATABASE_URL,echo=True)
SessionLocal=sessionmaker(bind=engine,autoflush=False,autocommit=False)

Base=declarative_base()
class User(Base):
    __tablename__='user'
    
    id=Column(Integer,primary_key=True,index=True)
    name=Column(String(100),nullable=False)
    email=Column(String(100),nullable=False,unique=True)
    
print("Creating tables in MYSQL DB")
Base.metadata.create_all(bind=engine)

def create_user(user_name:str,email:str):
    try:
        session=SessionLocal()
        
        new_user=User(name=user_name,email=email)
        
        session.add(new_user)
        
        session.commit()
        
        session.refresh(new_user)
        
    except Exception as e:
        session.rollback()
        print("Exception",e)
        return None
    finally:
        session.close()
    return new_user
result=create_user("Eleven","eleven@123")
print(f"Id:{result.id} name:{result.name} email:{result.email}")
        
def get_all_users():
    try:
        session=SessionLocal()
        User=session.query(User).all()
    except Exception as e:
        print("Exception",e)
    finally:
        session.close()
    return User

get_all_users()


def get_User_by_id(User_id:int):
    try:
        session=SessionLocal()
        User=session.query(User).filter(User.id==User_id).first()
    except Exception as e:
        session.close()
    return User

result=get_User_by_id(1)
# print(f"{result.id}{result.name}{result.email}")

def update_User(id,name,email):
    session =SessionLocal()
    User=session.query(User).filter(User.id==id).first()
    
    if User is None:
        print("User not found")
        session.close()
        return None
    User.name=name
    User.email=email
    session.commit()
    session.refresh(User)
    session.close()
    return User

def delete_User(User_id:int):
    session =SessionLocal()
    User=session.query(User).filter(User.id==User_id).first()
    
    if User is None:
        print("User not found")
        session.close()
        return None
    session.delete(User)
    session.commit()
    session.close()
    return User


update_User(1,"somu","somu@123")
# delete_User(10)       