# Importing necessary components from SQLAlchemy
from sqlalchemy import create_engine, Integer, Column, String
from sqlalchemy.orm import sessionmaker, declarative_base

# Database URL for connecting to MySQL database
DATABASE_URL = "mysql+pymysql://root:1234@localhost:3306/ust_db"

# Creating the engine to connect to the database
engine = create_engine(DATABASE_URL, echo=True)

# SessionLocal is a factory for creating new session objects that connect to the DB
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)

# Base class for creating ORM models
Base = declarative_base()

# Defining the Person model as a table in the MySQL database
class Person(Base):
    __tablename__ = 'persons'  # Name of the table in the DB
    
    # Defining columns for the table with their respective types
    id = Column(Integer, primary_key=True, index=True)  # Auto-incrementing primary key
    name = Column(String(50))  # Name column with a max length of 50
    email = Column(String(100), unique=True, nullable=False)  # Email column (unique, cannot be null)
    
    def __repr__(self):
        return f"User(id='{self.id}', name='{self.name}', email='{self.email}')"

# Create all tables in the database based on the defined models (including 'Person')
print("Creating tables in MySQL DB")
Base.metadata.create_all(bind=engine)  # Binds the engine and creates tables
print("Table creation completed")

# Function to create a new user in the 'persons' table
def create_user(name: str, email: str):
    try:
        # Establishing a session to interact with the database
        session = SessionLocal()
        
        # Creating a new Person object with the provided name and email
        new_person = Person(name=name, email=email)
        
        # Adding the new Person object to the session
        session.add(new_person)
        
        # Committing the session to save changes to the DB
        session.commit()
        
        # Refreshing the new_person object to get the updated data (e.g., ID)
        session.refresh(new_person)
        
    except Exception as e:
        # If an error occurs, rolling back the transaction
        session.rollback()
        print("Exception: ", e)
        return None
    
    finally:
        # Closing the session to free up resources
        session.close()
        
    return new_person  # Returning the newly created user

# Main block to test the `create_user` function by creating some users
if __name__ == "__main__":
    create_user(name="Shakeel", email="sha@gmail.com")
    create_user(name="abhi", email="abc@gmail.com")
    create_user(name="Sai", email="def@gmail.com")
    create_user(name="vikas", email="ghi@gmail.com")

# Function to retrieve all users from the 'persons' table
def get_all_users():
    try:
        # Starting a session to interact with the DB
        session = SessionLocal()
        
        # Querying all persons from the database
        persons = session.query(Person).all()
        
    except Exception as e:
        # Rolling back in case of error
        session.rollback()
        print("Exception: ", e)
        return None
    finally:
        # Closing the session
        session.close()
    
    return persons  # Returning the list of all users

# Main block to test the `get_all_users` function and print the retrieved data
if __name__ == "__main__":
    data = get_all_users()
    print(data)

# Function to retrieve a specific person by their ID
def get_person_by_id(person_id: int):
    try:
        # Starting a session to interact with the DB
        session = SessionLocal()
        
        # Querying a person by their ID (only returns one result)
        person = session.query(Person).filter(Person.id == person_id).first()
        
    except Exception as e:
        # Rolling back in case of error
        session.rollback()
        print("Exception: ", e)
        return None
    finally:
        # Closing the session
        session.close()
    
    return person  # Returning the person object if found, otherwise None

# Main block to test the `get_person_by_id` function with an example ID (1)
if __name__ == "__main__":
    data = get_person_by_id(1)
    print(data)

# Function to update a person's details (in this case, updating email)
def update_by_id(id: int, updated_person: Person):
    try:
        # Starting a session to interact with the DB
        session = SessionLocal()
        
        # Querying the person by their ID
        person = session.query(Person).filter(Person.id == id).first()
        
        # If the person is not found, print an error and return
        if person is None:
            print("Person not found!")
            return None
        
        # Updating the person's email with the new email from updated_person
        person.email = updated_person.email
        
        # Committing the session to save the changes to the database
        session.commit()
        
        # Refreshing the person object to get the updated data
        session.refresh(person)
        
    except Exception as e:
        # Rolling back in case of error
        session.rollback()
        print("Error:", e)
    
    finally:
        # Closing the session
        session.close()

# Function to delete a person by their ID
def delete_person(person_id: int):
    try:
        # Starting a session to interact with the DB
        session = SessionLocal()
        
        # Querying the person by their ID
        person = session.query(Person).filter(Person.id == person_id).first()
        
        # If the person is not found, print an error and return
        if person is None:
            print("Person not found!")
            return None
        
        # Deleting the person from the database
        session.delete(person)
        
        # Committing the session to reflect the changes
        session.commit()
        
    except Exception as e:
        # Rolling back in case of error
        session.rollback()
        print("Error:", e)
    
    finally:
        # Closing the session
        session.close()
