from sqlalchemy import create_engine,Column,Integer,String
from sqlalchemy.orm import sessionmaker,declarative_base

DATABASE_URL="mysql+pymysql://root:pass%40word1@localhost:3306/ust_db"
engine=create_engine(DATABASE_URL,echo=True)
SessionLocal=sessionmaker(bind=engine,autoflush=True,autocommit=False)

Base=declarative_base()

class Person(Base):
    __tablename__='persons'
    id=Column(Integer,primary_key=True,index=True)
    name=Column(String(50))
    email=Column(String(100),unique=True,nullable=False)
    
    def __repr__(self):
        return f"User(id={self.id},name={self.name},email={self.email})"


print("Creating tables in Mysql DB...")
Base.metadata.create_all(bind=engine)
print("Table creation complete")





def create_user(name:str,email:str):
    try:
        #1. create session
        session=SessionLocal()
        #2. create user
        new_person=Person(name=name,email=email)
        #3.Add user to session
        session.add(new_person)
        #4.commit session
        session.commit()
        #5.Refresh session
        session.refresh(new_person)
    except Exception as e:
        session.rollback()
        print("Exception",e)
        return None
    finally:
        #6.Close session
        session.close()
    
    return new_person




def get_all_users():
    try:
        session=SessionLocal()
        persons=session.query(Person).all()
        return persons    
    except Exception as e:
        session.rollback()
        print("Exception",e)
        return None
    finally:
        #6.Close session
        session.close()


def get_person_by_id(person_id:int):
    try:
        session=SessionLocal()
        person=session.query(Person).filter(Person.id==person_id).first()
        return person
    except Exception as e:
        session.rollback()
        print("Exception",e)
        return None
    finally:
        #6.Close session
        session.close()


def delete_person(person_id:int):
    try:
        session=SessionLocal()
        person=session.query(Person).filter(Person.id==person_id).first()
        
        if person is None:
            print("Person not found!")
            session.close()
            return None
        session.delete(person)
        session.commit()
        return person
    
    except Exception as e:
        session.rollback()
        print("Exception",e)
        return None
    finally:
        session.close()


def update_person(person_id:int,name:str,email:str):
    try:
        session=SessionLocal()
        person=session.query(Person).filter(Person.id==person_id).first()
        
        person.name=name
        person.email=email
        return person
    except Exception as e:
        session.rollback()
        print("Exception",e)
        return None
    finally:
        session.close()
        
        

#create_user("raji","raji@gmail.com")

b=get_all_users()
for row in b:
    print(f"ID is:{row.id},Name is {row.name}, Email is {row.email}")
print(get_person_by_id(1))














# create_engine: Creates an engine that connects to the database. 
# The engine is the starting point for any database interaction.

# Column, Integer, String: 
# These are used to define the columns in a database table, along with their types (integer, string, etc.).

# sessionmaker: 
# This is used to create a Session object. A session is the way to interact
# with the database for querying and updating records.

# declarative_base: 
# This is a factory function that creates a base class for your declarative class models 
# (i.e., the classes that represent your database tables)
