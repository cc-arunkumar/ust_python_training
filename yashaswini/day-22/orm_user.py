# import SQLAlchemy core modules
from sqlalchemy import create_engine, Column, Integer, String
# import SQLAlchemy ORM modules
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URL = "mysql+pymysql://root:password123@localhost:3306/ust_db"
engine = create_engine(DATABASE_URL, echo=True)
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)

Base = declarative_base()

class Users(Base):
    __tablename__ = 'Users'
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50))
    email = Column(String(100), unique=True, nullable=False)
    
    def __repr__(self):
        return f"User(id={self.id}, name='{self.name}', email='{self.email}')"


# ------------------ CREATE ------------------
def create_user(name: str, email: str):
    try:
        session = SessionLocal()
        new_user = Users(name=name, email=email)
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


# ------------------ READ ------------------
def get_all_users():
    try:
        session = SessionLocal()
        user = session.query(Users).all()
    except Exception as e:
        session.rollback()
        print("Exception:", e)
        return None
    finally:
        session.close()
    return user


def get_user_by_id(person_id: int):
    try:
        session = SessionLocal()
        user = session.query(Users).filter(Users.id == person_id).first()
    except Exception as e:
        session.rollback()
        print("Exception:", e)
        return None
    finally:
        session.close()
    return user


# ------------------ UPDATE ------------------
def update_user(person_id: int, name: str = None, email: str = None):
    try:
        session = SessionLocal()
        user = session.query(Users).filter(Users.id == person_id).first()
        if not user:
            return None
        if name:
            user.name = name
        if email:
            user.email = email
        session.commit()
        session.refresh(user)
    except Exception as e:
        session.rollback()
        print("Exception:", e)
        return None
    finally:
        session.close()
    return user


# ------------------ DELETE ------------------
def delete_user(person_id: int):
    try:
        session = SessionLocal()
        user = session.query(Users).filter(Users.id == person_id).first()
        if not user:
            return None
        session.delete(user)
        session.commit()
    except Exception as e:
        session.rollback()
        print("Exception:", e)
        return None
    finally:
        session.close()
    return user


# ------------------ MAIN ------------------
if __name__ == "__main__":
    print("Creating tables in MySQL DB.......")
    Base.metadata.create_all(bind=engine)
    print("Table creation completed")

    # Create users
    create_user('Stefan', 'stefan@gmail.com')
    create_user('Rebacca', 'rebacca@gmail.com')
    create_user('Caroline', 'caroline@gmail.com')
    create_user('damon', 'damon@gmail.com')
    create_user('Klaus', 'klaus@gmail.com')

    # Read all users
    user = get_all_users()
    print("All Users:")
    for u in user:
        print(u)

    # Read by ID
    person = get_user_by_id(1)
    print("Person with ID=1:", person)

    # Update user
    updated = update_user(2, name="Rebacca", email="rebacca@gmail.com")
    print("Updated Person:", updated)

    # Delete user
    deleted = delete_user(4)
    print("Deleted Person:", deleted)


# o/p:
# 1.
# User created: User(id=1, name='Stefan', email='stefan@gmail.com')

# 2.
# Updated: User(id=2, name='Rebacca', email='rebacca@gmail.com')
# User(id=2, name='Rebacca', email='rebacca@gmail.com')

# 3.
# Deleted: User(id=4, name='damon', email='damon@gmail.com')
# User(id=4, name='damon', email='damon@gmail.com')

# 4.
# User(id=1, name='Stefan', email='stefan@gmail.com')
# User(id=2, name='Rebacca', email='rebacca@gmail.com')
# User(id=3, name='Caroline', email='caroline@gmail.com')
# User(id=5, name='Klaus', email='klaus@gmail.com')

# 5.
# Person not found
# None