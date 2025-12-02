from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, declarative_base

# Database connection URL (MySQL with PyMySQL driver)
DATABASE_URL = 'mysql+pymysql://root:password1@localhost:3306/ust_db'

# Create engine (echo=True prints SQL statements executed)
engine = create_engine(DATABASE_URL, echo=True)

# Session factory for DB transactions
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)

# Base class for ORM models
Base = declarative_base()

# ORM model mapped to 'person' table
class Person(Base):
    __tablename__ = 'person'
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50))
    email = Column(String(100), unique=True, nullable=False)
    
    def __repr__(self):
        return f"User(id={self.id}, name='{self.name}', email='{self.email}')"


# Function to insert a new person
def create_person(name: str, email: str):
    session = SessionLocal()
    try:
        new_person = Person(name=name, email=email)
        session.add(new_person)
        session.commit()
        session.refresh(new_person)  # refresh to get auto-generated id
        print("User created:", new_person)
        return new_person
    except Exception as e:
        session.rollback()
        print("Exception:", e)
        return None
    finally:
        session.close()
        

# Function to update an existing person
def update_person(person_id: int, name: str = None, email: str = None):
    session = SessionLocal()
    try:
        person = session.query(Person).filter(Person.id == person_id).first()
        if person is None:
            print("Person not found")
            return None
        if name:
            person.name = name
        if email:
            person.email = email
        session.commit()
        session.refresh(person)
        print("Updated:", person)
        return person
    except Exception as e:
        session.rollback()
        print("Exception:", e)
        return None
    finally:
        session.close()


# Function to get all users
def get_all_users():
    session = SessionLocal()
    try:
        person = session.query(Person).all()
        return person
    except Exception as e:
        print("Exception:", e)
        return []
    finally:
        session.close()


# Function to get a user by ID
def get_user_by_id(person_id: int):
    session = SessionLocal()
    try:
        person = session.query(Person).filter(Person.id == person_id).first()
        return person
    except Exception as e:
        print("exception", e)
        return None
    finally:
        session.close()


# Function to delete a user
def delete_person(person_id: int):
    session = SessionLocal()
    try:
        person = session.query(Person).filter(Person.id == person_id).first()
        if person is None:
            print("Person not found")
            return None
        
        session.delete(person)
        session.commit()
        print("Deleted:", person)
        return person
    except Exception as e:
        session.rollback()
        print("Exception:", e)
        return None
    finally:
        session.close()


# Main execution block
if __name__ == "__main__":
    print("Creating table in MySQL DB...")
    Base.metadata.create_all(bind=engine)   # Creates table if not exists
    print("Table creation completed")

    # Insert sample users
    create_person('varsh', 'varsh@gmail.com')
    create_person("varsha", "vars@gmail")
    create_person("varsha", "v@gmail")
    create_person("tharun", "tharun@gmail")

    # Fetch all users
    users = get_all_users()
    for u in users:
        print(u)

    # Fetch user by ID
    user = get_user_by_id(1)
    print(user)

    # Delete user with ID=1
    deleted_user = delete_person(1)
    print(deleted_user)

    # Update user with ID=2
    updated_user = update_person(2, name="Varsha Updated", email="varsha_updated@gmail.com")
    print(updated_user)



# Creating table in MySQL DB...
# Table creation completed
# User created: User(id=1, name='varsh', email='varsh@gmail.com')
# User created: User(id=2, name='varsha', email='vars@gmail')
# User created: User(id=3, name='varsha', email='v@gmail')
# User created: User(id=4, name='tharun', email='tharun@gmail')

# # Printing all users
# User(id=1, name='varsh', email='varsh@gmail.com')
# User(id=2, name='varsha', email='vars@gmail')
# User(id=3, name='varsha', email='v@gmail')
# User(id=4, name='tharun', email='tharun@gmail')

# # Fetch user by ID=1
# User(id=1, name='varsh', email='varsh@gmail.com')

# # Delete user with ID=1
# Deleted: User(id=1, name='varsh', email='varsh@gmail.com')
# User(id=1, name='varsh', email='varsh@gmail.com')

# # Update user with ID=2
# Updated: User(id=2, name='Varsha Updated', email='varsha_updated@gmail.com')
# User(id=2, name='Varsha Updated', email='varsha_updated@gmail.com')
