# Import required SQLAlchemy components
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, declarative_base


# ----------------------------
# DATABASE CONFIGURATION
# ----------------------------

# MySQL database connection string
DATABASE_URL = "mysql+pymysql://root:1234@localhost:3306/ust_db"

# Create SQLAlchemy engine (echo=True shows SQL logs)
engine = create_engine(DATABASE_URL, echo=True)

# Session factory for handling database transactions
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)

# Base class for all ORM models
Base = declarative_base()


# ----------------------------
# ORM MODEL - USER TABLE
# ----------------------------

class User(Base):
    """
    ORM model representing the 'users' table in the database.
    """
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50))
    email = Column(String(100), unique=True, nullable=True)

    def __repr__(self):
        # String representation for easy debugging
        return f"User(id={self.id} | name={self.name} | email={self.email})"


# Create tables in the database
print("Creating tables in MySQL DB...")
Base.metadata.create_all(bind=engine)
print("Table creation completed")


# ----------------------------
# CRUD OPERATIONS
# ----------------------------

def create_user(name: str, email: str):
    """
    Create a new user and save it to the database.
    """
    try:
        session = SessionLocal()

        new_user = User(name=name, email=email)

        # Add and commit transaction
        session.add(new_user)
        session.commit()

        # Refresh to load generated ID
        session.refresh(new_user)

    except Exception as e:
        session.rollback()
        print("Exception:", e)
        return None

    finally:
        session.close()

    print(f"Name: {new_user.name} | Email: {new_user.email}")
    return new_user


def get_all_users():
    """
    Fetch all users from the database.
    """
    try:
        session = SessionLocal()
        users = session.query(User).all()
        return users

    except Exception as e:
        session.rollback()
        print("Exception", e)
        return None

    finally:
        session.close()


def get_person_by_id(user_id: int):
    """
    Fetch a single user by their ID.
    """
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


def update_user_by_id(user_id: int, new_email: str):
    """
    Update a user's email using their ID.
    """
    session = SessionLocal()

    user = session.query(User).filter(User.id == user_id).first()

    if user is None:
        print("User not found")
        session.close()
        return None

    # Update field
    user.email = new_email
    session.commit()
    session.close()

    return user


def delete_user_by_id(user_id: int):
    """
    Delete a user record using the ID.
    """
    session = SessionLocal()

    user = session.query(User).filter(User.id == user_id).first()

    if user is None:
        print("Person not found")
        session.close()
        return None

    session.delete(user)
    session.commit()
    session.close()

    return user


# ----------------------------
# MAIN EXECUTION
# ----------------------------

if __name__ == "__main__":

    # Example: Create a user
    # create_user("abhi", "abhi@gmail.com")

    # Example: Fetch all users
    # persons = get_all_users()
    # for p in persons:
    #     print(p)

    # Example: Update email
    # update_user_by_id(2, "niranjan123@gmail.com")

    # Example: Delete a user
    delete_user_by_id(3)

    # Example: Fetch user by ID
    # print(get_person_by_id(1))
