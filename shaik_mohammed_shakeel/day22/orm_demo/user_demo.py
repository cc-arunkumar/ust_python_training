# Importing necessary modules from SQLAlchemy
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, declarative_base

# Database URL for connecting to MySQL (make sure MySQL is running on localhost:3306)
DATABASE_URL = "mysql+pymysql://root:1234@localhost:3306/ust_db"

# Creating the engine that will manage database connections
engine = create_engine(DATABASE_URL, echo=True)

# SessionLocal is a factory to create session objects that interact with the database
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)

# Base class used to define the ORM models
Base = declarative_base()

# Defining the User class which will represent the 'users' table in the database
class User(Base):
    __tablename__ = 'users'  # Table name in the database

    # Columns in the 'users' table
    id = Column(Integer, primary_key=True, index=True)  # Primary key for the User
    name = Column(String(50))  # Name of the user
    email = Column(String(100), unique=True, nullable=False)  # Email of the user (unique and not null)

    # Representation method for the User object (useful for debugging and printing)
    def __repr__(self):
        return f"User(id={self.id}, name='{self.name}', email='{self.email}')"

# Creating the 'users' table in MySQL database
print("Creating tables in MySQL DB......")
Base.metadata.create_all(bind=engine)  # Creates all the tables in the database based on the model
print("Table creation completed")

# Function to create a new user in the 'users' table
def create_user(name: str, email: str):
    try:
        session = SessionLocal()  # Start a new session
        new_user = User(name=name, email=email)  # Create a new User object
        session.add(new_user)  # Add the user to the session
        session.commit()  # Commit the transaction to save the user in the DB
        session.refresh(new_user)  # Refresh the new user object to get the updated data (e.g., id)
    except Exception as e:
        session.rollback()  # If there's an error, roll back the transaction to maintain DB integrity
        print("Exception: ", e)  # Print the error message
        return None
    finally:
        session.close()  # Always close the session, even if there's an error
    return new_user  # Return the created user object

# Function to fetch all users from the 'users' table
def get_all_users():
    try:
        session = SessionLocal()  # Start a new session
        users = session.query(User).all()  # Query all users from the 'users' table
        return users  # Return the list of users
    except Exception as e:
        session.rollback()  # If there's an error, roll back the transaction
        print("Exception: ", e)  # Print the error message
        return None
    finally:
        session.close()  # Always close the session
    return users

# Function to fetch a user by their ID
def get_user_by_id(user_id: int):
    try:
        session = SessionLocal()  # Start a new session
        user = session.query(User).filter(User.id == user_id).first()  # Query a user by their ID
    except Exception as e:
        session.rollback()  # If there's an error, roll back the transaction
        print("Exception: ", e)  # Print the error message
        return None
    finally:
        session.close()  # Always close the session
    return user  # Return the user object if found, otherwise None

# Function to update a user's email by their ID
def update_user_by_id(id: int, updated_user: User):
    try:
        session = SessionLocal()  # Start a new session
        user = session.query(User).filter(User.id == id).first()  # Query the user by their ID
        if user is None:
            print("User not found!")  # If the user doesn't exist, print an error
            return None
        user.email = updated_user.email  # Update the user's email
        session.commit()  # Commit the changes to the database
        session.refresh(user)  # Refresh the user object to get the updated data
    except Exception as e:
        session.rollback()  # If there's an error, roll back the transaction
        print("Error:", e)  # Print the error message
    finally:
        session.close()  # Always close the session

# Function to delete a user by their ID
def delete_user(user_id: int):
    try:
        session = SessionLocal()  # Start a new session
        user = session.query(User).filter(User.id == user_id).first()  # Query the user by their ID
        if user is None:
            print("User not found!")  # If the user doesn't exist, print an error
            return None
        session.delete(user)  # Delete the user from the database
        session.commit()  # Commit the changes to the database
    except Exception as e:
        session.rollback()  # If there's an error, roll back the transaction
        print("Error:", e)  # Print the error message
    finally:
        session.close()  # Always close the session

# Main block for testing the CRUD functions
if __name__ == "__main__":
    # You can call the functions below to test their functionality

    # Create some users
    # create_user("Shakeel", "shakeel@gmial.com")
    # create_user("sai","sai@gmail.com")
    # create_user("abhi","abhi@gmail.com")

    # Fetch all users from the database
    # data = get_all_users()
    # print("All users:", data)

    # Fetch a user by their ID
    user_id = 3
    # user_by_id = get_user_by_id(user_id)
    # print(f"\nUser with ID {user_id}: {user_by_id}")

    # Update a user's email
    # updated_user = User(name="Shakeel", email="shakeel9051@gmial.com")
    # update_user_by_id(user_id, updated_user)

    # Delete a user by their ID
    delete_user(user_id)
