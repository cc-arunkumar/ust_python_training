from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, declarative_base

# Correct DATABASE_URL
DATABASE_URL = "mysql+pymysql://root:1234@localhost:3306/ust_db"

# Create the engine
engine = create_engine(DATABASE_URL, echo=True)

# Session local for managing the DB session
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)

# Base class for model definitions
Base = declarative_base()

# Define the Person model
class Person(Base):
    __tablename__ = 'persons'
    
    id = Column(Integer, primary_key=True, index=True)  # Corrected `column` to `Column`
    name = Column(String(50))
    email = Column(String(100), unique=True, nullable=False)
    
    def __repr__(self):
        return f"User(id={self.id}, name='{self.name}', email='{self.email}')"
    
print("Creating tables in MySQL DB......")

# Create tables
Base.metadata.create_all(bind=engine)

print("Table creation completed")


def create_user(name: str, email: str):
    try:
        session = SessionLocal()  
        
        new_person = Person(name=name, email=email)
        
        session.add(new_person)
        
        session.commit()
        
        session.refresh(new_person)
        
    except Exception as e:
        session.rollback()
        
        print("Exception: ", e)  
        
        return None
    
    finally:
        session.close()
    
    return new_person 


def get_all_users():
    try:
        session = SessionLocal()
        
        persons = session.query(Person).all()
        
        return persons  
        
    except Exception as e:
        session.rollback()
        
        print("Exception: ", e)
        
        return None
    
    finally:
        session.close()


def get_person_by_id(person_id: int):
    try:
        session = SessionLocal()
        person = session.query(Person).filter(Person.id == person_id).first()
    except Exception as e:
        session.rollback()
        print("Exception: ", e)
        return None
    finally:
        session.close()
    
    return person


def update_by_id(id: int, updated_person: Person):
    try:
        session = SessionLocal()
        person = session.query(Person).filter(Person.id == id).first()
 
        if person is None:
            print("Person not found!")
            return None
       
        person.email = updated_person.email
        session.commit()
        session.refresh(person)
    except Exception as e:
        session.rollback()
        print("Error:", e)
   
    finally:
        session.close()


def delete_person(person_id: int):
    try:
        session = SessionLocal()
        person = session.query(Person).filter(Person.id == person_id).first()
    
        if person is None:
            print("Person not found!")
            return None 
        
        session.delete(person)
        session.commit()
    
    except Exception as e:
        session.rollback()
        print("Error:", e)
    
    finally:
        session.close()


if __name__ == "__main__":
    # Example usage:
    # Create user
    # create_user("John Doe", "john.doe@example.com")
    
    # Fetch all users
    data = get_all_users()
    print("All users:", data)
    
    # Fetch user by ID
    person_id = 1  
    user_by_id = get_person_by_id(person_id)
    print(f"\nUser with ID {person_id}: {user_by_id}")
    
    # Update user by ID
    updated_person = Person(name="Abhi", email="Abhi2334@gmail.com")
    update_by_id(person_id, updated_person)
    
    # Delete user by ID
    delete_person(person_id)