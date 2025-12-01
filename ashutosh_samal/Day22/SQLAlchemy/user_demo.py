from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, declarative_base

# Database connection URL
DATABASE_URL = "mysql+pymysql://root:pass1word@localhost:3306/ust_db"

# Create engine and session factory
engine = create_engine(DATABASE_URL, echo=True)
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)
Base = declarative_base()

# User model
class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String(50), nullable=False)
    email = Column(String(100), unique=True, nullable=False)

    def __repr__(self):
        return f"User(id={self.id}, name='{self.name}', email='{self.email}')"

# Create tables
print("Creating tables in MySQL DB...")
Base.metadata.create_all(bind=engine)
print("Table creation completed")

# Create a new user
def create_user(name: str, email: str):
    try:
        session = SessionLocal()
        new_user = User(name=name, email=email)
        session.add(new_user)
        session.commit()
        session.refresh(new_user)
    except Exception as e:
        session.rollback()
        print("Exception:", e)
        return None
    finally:
        session.close()
    return new_user

print(create_user("Ashutosh","ashu@gmail.com"))
print(create_user("Deva","deva@gmail.com"))
print(create_user("Sovan","sovan@gmail.com"))
print(create_user("Harsh","harsh@gmail.com"))

# Fetch all users
def get_all_users():
    try:
        session = SessionLocal()
        users = session.query(User).all()
    except Exception as e:
        session.rollback()
        print("Exception:", e)
        return None
    finally:
        session.close()
    return users

print(get_all_users())


# Fetch user by ID
def get_user_by_id(user_id: int):
    try:
        session = SessionLocal()
        user = session.query(User).filter(User.id == user_id).first()
    except Exception as e:
        session.rollback()
        print("Exception:", e)
        return None
    finally:
        session.close()
    return user

print(get_user_by_id(1))


# Update user email by ID
def update_by_id(user_id: int, user_email: str):
    session = SessionLocal()
    user = session.query(User).filter(User.id == user_id).first()
    if user is None:
        print("Person not found")
        session.close()
        return None
    user.email = user_email
    session.commit()
    session.refresh(user)
    return user

print(update_by_id(1, "ashutosh@gmail.com"))


# Delete user by ID
def delete_user(user_id: int):
    session = SessionLocal()
    user = session.query(User).filter(User.id == user_id).first()
    if user is None:
        print("Person not found!")
        session.close()
        return None
    session.delete(user)
    session.commit()
    session.close()
    return user
print(delete_user(4))


