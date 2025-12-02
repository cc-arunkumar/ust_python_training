from sqlalchemy import create_engine,Column,Integer,String
from sqlalchemy.orm import sessionmaker,declarative_base

DATABASE_URL = "mysql+pymysql://root:felix_123@localhost:3306/ust_db"

engine = create_engine(DATABASE_URL,echo=True)

SessionLocal = sessionmaker(bind=engine,autoflush=False,autocommit=False)

Base = declarative_base()
class Person(Base):
    __tablename__ = "person"
    
    id = Column(Integer,primary_key=True,index=True)
    name = Column(String(50))
    email = Column(String(100),unique=True,nullable=False)
    
    def __repr__(self):
        return f"User_id = {self.id}, name = {self.name}' email = {self.email}"

print("Creating tables in mysql DB...")
Base.metadata.create_all(bind=engine)
print("Table creation completed")

def create_person(name:str , email:str):
    try:
        session = SessionLocal()
        
        new_person = Person(name=name, email=email)
        
        session.add(new_person)
        
        session.commit()
        
        session.refresh(new_person)
    except Exception as e:
        session.rollback()
        print("ERROR: ,",e)
        return None
    finally:
        print("Completed")
    session.close()
    return new_person

# create_person("Felix","felix@ust.com")
# create_person("Akhil","akhil@ust.com")
# create_person("Arjun","arjun@ust.com")
# create_person("Arun","arun@ust.com")

def get_all_persons():
    try:
        session = SessionLocal()
        
        persons = session.query(Person).all()
        
        session.close()
        
        
        for person in persons:
            # print(person.)
            print(f"ID: {person.id} | Name: {person.name} | Email: {person.email}")
    except Exception as e:
        print("ERROR: ",e)
    finally:
        print("Completed")
        
def get_person_by_id(person_id:int):
    try:
        session = SessionLocal()
        
        person = session.query(Person).filter(Person.id == person_id).first()
        
        print(f"ID: {person.id} | Name: {person.name} | Email: {person.email}")
        
        session.close()
    except Exception as e:
        print("ERROR: ",e)
    finally:
        print("Completed")
        
def update_person_by_id(person_id,new_email):
    try:
        session = SessionLocal()
        
        person = session.query(Person).filter(Person.id == person_id).first()
        
        if person is None:
            print("Person not found")
            session.close()
            return None
        person.email = new_email
        session.commit()
        session.refresh(person)
        
        print(f"Updated -> ID: {person.id} | Name: {person.name} | Email: {person.email}")
        
        session.close()
    except Exception as e:
        print("ERROR: ",e)
    finally:
        print("Completed")
        
def delete_person_by_id(person_id):
    try:
        session = SessionLocal()
        
        person = session.query(Person).filter(Person.id == person_id).first()
        
        if person is None:
            print("Person not found")
            session.close()
            return None
                
        
        session.delete(person)
        session.commit()
        session.close()
        print("Person deleted")
    except Exception as e:
        print("ERROR: ",e)
    finally:
        print("Completed")
        
        
        
if __name__ =="__main__":
    # get_all_persons()
    # get_person_by_id(1)
    # update_person_by_id(1,"felix@ust.com")
    delete_person_by_id(1)
    