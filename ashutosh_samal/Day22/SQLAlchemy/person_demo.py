from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, declarative_base

# Correct driver string: mysql+pymysql
DATABASE_URL = "mysql+pymysql://root:pass1word@localhost:3306/ust_db"

# Create engine
engine = create_engine(DATABASE_URL, echo=True)

# Session factory
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)

# Base class for models
Base = declarative_base()

# Model definition
class Person(Base):
    __tablename__ = "persons"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String(50), nullable=False)
    email = Column(String(100), unique=True, nullable=False)

    def __repr__(self):
        return f"User(id={self.id}, name='{self.name}', email='{self.email}')"

# Create tables
print("Creating tables in MySQL DB...")
Base.metadata.create_all(bind=engine)
print("Table creation completed")

def create_user(name:str,email:str):
    try:
        #Create session
        session=SessionLocal()
        
        #Create user
        new_person=Person(name=name,email=email)
        #add user to session
        session.add(new_person)
        
        #Commit session
        session.commit()
        
        #Refresh session
        session.refresh(new_person)
    except Exception as e:
        session.rollback()
        print("Exception:",e)
        return None
    finally:
        session.close()
    return new_person
print(create_user("Ashutosh","ashu@gmail.com"))
print(create_user("Raj","raj@gmail.com"))
print(create_user("shiva","shiv@gmail.com"))


# Function to get all person records from the database
def get_all_users():
    try:
        session = SessionLocal()  # Create a database session
        persons = session.query(Person).all()  # Fetch all records from Person table
    except Exception as e:
        session.rollback()  # Rollback if error occurs
        print("Exception:", e)
        return None
    finally:
        session.close()  # Close DB session in all cases
    return persons  # Return fetched list of persons

print(get_all_users())  # Calling the function and printing results


# Function to fetch a single person using their ID
def get_person_by_id(person_id: int):
    try:
        session = SessionLocal()  # Create DB session
        person = session.query(Person).filter(Person.id == person_id).first()  # Query person by ID
    except Exception as e:
        session.rollback()  # Rollback if error occurs
        print("Exception:", e)
        return None
    finally:
        session.close()  # Close session
    return person  # Return the Person object (or None if not found)

print(get_person_by_id)  # Prints function reference (not calling) — optional


# Function to update a person's email using their ID
def update_by_id(person_id: int, person_email: str):
    session = SessionLocal()  # Create DB session
    person = session.query(Person).filter(Person.id == person_id).first()  # Find the record

    if person is None:
        print("Person not found")  # If no match found
        session.close()
        return None

    person.email = person_email  # Update email field
    session.commit()  # Save changes to DB
    session.close()  # Close session
    return person  # Return updated person object

print(update_by_id(1, "ashutosh@gmail.com"))  # Example function call


# Function to delete a person using their ID
def delete_person(person_id: int):
    session = SessionLocal()  # Create DB session
    person = session.query(Person).filter(Person.id == person_id).first()  # Find record

    if person is None:
        print("Person not found !")
        session.close()
        return None

    session.delete(person)  # Delete the record
    session.commit()  # Save changes
    session.close()  # Close session
    return person  # Return deleted person object


print(delete_person(1))  # Example delete call
