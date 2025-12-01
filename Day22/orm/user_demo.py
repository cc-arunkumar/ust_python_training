from sqlalchemy import create_engine,Column,Integer,String
from sqlalchemy.orm import sessionmaker,declarative_base

DATABASE_URL = "mysql+pymysql://root:pass%40word1@localhost:3306/aims_db"

engine  = create_engine(DATABASE_URL,echo=True)
SessionLocal = sessionmaker(bind=engine,autoflush=False,autocommit=False)

Base = declarative_base()

class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer,primary_key=True,index=True)
    name = Column(String(50))
    email = Column(String(100),unique=True,nullable=False)
    
    def __repr__(self):
        return f"User(id = {self.id}, name = '{self.name}',email = '{self.email}')"
    
print("creating tables in Mysql DB")
Base.metadata.create_all(bind=engine)
print("Table creation completed")


def create_user(name: str, email: str): 
    try:
        session = SessionLocal()
        new_person = User(name=name, email=email)
        session.add(new_person)
        session.commit()
        session.refresh(new_person)        
    except Exception as e:
        session.rollback()
        print("Exception", e)
        return None
    finally:
        session.close()
        
    return new_person

create_user("madhan", "madhnmad@ust.com")
create_user("gowt", "gowt@ust.com")
create_user("sou", "sou@ust.com")
create_user("dev", "dev@ust.com")

def get_all_users():
    try:
        session = SessionLocal()
        users = session.query(User).all()
        for user in users:
            print(f"User: Name = {user.name}, Email = {user.email}")
    except Exception as e:
        print("Exception", e)
        return None
    finally:
        session.close()
get_all_users()

def update_users(name: str, new_email: str):
    try:
        session = SessionLocal()
        user = session.query(User).filter(User.name == name).first()
        if user is None:
            print(f"User with name {name} not found!")
            return None
    
        user.email = new_email
        session.commit()
        session.refresh(user)
        print(f"User updated: Name = {user.name}, New Email = {user.email}")
        
    except Exception as e:
        session.rollback()
        print("Exception", e)
        return None
    finally:
        session.close()
    
    
def delete_person(person_id: int):
    try:
        session = SessionLocal()
        person = session.query(User).filter(User.id == person_id).first()
        
        if person is None:
            print(f"Person with ID {person_id} not found!")
            return None

        session.delete(person)
        session.commit()
        print(f"Person with ID {person_id} has been deleted")
        
    except Exception as e:
        session.rollback()
        print("Exception", e)
        return None
    finally:
        session.close()

