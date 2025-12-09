from sqlalchemy import create_engine,Column,Integer,String
from sqlalchemy.orm import sessionmaker,declarative_base
from pydantic import BaseModel

DATABASE_URL="mysql+pymysql://root:password123@localhost:3306/ust_db"
engine=create_engine(DATABASE_URL,echo=True)
SessionLocal=sessionmaker(bind=engine,autoflush=False,autocommit=False)

Base=declarative_base()
class User(Base,BaseModel):
    __tablename__="users"
    id=Column(Integer,primary_key=True,index=True)
    name=Column(String(50))
    email=Column(String(100),nullable=False,unique=True)
    
    def __repr__(self):
        return f"User(id ={self.id},name = {self.name},email ={self.email})"

Base.metadata.create_all(bind=engine)
    
def get_all_users():
    try:
        session=SessionLocal()
        users=session.query(User).all()
        return users
    except Exception as e:
        print("Exception :",e)
        return None
    finally:
        session.close()
        
def get_user_by_id(id:int):
    try:
        session=SessionLocal()
        user=session.query(User).filter(User.id==id).first()
        return user
    except Exception as e:
        print("Exception :",e)
        return None
    finally:
        session.close()
        
def create_user(name:str,email:str):
    try:
        session=SessionLocal()
        new_user=User(name=name,email=email)
        session.add(new_user)
        session.commit()
        session.refresh(new_user)
        return new_user
    except Exception as e:
        print("Exception :",e)
        return None
    finally:
        session.close()
    
def update_user_by_id(id:int,email:str):
    try:
        session=SessionLocal()
        user=session.query(User).filter(User.id==id).first()
        if user is None :
            print("User Not found")
            return None
        user.email=email
        session.commit()
        session.refresh(user)
        return user
    except Exception as e:
        print("Exception :",e)
        return None
    finally:
        session.close()
    
def delete_user_by_id(id:int):
    try:
        session=SessionLocal()
        user=session.query(User).filter(User.id==id).first()
        if user is None :
            print("User Not found")
            return None
        session.delete(user)
        session.commit()
        return "deleted"
    except Exception as e:
        print("Exception :",e)
        return None
    finally:
        session.close()
        
        
if __name__=="__main__":
    # user=create_user("shyam","shyamsunder@gamil.com")
    # print(user)
    
    # data=get_all_users()
    # for row in data:
    #     print(row)
    
    # print(get_user_by_id(2))
    
    # print(update_user_by_id(2,"ram@gmail.com"))
    
    print(delete_user_by_id(2))
    