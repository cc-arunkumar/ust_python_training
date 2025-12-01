from sqlalchemy import create_engine,Column,Integer,String
from sqlalchemy.orm import sessionmaker,declarative_base

DATABASE_URL = "mysql+pymysql://root:password123@localhost:3306/ust_db"
engine = create_engine(DATABASE_URL,echo = True)
SessionLocal = sessionmaker(bind=engine,autoflush=False,autocommit = False)

Base = declarative_base()

class Person(Base):
    __tablename__ = "persons"
    
    id = Column(Integer, primary_key=True,index=True)
    name = Column(String(50))
    email = Column(String(100),unique=True,nullable=False)
    
    def __repr__(self):
        return f"Userid = {self.id},name = {self.name},email = {self.email}"
    
print("Creating tables in Mysql DB...")
Base.metadata.create_all(bind=engine)
print("Table creation completed")

def create_user(name:str,email:str):
    try:
        
        session = SessionLocal()
        new_person = Person(name = name,email =email)
        session.add(new_person)
        session.commit()
        session.refresh(new_person)
        
    except Exception as e:
        session.rollback()
        print("Exception: ",e)
        return None
    finally:
        session.close()
    return new_person.__dict__

def get_all():
    try:
        
        session = SessionLocal()
        persons = session.query(Person).all()
        for p in persons:
            print(p)
        return persons
    except Exception as e:
        session.rollback()
        print("Exception: ",e)
        return None
    finally:
        session.close()

def get_by_id():
    try:
        
        session = SessionLocal()
        person = session.query(Person).filter(Person.id==1).first()
        
        print(person)
        return person
    except Exception as e:
        session.rollback()
        print("Exception: ",e)
        return None
    finally:
        session.close()

def update_person(id:int,email:str):
    try:
        
        session = SessionLocal()
        person = session.query(Person).filter(Person.id==id).first()
        if not person:
            print("Person not found !")
            return None
        person.email = email
        session.commit()
        session.refresh(person)
        return person
    except Exception as e:
        session.rollback()
        print("Exception: ",e)
        return None
    finally:
        session.close()

def delete_person(id:int):
    try:
        
        session = SessionLocal()
        person = session.query(Person).filter(Person.id==id).first()
        if not person:
            print("Person not found !")
            return None
        session.delete(person)
        session.commit()
        return person
    except Exception as e:
        session.rollback()
        print("Exception: ",e)
        return None
    finally:
        session.close()

# get_all()
# get_by_id()
# update_person(5,"akhilpraveen12qwe3@gmail.com")
delete_person(5)