# This script manages a MySQL database of users using SQLAlchemy. It defines functions to create, retrieve, and update users in the database. The User class represents the database table,
# and the script includes error handling to ensure smooth operations.

# Importing required modules from SQLAlchemy
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, declarative_base

# Database URL and connection setup
DATABASE_URL = "mysql+pymysql://root:bhargavi_123@localhost:3306/ust_db"
engine = create_engine(DATABASE_URL, echo=True)  # Creates the engine with connection string
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)  # Session setup for DB interaction

Base = declarative_base()  # Base class to create models from

# User class to represent the 'users' table in the database
class User(Base):
    __tablename__ = 'users'  # Table name set to 'users'
    id = Column(Integer, primary_key=True, index=True)  # Primary key column
    name = Column(String(50))  # Name column
    email = Column(String(100), unique=True, nullable=False)  # Email column, must be unique and cannot be NULL
    
    # Method to display the user object in a readable format
    def __repr__(self):
        return f"User(id={self.id}, name='{self.name}', email='{self.email}')"

# Creating tables if they don't exist already
print("Creating tables in MySQL DB...")
Base.metadata.create_all(bind=engine)  # Creates all tables mapped by the Base class
print("Table creation completed")

# Function to create a new user in the database
def create_user(name: str, email: str):
    try:
        session = SessionLocal()  # Open a new session
        new_user = User(name=name, email=email)  # Create a new User object
        session.add(new_user)  # Add the new user to the session
        session.commit()  # Commit the transaction to the database
        session.refresh(new_user)  # Refresh the object to get the updated data (e.g., id after insertion)
    except Exception as e:
        session.rollback()  # Rollback in case of error
        print("Exception:", e)  # Print error message
        return None
    finally:
        session.close()  # Always close the session after use
    return new_user  # Return the newly created user

# Function to get all users from the database
def get_all_users():
    try:
        session = SessionLocal()  # Open a new session
        users = session.query(User).all()  # Query all users
    except Exception as e:
        session.rollback()  # Rollback in case of error
        print("Exception:", e)  # Print error message
        return None
    finally:
        session.close()  # Always close the session
    return users  # Return the list of users

# Function to get a user by their ID
def get_user_by_id(user_id: int):
    try:
        session = SessionLocal()  # Open a new session
        user = session.query(User).filter(User.id == user_id).first()  # Query user by ID
        if user is None:
            print("User not found")  # Print message if user doesn't exist
            return None
    except Exception as e:
        print(f"Error occurred: {e}")  # Print error message
        return None
    finally:
        session.close()  # Always close the session
    return user  # Return the user object

# Function to update a user by their ID with new data
def update_user_by_id(user_id: int, new_data: dict):
    try:
        session = SessionLocal()  # Open a new session
        user = session.query(User).filter(User.id == user_id).first()  # Get user by ID

        if user is None:
            print("User not found")  # Print message if user doesn't exist
            return None

        # Update the user object with new data
        for key, value in new_data.items():
            setattr(user, key, value)

        session.commit()  # Commit the changes to the database
        print("User updated successfully")  # Print success message
        session.refresh(user)  # Refresh the object to reflect changes
        return user  # Return the updated user object
    except Exception as e:
        print(f"Error occurred: {e}")  # Print error message
        session.rollback()  # Rollback in case of error
    finally:
        session.close()  # Always close the session
    return None  # Return None if error occurs

# Main program execution
if __name__ == "__main__":
    # Create a new user
    new_user = create_user('Bhargavi', 'Bhargavi1@ust.com')
    if new_user:
        print(f"New user created ====> Name: {new_user.name}, Email: {new_user.email}")  # Print user details

    # Get and display all users
    users = get_all_users()
    if users:
        print("All Users:")
        for u in users:
            print(f" ====> Name: {u.name}, Email: {u.email}")  # Print details of each user

    # Update a user
    user_to_update = get_user_by_id(1)  # Fetch user with ID 1
    if user_to_update:
        updated_user = update_user_by_id(1, {'name': 'Bhargavi Updated', 'email': 'bhargavi.updated@ust.com'})
        if updated_user:
            print(f"Updated user ====> Name: {updated_user.name}, Email: {updated_user.email}")  # Print updated user details


