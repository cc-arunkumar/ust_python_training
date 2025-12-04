from sqlalchemy import create_engine,Column,Integer,String 
from sqlalchemy.orm import sessionmaker,declarative_base

DATABASE_URL="mysql+pymysql://root:raswanthi_1@localhost:3306/ust_db"
engine=create_engine(DATABASE_URL,echo=True)

SessionLocal=sessionmaker(bind=engine,autoflush=False,autocommit=False)

Base=declarative_base()
print(Base)

class User(Base):
    __tablename__="users"
    
    user_id=Column(Integer,primary_key=True,index=True)
    user_name=Column(String(50))
    email=Column(String(100),unique=True,nullable=False)
    
    def __repr__(self):
        return f"User(id={self.user_id}, name='{self.user_name}', email='{self.email}')"
    
print("Creating tables in MySQL DB...")
Base.metadata.create_all(bind=engine)
print("Table creation completed")

    
def create_user(user_name:str,email:str):
    try:
        session=SessionLocal()                    
        new_user=User(user_name=user_name,email=email)  
        session.add(new_user)                   
        session.commit()                          
        session.refresh(new_user)               
    except Exception as e:
        session.rollback()
        print("Exception:",e)
        return None 
    finally:
        session.close()
    return new_user.__dict__
        
        
def get_all_users():
    try:
        session=SessionLocal()
        users=session.query(User).all()
        
    except Exception as e:
        session.rollback()
        print("Exception",e)
        return None
    finally:
        session.close()
    return users


def get_user_by_id(user_id:int):
    try:
        session=SessionLocal()
        user=session.query(User).filter(User.user_id==user_id).first()
    except Exception as e:
        session.rollback()
        print("Exception",e)
        return None
    finally:
        session.close()
    return user


def update_user(user_id:int,email:str):
    try:
        session=SessionLocal()
        user=session.query(User).filter(User.user_id==user_id).first()
        
        if user is None:
            print("User not found !")
            return None 
        
        user.email=email
        session.commit()
        session.refresh(user)
        return user
    except Exception as e:
        session.rollback()
        print("Exception",e)
    finally:
        session.close()
    
    
    
def delete_user(user_id:int):
    try:
        session=SessionLocal()
        user=session.query(User).filter(User.user_id==user_id).first()
    
        if user is None:
            print("User not found !")
            session.close()
            return None 
        
        session.delete(user)
        
        session.commit()
        print("deleted")
    except Exception as e:
        session.rollback()
        print("Exception",e)
    finally:
        session.close()
    return user
    
# print(create_user("Ram","ram@example.com"))
# print(create_user("Tara","tara@example.com"))

# print(get_all_users())
# print(get_user_by_id(2))

# print(update_user("2","ram2@example.com"))

print(delete_user(3))