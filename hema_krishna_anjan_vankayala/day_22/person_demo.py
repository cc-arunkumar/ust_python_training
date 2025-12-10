from sqlalchemy import create_engine,Column,Integer,String
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASEURL = "mysql+pymysql://root:password123@localhost:3306/ust_db"
engine = create_engine(DATABASEURL,echo=True)
SessionLocal = sessionmaker(bind=engine,autoflush=False,autocommit=False)

Base = declarative_base()

class Person(Base):
    __tablename__ = 'persons'
    id = Column(Integer,primary_key=True, index=True)
    name = Column(String(50))
    email = Column(String(100),unique=True,nullable=False)
    
    def __repr__(self):
        return f'User(id = {self.id}, name = {self.name}, email = {self.email})'
    
# print("Creating table in MYSQL DB..")
Base.metadata.create_all(bind=engine)
# print("Table creation completed")


#CRUD OPERATIONS
def create_user(name:str,email:str):
    try:
        #1.Create session
        session = SessionLocal()
        #Create User
        new_person = Person(name=name,email=email)
        #Add User in Session
        session.add(new_person)
        #Commit Session
        session.commit()
        #Refresh Session
        session.refresh(new_person)
        
    except Exception as e:
        session.rollback()
        print("Exception:",e)
    
    finally:
        #Close Session
        session.close()
    
    return new_person

def get_all_users():
    try:
        #create Session
        session = SessionLocal()
        #Execute Query to get all the Users
        persons = session.query(Person).all()
        #Returns the List
        return persons
        
    except Exception as e:

        session.rollback()
        print("Error:",e)
        
    finally:
        session.close()

def get_person_by_id(person_id : int):
    
    session  = SessionLocal()
    
    person = session.query(Person).filter(Person.id == person_id).all()
    
    session.close()
    
    return person
    
def update_by_id(id: int, updated_person : Person):
    try:
        session = SessionLocal()
        person = session.query(Person).filter(Person.id == id).first()

        if person is None:
            print("Person is Not Found!")
            session.close()
            return None
        
        person.email = updated_person.email 
        session.commit()
        session.refresh(person)
    except Exception as e:

        session.rollback()
        print("Error:",e)
    
    finally:
        session.close()
        
def delete_by_id(person_id:int):
    try:
        session = SessionLocal()
        person = session.query(Person).filter(Person.id == person_id ).first()
        
        if person is None:
            print("Person is Not Found!")
            return None 
        
        session.delete(person)
        session.commit()
        return True
        
    except Exception as e:
        session.rollback()
        print("Error:",e)

    finally:
        session.close()
    


if __name__== "__main__":
    data=delete_by_id(5)
    if data:
        print("Deleted Succesfully!")
