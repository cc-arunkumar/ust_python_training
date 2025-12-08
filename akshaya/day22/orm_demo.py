from sqlalchemy import create_engine,Integer,String,Column
from sqlalchemy.orm import sessionmaker,declarative_base

DATABASE_URL= "mysql+pymysql://root:akshaya@localhost:3306/ust_db"
engine=create_engine(DATABASE_URL,echo=True)
SessionLocal=sessionmaker(bind=engine,autoflush=False,autocommit=False)

Base=declarative_base()

class Person(Base):
    __tablename__="persons"
    
    id=Column(Integer,primary_key=True,index=True)
    name=Column(String(50))
    email=Column(String(100),unique=True,nullable=False)
    
    def __repr__(self):
        return f"User(id={self.id},name='{self.name}',email='{self.email}')"

print("creating tables in mysql db...")
Base.metadata.create_all(bind=engine)
print("table creation completed")

def create_user(name:str,email:str):
    try:
        session=SessionLocal()
        new_person=Person(name=name,email=email)
        session.add(new_person)
        session.commit()
        session.refresh(new_person)
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
        print("Exception:",e)
        return None
    finally:
        session.close()
    return persons
    

# print(create_user("Akshhh","akshh@ust.com"))
# print(create_user("Katherine","kat@ust.com"))
# print(create_user("john","john@ust.com"))

# print(get_all_users())

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
    
# print(get_person_by_id(1))

def update(person_id:int,email:str):
    try:
        session=SessionLocal()
        persons=session.query(Person).filter(Person.id==person_id).first()
        if persons is None:
            print("person not found!")
        persons.email=email
        session.commit()
        print(persons)
    except Exception as e:
        session.rollback()
        print("Exception:",e)
    finally:
        session.close()
        
update(5,"kath@ust.com")
        
def delete(person_id:int):
    try:
        session=SessionLocal()
        person=session.query(Person).filter(Person.id==person_id).first()
        if person is None:
            print("person not found!")
            session.close()
        
        session.delete(person)
        session.commit()
        print("deleted")
    except Exception as e:
        session.rollback()
        print("Exception:",e)
    finally:
        session.close()
   
delete(6)       

