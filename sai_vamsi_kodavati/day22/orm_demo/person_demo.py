from sqlalchemy import create_engine,Column,Integer,String
from sqlalchemy.orm import sessionmaker,declarative_base

DATABASE_URL = "mysql+pymysql://root:12345@localhost:3306/ust_db"
engine = create_engine(DATABASE_URL,echo=True)
SessionLocal = sessionmaker(bind=engine,autoflush=False,autocommit = False)

Base = declarative_base()
class Person(Base):
    __tablename__ = "persons"
    
    id = Column(Integer,primary_key = True,index = True)
    name = Column(String(50))
    email = Column(String(100),unique=True,nullable = False)
    
    def __repr__(self):
        return f"User(id = {self.id},name = '{self.name}',email = '{self.email}')"
    
print("Creating tables in MySql DB...")
Base.metadata.create_all(bind=engine)
print("Table creation completed")



# def create_user(name:str,email:str):
#     try:
    
#         # Create Session
#         session = SessionLocal()
        
#         new_person= Person(name=name,email=email)
        
#         session.add(new_person)
        
#         session.commit()
        
#         session.refresh(new_person)
#     except Exception as e:
#         session.rollback()
#         print("Exception: ",e)
#         return None
    
#     finally:
#         session.close()
        
#     return new_person

# if __name__=="__main__":
#     create_user(name="Abhi",email="abhi@123")

# def get_all_users():
#     try:
        
#         session = SessionLocal()
        
#         persons = session.query(Person).all()
        
#     except Exception as e:
#         session.rollback()
#         print("Exception: ",e)
#     finally:
#         session.close()
#     return persons

# if __name__ == "__main__":
#     data = get_all_users()
#     print(data)

# def get_person_by_id(person_id:int):
#     try:
#         session = SessionLocal()
#         person = session.query(Person).filter(Person.id==person_id).first()
#     except Exception as e:
#         session.rollback()
#         print("Exception: ",e)
#     finally:
#         session.close()
#     return person

# if __name__ == "__main__":
#     data = get_person_by_id(1)
#     print(data)

def delete_person_by_id(person_id:int):

    session = SessionLocal()
    person = session.query(Person).filter(Person.id == person_id).first()
    
    if person is None:
        print("Person not found!")
        session.close()
        return None
    
    session.delete(person)
    session.commit()
    session.close()
    return person

if __name__ == "__main__":
    data= delete_person_by_id(9)
    print(data)
    
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

if __name__ == "__main__":
    data = update_by_id(9,"niranjan@123")
    print(data)