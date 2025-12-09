from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, declarative_base

Base = declarative_base()
class User(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    
    
DATABASE_URL = "mysql+pymysql://root:pass%40word1@localhost:3306/ust_db_employee"
engine = create_engine(DATABASE_URL)
Base.metadata.create_all(engine)
SessionLocal = sessionmaker(bind=engine)



def create_user(name: str, email: str):
    session = SessionLocal()
    try:
        user = User(name=name, email=email)
        session.add(user)
        session.commit()
        session.refresh(user)
        return user
    except Exception as e:
        session.rollback()
        print("Error:", e)
    finally:
        session.close()

# create_user("rohit", "rohit@gmail.com")
create_user("rohan", "rohan@gmail.com")
# create_user("shetty", "shetty@gmail.com")
# create_user("varun", "varun@gmail.com")


def get_user_by_id(user_id:int):
    session = SessionLocal()
    user = session.query(User).filter(user_id==User.id).first()
    print(" data found" ,"id :",user.id, "name:",user.name,"email:", user.email)
def get_all_users():
    session = SessionLocal()
    ans = session.query(User).all()
    for row in ans:
        print("id :",row.id, "name:",row.name,"email:", row.email )
ans = get_all_users()
    
def update_user_by_id(user_id:int,name:str):
    session = SessionLocal()
    user=session.query(User).filter(user_id==User.id).first()
    
    user.name=name
    
    session.commit()
    session.refresh(user)
    session.close()

    

# get_user_by_id(3)
# update_user_by_id(3,"Rohit")


def delete_user(user_id:int):
    session = SessionLocal()
    user=session.query(User).filter(user_id==User.id).first()
    
    if user is None:
        print("user not found")
        session.close()
        return None
    
    
    session.delete(user)
    session.commit()
    session.close()
    return user


# delete_user(2)

