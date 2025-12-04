from sqlalchemy import create_engine,Column,Integer,String 
from sqlalchemy.orm import sessionmaker,declarative_base

DATABASE_URL="mysql+pymysql://root:raswanthi_1@localhost:3306/ust_db"
engine=create_engine(DATABASE_URL,echo=True)

SessionLocal=sessionmaker(bind=engine,autoflush=False,autocommit=False)

Base=declarative_base()
print(Base)

class Person(Base):
    __tablename__="persons"
    
    id=Column(Integer,primary_key=True,index=True)
    name=Column(String(50))
    email=Column(String(100),unique=True,nullable=False)
    
    def __repr__(self):
        return f"User(id={self.id}, name='{self.name}', email='{self.email}')"
    
print("Creating tables in MySQL DB...")
Base.metadata.create_all(bind=engine)
print("Table creation completed")

    
def create_user(name:str,email:str):
    try:
        session=SessionLocal()                    #1.create session
        new_person=Person(name=name,email=email)  #2.create object called new_person
        session.add(new_person)                   #3.adding object with session
        session.commit()                          #4.commit session
        session.refresh(new_person)               #5.refresh session
    except Exception as e:
        session.rollback()
        print("Exception:",e)
        return None 
    finally:
        session.close()
    return new_person.__dict__
        
        
def get_all_users():
    try:
        session=SessionLocal()
        persons=session.query(Person).all()
        
    except Exception as e:
        session.rollback()
        print("Exception",e)
        return None
    finally:
        session.close()
    return persons


def get_person_by_id(person_id:int):
    try:
        session=SessionLocal()
        person=session.query(Person).filter(Person.id==person_id).first()
    except Exception as e:
        session.rollback()
        print("Exception",e)
        return None
    finally:
        session.close()
    return person


def update_person(person_id:int,email:str):
    try:
        session=SessionLocal()
        person=session.query(Person).filter(Person.id==person_id).first()
        
        if person is None:
            print("Person not found !")
            return None 
        
        person.email=email
        session.commit()
        session.refresh(person)
        return person
    except Exception as e:
        session.rollback()
        print("Exception",e)
    finally:
        session.close()
    
    
    
def delete_person(person_id:int):
    try:
        session=SessionLocal()
        person=session.query(Person).filter(Person.id==person_id).first()
    
        if person is None:
            print("Person not found !")
            session.close()
            return None 
        session.delete(person)
        session.commit()
        print("deleted")
    except Exception as e:
        session.rollback()
        print("Exception",e)
    finally:
        session.close()
    return person
    
# print(create_user("Janat","janatsherin@example.com"))
# print(get_all_users())
# print(get_person_by_id(2))
# print(update_person(2,"aksh2@example.com"))
print(delete_person(4))
    
    
    