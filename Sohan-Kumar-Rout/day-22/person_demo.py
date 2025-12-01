from sqlalchemy import create_engine,Column,Integer,String

from sqlalchemy.orm import sessionmaker,declarative_base

DATABASE_URL="mysql+pymysql://root:pass%40word1@localhost:3306/ust_asset_db"

engine = create_engine(DATABASE_URL,echo=True)

SessionLocal= sessionmaker(bind=engine,autoflush=False,autocommit=False)

Base = declarative_base()

class Person(Base):
    __tablename__="persons"
    
    id = Column(Integer,primary_key=True,nullable=False)
    name = Column(String(50))
    email= Column(String(100),unique=True,nullable=False)
    
    def __repr__(self):
        return f"User(id = {self.id} , name = : {self.name} , email : {self.email})"
    
print("Table is creating ....")
Base.metadata.create_all(bind=engine)
print("Table is created")


def create_user(name = str , email=str):
    try:
        session=SessionLocal()
        
        new_person = Person(name= name, email=email)
        
        session.add(new_person)
        
        session.commit()
        
        session.refresh(new_person)
        
    except Exception as e:
        session.rollback()
        print("Exception",e)
        return None
    finally:
        session.close()
        
    return new_person
print("creating user")
print(create_user("Sohan", "sohan@gmail.com"))
create_user("Pihoo Mishra", "pihoo@gmail.com")
create_user("Itishree", "itishree@gmail.com")
create_user("Ayan", "ayna@gmail.com")
print("Created user",)

def get_all_users():
    try:
        session = SessionLocal()
        persons= session.query(Person).all()
        session.close()
        return persons
    except Exception as e:
        print("Exception occured",e)
        return None
    
    finally:
        session.close()
        
print(get_all_users())

def get_person_by_id(person_id:int):
    try:
        session=SessionLocal()
        person= session.query(Person).filter(Person.id==person_id).first()
        session.close()
    except Exception as e:
        print("Exception ",e)
        return None
    
    finally:
        session.close()
    return person
print("Employee with of specific id : ",get_person_by_id(2))


def update_by_id(person_id=int, new_email=str):
    session=SessionLocal()
    person=session.query(Person).filter(Person.id==person_id).first()
    
    if person is None:
        print("User not found")
        session.close()
        return None
    
    session.delete(person)
    session.commit()
    session.close()
    return person

print(update_by_id(2,"sovan@gmail.com"))
print(get_all_users())
    
def delete_by_id(person_id=int):
    session=SessionLocal()
    person=session.query(Person).filter(Person.id==person_id).first()
    
    if person is None:
        print("User not found")
        session.close()
        return None
    
    session.delete(person)
    session.commit()
    session.close()
    return person
print(delete_by_id(2))
print(get_all_users())