#output
# Creating tables in MySQL DB...
# 2025-12-01 22:09:10,223 INFO sqlalchemy.engine.Engine SELECT DATABASE()
# 2025-12-01 22:09:10,224 INFO sqlalchemy.engine.Engine [raw sql] {}
# 2025-12-01 22:09:10,225 INFO sqlalchemy.engine.Engine SELECT @@sql_mode
# 2025-12-01 22:09:10,225 INFO sqlalchemy.engine.Engine [raw sql] {}
# 2025-12-01 22:09:10,226 INFO sqlalchemy.engine.Engine SELECT @@lower_case_table_names
# 2025-12-01 22:09:10,226 INFO sqlalchemy.engine.Engine [raw sql] {}
# 2025-12-01 22:09:10,230 INFO sqlalchemy.engine.Engine BEGIN (implicit)
# 2025-12-01 22:09:10,239 INFO sqlalchemy.engine.Engine DESCRIBE `ust_db`.`users`
# 2025-12-01 22:09:10,239 INFO sqlalchemy.engine.Engine [raw sql] {}
# 2025-12-01 22:09:10,244 INFO sqlalchemy.engine.Engine COMMIT
# Table creation completed
# 2025-12-01 22:09:10,246 INFO sqlalchemy.engine.Engine BEGIN (implicit)
# 2025-12-01 22:09:10,248 INFO sqlalchemy.engine.Engine INSERT INTO users (name, email) VALUES (%(name)s, %(email)s)
# 2025-12-01 22:09:10,248 INFO sqlalchemy.engine.Engine [generated in 0.00027s] {'name': 'Bhargavi', 'email': 'Bhargavi1@ust.com'}
# 2025-12-01 22:09:10,265 INFO sqlalchemy.engine.Engine COMMIT
# 2025-12-01 22:09:10,270 INFO sqlalchemy.engine.Engine BEGIN (implicit)
# 2025-12-01 22:09:10,273 INFO sqlalchemy.engine.Engine SELECT users.id, users.name, users.email 
# FROM users 
# WHERE users.id = %(pk_1)s
# 2025-12-01 22:09:10,273 INFO sqlalchemy.engine.Engine [generated in 0.00043s] {'pk_1': 2}
# 2025-12-01 22:09:10,274 INFO sqlalchemy.engine.Engine ROLLBACK
# New user created ====> Name: Bhargavi, Email: Bhargavi1@ust.com
# 2025-12-01 22:09:10,276 INFO sqlalchemy.engine.Engine BEGIN (implicit)
# 2025-12-01 22:09:10,277 INFO sqlalchemy.engine.Engine SELECT users.id AS users_id, users.name AS users_name, users.email AS users_email
# FROM users
# 2025-12-01 22:09:10,277 INFO sqlalchemy.engine.Engine [generated in 0.00067s] {}
# 2025-12-01 22:09:10,278 INFO sqlalchemy.engine.Engine ROLLBACK
# All Users:
#  ====> Name: Bhargavi Updated, Email: bhargavi.updated@ust.com
#  ====> Name: Bhargavi, Email: Bhargavi1@ust.com
# 2025-12-01 22:09:10,280 INFO sqlalchemy.engine.Engine BEGIN (implicit)
# 2025-12-01 22:09:10,282 INFO sqlalchemy.engine.Engine SELECT users.id AS users_id, users.name AS users_name, users.email AS users_email
# FROM users
# WHERE users.id = %(id_1)s
#  LIMIT %(param_1)s
# 2025-12-01 22:09:10,283 INFO sqlalchemy.engine.Engine [generated in 0.00172s] {'id_1': 1, 'param_1': 1}
# 2025-12-01 22:09:10,284 INFO sqlalchemy.engine.Engine ROLLBACK
# 2025-12-01 22:09:10,286 INFO sqlalchemy.engine.Engine BEGIN (implicit)
# 2025-12-01 22:09:10,286 INFO sqlalchemy.engine.Engine SELECT users.id AS users_id, users.name AS users_name, users.email AS users_email
# FROM users
# WHERE users.id = %(id_1)s
#  LIMIT %(param_1)s
# 2025-12-01 22:09:10,287 INFO sqlalchemy.engine.Engine [cached since 0.005618s ago] {'id_1': 1, 'param_1': 1}
# 2025-12-01 22:09:10,288 INFO sqlalchemy.engine.Engine COMMIT
# User updated successfully
# 2025-12-01 22:09:10,291 INFO sqlalchemy.engine.Engine BEGIN (implicit)
# 2025-12-01 22:09:10,293 INFO sqlalchemy.engine.Engine SELECT users.id, users.name, users.email
# FROM users
# WHERE users.id = %(pk_1)s
# 2025-12-01 22:09:10,296 INFO sqlalchemy.engine.Engine [cached since 0.02368s ago] {'pk_1': 1}
# 2025-12-01 22:09:10,298 INFO sqlalchemy.engine.Engine ROLLBACK
# Updated user ====> Name: Bhargavi Updated, Email: bhargavi.updated@ust.com