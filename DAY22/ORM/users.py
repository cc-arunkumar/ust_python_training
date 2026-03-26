from sqlalchemy import create_engine,Column,String,Integer
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URL = "mysql+pymysql://root:pass%40word1@localhost:3306/ust_db"

engine=create_engine(DATABASE_URL,echo=False)
SessionLocal=sessionmaker(bind=engine,autoflush=False,autocommit=False)

Base=declarative_base()

class User(Base):
    __tablename__='users'
    
    id=Column(Integer,primary_key=True,index=True)
    name=Column(String(50))
    email=Column(String(100), unique=True,nullable=False)
    
    def __repr__(self):
        return f"User (id={self.id}, name='{self.name}', email='{self.email}')"

print("Creating tables")
Base.metadata.create_all(bind=engine)
print("Table Created")

def create_user(name:str, email:str):
    try:
        session=SessionLocal()
        new_user=User(name=name,email=email)
        session.add(new_user)
        session.commit()
        session.refresh(new_user)
    
    except Exception as e:
        session.rollback()
        print("Exception :",e)
        return None
    
    finally:
        session.close()
    return new_user


def get_all_users():
    session=SessionLocal()
    users=session.query(User).all()
    for user in users:
        print(f"User id : {user.id} | User name: {user.name} | User Email : {user.email}")
        print("")
    session.close()

def get_user_by_id(user_id:int):
    session=SessionLocal()
    users=session.query(User).filter(User.id==user_id).first()
    session.close()
    return users    


def update_user(user_id: int, email: str):
    session = SessionLocal()
    try:
        users=session.query(User).filter(User.id == user_id).first()
        
        if users is None:
            print("User not Found")
            return None
        
        users.email=email
        session.commit()
        session.refresh(users)
        return users
    
    except Exception as e:
        session.rollback()
        print("Exception:", e)
        return None
    
    finally:
        session.close()


def delete_user(user_id:int):
    session=SessionLocal()
    user=session.query(User).filter(User.id==user_id).first()
    
    if user is None:
        print("User nor Found")
        session.close()
        return None
    print(user)
    session.delete(user)
    session.commit()
    session.close()
    



#CREATE

"""new_user1=create_user("Gowtham","gowtham10ja@gmail.com")
new_user2=create_user("Vijay","Vijay@gmail.com")
new_user3=create_user("DK","Dinesh@gmail.com")
new_user4=create_user("Vikram","vikram@gmail.com")
new_user5=create_user("ssk","ssk@gmail.com")"""

#GET ALL
# print(get_all_users())


#GET USERS BY ID
# print(get_user_by_id(3))

# UPDATE USER
# print(update_user(3,"mani@gmail.com"))


# DELETE USER

delete_user(5)