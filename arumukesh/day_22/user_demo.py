from sqlalchemy import create_engine,Integer,String,Column
from sqlalchemy.orm import sessionmaker,declarative_base

database_url = "mysql+pymysql://root:pass%40word1@localhost:3306/ust_db"

engine=create_engine(database_url,echo=True)
SessionLocal=sessionmaker(bind=engine,autoflush=False,autocommit=False)


Base= declarative_base()
class User(Base):
    __tablename__="users"
    
    id=Column(Integer,primary_key=True,index=True)
    name=Column(String(50))
    email=Column(String(50),unique=True,nullable=False)
    
    def __repr__(self):
        return f"User(id={self.id},name={self.name},email={self.email})"
    
print("creating tables")
Base.metadata.create_all(bind=engine)
print("table created ")


def create_user(name:str,email:str):
    try:
        session=SessionLocal()
        new_user=User(name=name,email=email)
        session.add(new_user)
        session.commit()
        session.refresh(new_user)
        
    except Exception as e:
        session.rollback()
        print(e)
        return None
    finally:
        session.close()
    return new_user


# print(create_user("arumuekh","arum@gmsul.com"))
    
# create_user("dadsa","asdasd@gmail")

def get_all():
    try:
        session=SessionLocal()
        users=session.query(User).all()
        # session.close()
        return users 
    except Exception as e:
        session.rollback()
        print(e)
        return None
    finally:
        session.close()
        
def get_user_by_id(id:int):
    session=SessionLocal()
    user=session.query(User).filter(User.id==id).first()
    session.close()
    return user

def update_user(id:int,new_email:str):
    session=SessionLocal()
    user=session.query(User).filter(User.id==id).first()
    if user is None:
        print("User not found")
        session.close()
        return None
    user.email=new_email
    session.commit()
    session.refresh(user)
    
def delete_user(id:int):
    session=SessionLocal()
    user=session.query(User).filter(User.id==id).first()
    if user is None:
        print("User not found")
        session.close()
        return None
    session.delete(user)
    session.commit()
    # session.refresh(user)
# print(get_all())

# print(create_user("akash","jsfvbhsjdfhyb"))
# update_user(1,"aaaaaaa")
# print(get_user_by_id(1))
print(delete_user(1))
print(get_user_by_id(1))