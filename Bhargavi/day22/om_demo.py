# This script interacts with a MySQL database using SQLAlchemy to manage a "persons" table. 
# It includes functions to create, retrieve, and update person records in the database. The Person model is defined with id, name, and email columns,
# and all operations are handled within a session with error handling and transaction management.


# Import necessary libraries from SQLAlchemy
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, declarative_base

# Database URL configuration (MySQL connection details)
DATABASE_URL = "mysql+pymysql://root:bhargavi_123@localhost:3306/ust_db"
# Create engine to connect to the database with SQLAlchemy
engine = create_engine(DATABASE_URL, echo=True)

# Session configuration for SQLAlchemy ORM
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)

# Declare the base class for the ORM models
Base = declarative_base()

# Define the Person model to interact with the 'persons' table in the database
class Person(Base):
    __tablename__ = 'persons'  # Table name in the database
    
    # Define the columns of the 'persons' table
    id = Column(Integer, primary_key=True, index=True)  # Primary key
    name = Column(String(50))  # Name of the person
    email = Column(String(100), unique=True, nullable=False)  # Unique email address
    
    # String representation of the Person instance
    def __repr__(self):
        return f"User(id={self.id}, name='{self.name}', email='{self.email}')"

# Create all tables defined using SQLAlchemy Base (i.e., creating 'persons' table)
print("Creating tables in MySQL DB...")
Base.metadata.create_all(bind=engine)
print("Table creation completed")

# Function to create a new person in the database
def create_person(name: str, email: str):
    try:
        session = SessionLocal()  # Open a session to interact with the database
        new_person = Person(name=name, email=email)  # Create a new Person object
        session.add(new_person)  # Add the new person to the session
        session.commit()  # Commit the transaction to the database
        session.refresh(new_person)  # Refresh the object with database values
    except Exception as e:
        session.rollback()  # Rollback the session if there's an error
        print("Exception:", e)
        return None
    finally:
        session.close()  # Close the session after the operation
    return new_person  # Return the newly created person object

# Function to fetch all persons from the 'persons' table
def get_all_users():
    try:
        session = SessionLocal()  # Open a session to interact with the database
        persons = session.query(Person).all()  # Query all Person objects
    except Exception as e:
        session.rollback()  # Rollback the session if there's an error
        print("Exception:", e)
        return None
    finally:
        session.close()  # Close the session after the operation
    return persons  # Return the list of Person objects

# Function to fetch a person by their ID
def get_person_by_id(person_id: int):
    try:
        session = SessionLocal()  # Open a session to interact with the database
        person = session.query(Person).filter(Person.id == person_id).first()  # Query a person by ID
        if person is None:
            print("Person not found")  # Print message if person does not exist
            return None
    except Exception as e:
        print(f"Error occurred: {e}")  # Print any exception that occurs
        return None
    finally:
        session.close()  # Close the session after the operation
    return person  # Return the fetched person object

# Function to update a person's details by their ID
def update_person_by_id(person_id: int, new_data: dict):
    try:
        session = SessionLocal()  # Open a session to interact with the database
        person = session.query(Person).filter(Person.id == person_id).first()  # Fetch the person by ID
        if person is None:
            print("Person not found")  # Print message if person does not exist
            return None
        # Loop through the new data dictionary and update the person's fields
        for key, value in new_data.items():
            setattr(person, key, value)  # Set new values for the person's attributes
        session.commit()  # Commit the changes to the database
        print("Person updated successfully")  # Print success message
        session.refresh(person)  # Refresh the object to sync with the database
    except Exception as e:
        print(f"Error occurred: {e}")  # Print any exception that occurs
        session.rollback()  # Rollback the session if there's an error
    finally:
        session.close()  # Close the session after the operation
    return person  # Return the updated person object

# Main block to execute the functions and test them
if __name__ == "__main__":

    # Create a new person named 'Bhargavi' with email 'Bhargavi1@ust.com'
    new_person = create_person('Bhargavi', 'Bhargavi1@ust.com')
    if new_person:
        print(f"New person created ====> Name: {new_person.name}, Email: {new_person.email}")

    # Fetch and display all persons from the database
    persons = get_all_users()
    if persons:
        print("All Persons:")
        for p in persons:
            print(f" ====> Name: {p.name}, Email: {p.email}")
    
    # Update a person's details with ID 1
    person_to_update = get_person_by_id(1)  # Fetch person with ID 1
    if person_to_update:
        updated_person = update_person_by_id(1, {'name': 'Bhargavi Updated', 'email': 'bhargavi.updated@ust.com'})
        if updated_person:
            print(f"Updated person ====> Name: {updated_person.name}, Email: {updated_person.email}")

#output
# Creating tables in MySQL DB...
# Table creation completed
# New person created ====> Name: Bhargavi, Email: Bhargavi1@ust.com
# All Persons:
# ====> Name: Bhargavi, Email: Bhargavi1@ust.com
# Updated person ====> Name: Bhargavi Updated, Email: bhargavi.updated@ust.com
