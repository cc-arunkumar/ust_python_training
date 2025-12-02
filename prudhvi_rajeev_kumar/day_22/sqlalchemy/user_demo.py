from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URL = "mysql+pymysql://root:pass%40word1@localhost:3306/ust_db"

engine = create_engine(DATABASE_URL, echo=True)
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)

Base  = declarative_base()

class User(Base):
    __tablename__ = 'users'
    
    user_id = Column(Integer, primary_key=True, index=True)
    user_name = Column(String(50))
    user_email = Column(String(100), unique=True, nullable=True)
    
    def __repr__(self):
        return f"{self.user_id}, {self.user_name}, {self.user_email}"
    
print("Creating tables.")
Base.metadata.create_all(bind=engine)
print("Table ceaation completed.")

def create_user(user_name : str, user_email : str):
    try:
        session = SessionLocal()
        new_user = User(user_name= user_name, user_email=user_email)
        session.add(new_user)
        session.commit()
        session.refresh(new_user)
    except Exception as e:
        session.rollback()
        print("Exception as : ", e)
        return None
    finally:
        session.close()
    
    return new_user

def get_all_users():
    try:
        session = SessionLocal()
        persons = session.query(User).all()
    except Exception as e:
        session.rollback()
        print("Exception as ", e)
        return None
    finally:
        session.close()
    return persons
       
def get_user_by_id(user_id : int):
    try:
        session = SessionLocal()
        user = session.query(User).filter(User.user_id == user_id).first()
    except Exception as e:
        session.rollback()
        print("Exception : ", e)
    finally:
        session.close()
    return user  

def update_user(user_id: int, new_email: str):
    try:
        session = SessionLocal()
        user = session.query(User).filter(User.user_id == user_id).first()
        if user is None:
            print("No user found.")
            return None
        
        user.user_email = new_email
        session.commit()
        session.refresh(user)
        return user
    except Exception as e:
        session.rollback()
        print("Exception in update_person:", e)
        return None
    finally:
        session.close()


def delete_user(user_id: int):
    try:
        session = SessionLocal()
        user = session.query(User).filter(User.user_id == user_id).first()
        if user is None:
            print("No user found.")
            return None
        
        session.delete(user)
        session.commit()
        return user
    except Exception as e:
        session.rollback()
        print("Exception in delete_user:", e)
        return None
    finally:
        session.close()

        
if __name__ == "__main__":
    # new_user = create_user("Harsh", "harshjaiswal@gmail.com")
    # print(f"User Created with id : {new_user.user_id}, name : {new_user.user_name}, email : {new_user.user_email}")
    
    get = get_all_users()
    for i in get:
        print(f"User {i.user_id}, name : {i.user_name}, {i.user_email}")
    
    user_by_id = get_user_by_id(4)

    
    
    
