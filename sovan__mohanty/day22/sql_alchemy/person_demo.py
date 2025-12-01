from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, declarative_base

# Correct driver string: mysql+pymysql
DATABASE_URL = "mysql+pymysql://root:pass%40word1@localhost:3306/ust_db"

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
print(create_user("Sovan","sovan@gmail.com"))
print(create_user("Raj","raj@gmail.com"))
print(create_user("shiva","shiv@gmail.com"))
def get_all_users():
    try:
        session=SessionLocal()
        persons=session.query(Person).all()
    except Exception as e:
        session.rollback()
        print("Exception:",e)
        return None
    finally:
        session.close()
    return persons
print(get_all_users())

def get_person_by_id(person_id:int):
    try:
        session=SessionLocal()
        person=session.query(Person).filter(Person.id==person_id).first()
    except Exception as e:
        session.rollback()
        print("Exception:",e)
        return None
    finally:
        session.close()
    return person
print(get_person_by_id)

def update_by_id(person_id:int,person_email:str):
    session=SessionLocal()
    person=session.query(Person).filter(Person.id==person_id).first()
    if person is None:
        print("Person not found")
        session.close()
        return None
    person.email=person_email
    session.commit()
    session.close()
    return person
print(update_by_id(1,"msovan@gmail.com"))

def delete_person(person_id:int):
    session=SessionLocal()
    person=session.query(Person).filter(Person.id==person_id).first()
    if person is None:
        print("Person not found !")
        session.close()
        return None
    session.delete(person)
    session.commit()
    session.close()
    return person
print(delete_person(1))