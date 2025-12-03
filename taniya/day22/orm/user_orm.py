from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker

DATABASE_URL = "mysql+pymysql://root:pass%40word1@localhost:3306/ust_db"

engine = create_engine(DATABASE_URL, echo=True)
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    user_id = Column(Integer, primary_key=True, index=True)
    user_name = Column(String(50))
    user_email = Column(String(100), unique=True, nullable=True)

print("Creating tables in MySQL DB..")
Base.metadata.create_all(bind=engine)
print("Table creation completed")

def create_user(user_name: str, user_email: str):
    try:
        session = SessionLocal()
        new_user = User(user_name=user_name, user_email=user_email)
        session.add(new_user)
        session.commit()
        session.refresh(new_user)
    except Exception as e:
        session.rollback()
        print("Exception as:", e)
        return None
    finally:
        session.close()
    return new_user

def get_user():
    session = SessionLocal()
    users = session.query(User).all()
    session.close()
    return users

def get_user_by_id(user_id: int):
    session = SessionLocal()
    user = session.query(User).filter(User.user_id == user_id).first()
    session.close()
    return user

def update_user(user_id: int, new_name: str, new_email: str):
    try:
        session = SessionLocal()
        user = session.query(User).filter(User.user_id == user_id).first()
        if not user:
            print("user id not found")
            return None
        if new_name:
            user.user_name = new_name
        if new_email:
            user.user_email = new_email
        session.commit()
        session.refresh(user)
        return user
    except Exception as e:
        session.rollback()
        print("Exception while updating user:", e)
        return None
    finally:
        session.close()

def delete_user(user_id: int):
    try:
        session = SessionLocal()
        user = session.query(User).filter(User.user_id == user_id).first()
        if not user:
            print("user id not found")
            return None
        session.delete(user)
        session.commit()
        print(f"User with id={user_id} deleted successfully")
        return True
    except Exception as e:
        session.rollback()
        print("Exception while deleting user:", e)
        return False
    finally:
        session.close()

if __name__ == "__main__":
    # person = create_user("Taniya", "taniya22@gmail.com")
    # print(person)

    # person = create_user("Tanu", "taniya2219@gmail.com")
    # print(person)

    # person = create_user("Tanvi", "tanvii21220@gmail.com")
    # print(person)

    users = get_user()
    for u in users:
        print("id:", u.user_id, "name:", u.user_name, "email:", u.user_email)
    user = get_user_by_id(2)
    if user:
        print("Fetched by ID, id:", user.user_id, "name:", user.user_name, "email:", user.user_email)
    else:
        print("No user found with id=2")
        
    updated = update_user(2, new_name="Tanu Updated", new_email="tanu_updated@gmail.com")
    if updated:
        print("Updated:", updated.user_id, updated.user_name, updated.user_email)

    deleted = delete_user(3)
    if deleted:
        print("User deleted successfully")
        
    users = get_user()
    for u in users:
        print("id:", u.user_id, "name:", u.user_name, "email:", u.user_email)