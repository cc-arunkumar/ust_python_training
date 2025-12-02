from sqlalchemy import create_engine,Column,Integer,String
from sqlalchemy.orm import sessionmaker,declarative_base

DATABASE_URL="mysql+pymysql://root:password123@localhost:3306/ust_db"
engine=create_engine(DATABASE_URL)

SessionLocal=sessionmaker(bind=engine,autoflush=False,autocommit=False)
Base=declarative_base()

class User(Base):
    __tablename__="users"
    
    id=Column(Integer,primary_key=True,index=True)
    name=Column(String(50))
    email=Column(String(100),unique=True,nullable=False)
    
    def __repr__(self):
        return f"User(id={self.id}, name='{self.name}', email='{self.email}')'"

print("Ceating Tables in MySql DB...")
Base.metadata.create_all(bind=engine)
print("Table creation completed")




def create_user(name:str,email:str):
    try:
        session=SessionLocal()
        new_user=User(name=name,email=email)
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
    
    

def get_all_users():
    try:
        session=SessionLocal()
        users=session.query(User).all()
        for person in users:
            print(f"id={person.id} name={person.name} email={person.email}")
            
        session.commit()
    except Exception as e:
        session.rollback()
        return None
    finally:
        session.close()
        
        

def get_user_by_id(person_id:int):
    try:
        session=SessionLocal()
        user=session.query(User).filter(User.id==person_id).first()
        print(f"id={user.id} name={user.name} email={user.email}")
        session.commit()
    except Exception as e:
        session.rollback()
        return None
    finally:
        session.close()
        
        
def update_by_id(user_id:int,new_email:str):
    try:
        session=SessionLocal()
        user=session.query(User).filter(User.id==user_id).first()
        if user is None:
            print("Person not found")
            session.close()
            return None 
        user.email=new_email
        session.commit()
        session.refresh(user)
    except Exception as e:
        session.rollback()
    finally:
        session.close()
        
        
def delete_by_id(user_id:int):
    try:
        session=SessionLocal()
        user=session.query(User).filter(User.id==user_id).first()
        if user is None:
            print("User not found")
            session.close()
            return None 
        session.delete(user)
        session.commit()
    except Exception as e:
        session.rollback()
        return None
    finally:
        session.close()
        


    
        
    
        
    




if  __name__=="__main__":
    # create_user("Arun","arun123@gmail.com")
    # create_user("Felix","felix12@gmail.com")
    # create_user("Arjun","arjun12@gmail.com")
    # create_user("Akhil","akhil12@gmail.com")
    get_all_users()
    get_user_by_id(4)
    update_by_id(4,"felix123@gmail.com")
    delete_by_id(4)
    