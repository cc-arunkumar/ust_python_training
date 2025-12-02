from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URL = "mysql+pymysql://root:pass%40word1@localhost:3306/ust_db"

engine = create_engine(DATABASE_URL, echo=True)
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)

Base  = declarative_base()

class Person(Base):
    __tablename__ = 'persons'
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50))
    email = Column(String(100), unique=True, nullable=True)
    
    def __repr__(self):
        return f"{self.id}, {self.name}, {self.email}"
    
print("Creating tables.")
Base.metadata.create_all(bind=engine)
print("Table ceaation completed.")

def create_user(name : str, email : str):
    try:
        session = SessionLocal()
        new_person = Person(name= name, email=email)
        session.add(new_person)
        session.commit()
        session.refresh(new_person)
    except Exception as e:
        session.rollback()
        print("Exception as : ", e)
        return None
    finally:
        session.close()
    
    return new_person

def get_all_persons():
    try:
        session = SessionLocal()
        persons = session.query(Person).all()
    except Exception as e:
        session.rollback()
        print("Exception as ", e)
        return None
    finally:
        session.close()
    return persons
       
def get_person_by_id(person_id : int):
    try:
        session = SessionLocal()
        person = session.query(Person).filter(Person.id == person_id).first()
    except Exception as e:
        session.rollback()
        print("Exception : ", e)
    finally:
        session.close()
    return person 

def update_person(person_id: int, new_email: str):
    try:
        session = SessionLocal()
        person = session.query(Person).filter(Person.id == person_id).first()
        if person is None:
            print("No person found.")
            return None
        
        person.email = new_email
        session.commit()
        session.refresh(person)
        return person
    except Exception as e:
        session.rollback()
        print("Exception in update_person:", e)
        return None
    finally:
        session.close()


def delete_person(person_id: int):
    try:
        session = SessionLocal()
        person = session.query(Person).filter(Person.id == person_id).first()
        if person is None:
            print("No person found.")
            return None
        
        session.delete(person)
        session.commit()
        return person
    except Exception as e:
        session.rollback()
        print("Exception in delete_person:", e)
        return None
    finally:
        session.close()

        
if __name__ == "__main__":
    updates = update_person(3, "rajeevkumar2002@gmail.com")
    print("Updated...")
    
    delete = delete_person(3)
    print("person deleted...")
    
    
    
