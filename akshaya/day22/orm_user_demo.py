from sqlalchemy import create_engine,Integer,String,Column
from sqlalchemy.orm import sessionmaker,declarative_base

DATABASE_URL= "mysql+pymysql://root:akshaya@localhost:3306/ust_db"
engine=create_engine(DATABASE_URL,echo=True)
SessionLocal=sessionmaker(bind=engine,autoflush=False,autocommit=False)

Base=declarative_base()

class User(Base):
    __tablename__="users"
    
    id=Column(Integer,primary_key=True,index=True)
    name=Column(String(50))
    email=Column(String(100),unique=True,nullable=False)
    
    def __repr__(self):
        return f"User(id={self.id},name='{self.name}',email='{self.email}')"

print("creating tables in mysql db...")
Base.metadata.create_all(bind=engine)
print("table creation completed")

def create_user(name:str,email:str):
    try:
        session=SessionLocal()
        new_user=User(name=name,email=email)
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
        print("Exception:",e)
        return None
    finally:
        session.close()
    return users
    

# print(create_user("Akshhh","akshh@ust.com"))
# print(create_user("Katherine","kat@ust.com"))
# print(create_user("john","john@ust.com"))
# print(create_user("paul","paul@ust.com"))

# print(get_all_users())

def get_person_by_id(user_id:int):
    try:
        session=SessionLocal()
        user=session.query(User).filter(User.id==user_id).first()
    except Exception as e:
        session.rollback()
        print("Exception:",e)
        return None
    finally:
        session.close()
    return user
    
# print(get_person_by_id(1))

def update(person_id:int,email:str):
    try:
        session=SessionLocal()
        users=session.query(User).filter(User.id==person_id).first()
        if users is None:
            print("person not found!")
        users.email=email
        session.commit()
        print(users)
    except Exception as e:
        session.rollback()
        print("Exception:",e)
    finally:
        session.close()
        
# update(2,"kath@ust.com")
        
def delete(user_id:int):
    try:
        session=SessionLocal()
        user=session.query(User).filter(User.id==user_id).first()
        if user is None:
            print("User not found!")
            session.close()
        
        session.delete(user)
        session.commit()
        print("deleted")
    except Exception as e:
        session.rollback()
        print("Exception:",e)
    finally:
        session.close()
   
delete(4)       

