from sqlalchemy import create_engine,Column,Integer,String
from sqlalchemy.orm import sessionmaker,declarative_base

DATABASE_URL="mysql+pymysql://root:1234@localhost:3306/ust_db"
engine=create_engine(DATABASE_URL,echo=False)
SessionLocal=sessionmaker(bind=engine,autoflush=False,autocommit=False)

Base=declarative_base()

class User(Base):
    __tablename__='users'
    
    user_id=Column(Integer,primary_key=True,index=True)
    user_name=Column(String(50))
    user_email=Column(String(100),unique=True,nullable=False)
    
    def __repr__(self):
        return f"User(id= {self.user_id},name= '{self.user_name}', email='{self.user_email}')"
    
print("Creating tables in mysql")
Base.metadata.create_all(bind=engine)
print("Table creation complete")




def create_user(name:str,email:str):
    try:
        session=SessionLocal()
        new_person=User(user_name=name,user_email=email)
        session.add(new_person)
        session.commit()
        session.refresh(new_person)
    except Exception as e:
        session.rollback()
        print("Error: ",e)
        return None
    finally:
        session.close()
    return new_person




def get_all_users():
    try:
        session=SessionLocal()
        users=session.query(User).all()
        session.close()
        return users
    except Exception as e:
        session.rollback()
        print("Error:",e)
    finally:
        session.close()
        
        
        
def get_users_by_id(user_id:int):
    try:
        session=SessionLocal()
        user=session.query(User).filter(User.user_id == user_id).first()
        session.close()
        return user
    except Exception as e:
        session.rollback()
        print("Error:",e)
    finally:
        session.close()

        


def update_user(user_id:int,new_email:str):
    session=SessionLocal()
    user=session.query(User).filter(User.user_id==user_id).first()
    
    if user is None:
        print("person not found")
        session.close()
        return None
    user.user_email=new_email
    # session.(person)
    session.commit()
    session.close()
    return user

     

def delete_user(user_id:int):
    session=SessionLocal()
    user=session.query(User).filter(User.user_id==user_id).first()
    
    if user is None:
        print("person not found")
        session.close()
        return None
    session.delete(user)
    session.commit()
    session.close()
    return user



        
        
# if __name__=="__main__":
#     created_user=create_user("reshma","reshma@gmail.com")
    
#     if created_user:
#         print(f"Created User: {created_user}")


        
# if __name__=="__main__":        
#     get_users_id=get_users_by_id(3)
#     print(get_users_id)
    

# update_user(4,"reshma_bhai@gmail.com") 

delete_user(4)

if __name__=="__main__":        
    get_users=get_all_users()
    for i in get_users:
        print(i)