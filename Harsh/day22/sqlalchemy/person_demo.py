from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URL = "mysql+pymysql://root:pass%40word1@localhost:3306/ust_db"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)

Base = declarative_base()

class Person(Base):
    __tablename__ = "persons"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50))
    email = Column(String(100), unique=True, nullable=False)

print("Creating table...")
Base.metadata.create_all(bind=engine)
print("Table created")

def create_person(name: str, email: str):
    try:
        session = SessionLocal()
        new_person = Person(name=name, email=email)
        session.add(new_person)
        session.commit()
        session.refresh(new_person)
        return new_person
    except Exception as e:
        print("Error:", e)
        return None
    finally:
        session.close()
        
def get_all_persons():
    try:
        session=SessionLocal()
        persons=session.query(Person).all()
    except Exception as e:
        print("Error",e)
    finally:
        session.close()
    return persons


def get_by_id(id:int):
    try:
        session=SessionLocal()
        person_by_id=session.query(Person).filter(Person.id==id).first()
    except Exception as e:
        print("Error",e)
    finally:
        session.close()
    return person_by_id

def delete_by_id(id: int):
    try:
        session = SessionLocal()
        person_by_id = session.query(Person).filter(Person.id == id).first()
        if not person_by_id:
            print(f"No Person found with ID:{id}")
            return None
        session.delete(person_by_id)
        session.commit()
        print(f"Deleted Person with ID:{id}")
            
    except Exception as e:
        print("Error:", e)
    finally:
        session.close()
        
def update_person(id: int, new_name: str = None, new_email: str = None):
    try:
        session = SessionLocal()
        person = session.query(Person).filter(Person.id == id).first()
        if not person:
            print(f"No Person found with ID:{id}")
            return None

        person.name = new_name
        person.email = new_email
        session.commit()
        session.refresh(person)
        print(f"Updated Person with ID:{id}, Name:{person.name}, Email:{person.email}")
        return person
    except Exception as e:
        print("Error:", e)
        return None
    finally:
        session.close()



if __name__ == "__main__":
    persons = [
        ("Amit Sharma", "amit.sharma@ust.com"),
        ("Priya Verma", "priya.verma@ust.com"),
        ("Ravi Kumar", "ravi.kumar@ust.com"),
        ("Sneha Patel", "sneha.patel@ust.com"),
        ("Harsh Jaiswal","harsh.jaiswal@ust.com")
    ]
    
    # for name, email in persons:
    #     new_person = create_person(name, email)
    #     print(f"Person Added with ID:{new_person.id}, Name:{new_person.name}, Email:{new_person.email}")
    
    
    all_persons = get_all_persons()
    print("\n")
    for persons in all_persons :
        print(f"ID:{persons.id}, Name:{persons.name}, Email:{persons.email}")
    
    print("\n")
    person_by_id=get_by_id(5)
    print(f"ID:{person_by_id.id},Name:{person_by_id.name},Email:{person_by_id.email}")
    
    # delete_person=delete_by_id(4)
    # print(f"Person Deleted ")
    
    update_person(2, new_name="Priya Singh", new_email="priya.singh@ust.com")
    
