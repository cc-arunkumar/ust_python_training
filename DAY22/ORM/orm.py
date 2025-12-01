from sqlalchemy import create_engine,Column,String,Integer
from sqlalchemy.orm import sessionmaker, declarative_base

# DATABASE_URL= "mysql+pymysql://root:Pass@word1@localhost:3306/ust_db"
DATABASE_URL = "mysql+pymysql://root:pass%40word1@localhost:3306/ust_db"

engine=create_engine(DATABASE_URL,echo=False)
SessionLocal=sessionmaker(bind=engine,autoflush=False,autocommit=False)

Base=declarative_base()

class Person(Base):
    __tablename__='persons'
    
    id=Column(Integer,primary_key=True,index=True)
    name=Column(String(50))
    email=Column(String(100), unique=True,nullable=False)
    
    def __repr__(self):
        return f"User (id={self.id}, name='{self.name}', email='{self.email}')"

print("Creaing tables")
Base.metadata.create_all(bind=engine)
print("Table Created")

def create_usert(name:str, email:str):
    try:
        session=SessionLocal()
        new_person=Person(name=name,email=email)
        session.add(new_person)
        session.commit()
        session.refresh(new_person)
    
    except Exception as e:
        session.rollback()
        print("Exception :",e)
        return None
    
    finally:
        session.close()
    return new_person


def get_all_users():
    session=SessionLocal()
    persons=session.query(Person).all()
    for user in persons:
        print(f"User id : {user.id} | User name: {user.name} | User Email : {user.email}")
        print("")
    session.close()
    # return persons

def get_person_by_id(person_id:int):
    session=SessionLocal()
    person=session.query(Person).filter(Person.id==person_id).first()
    session.close()
    return person    


def update_person(person_id: int, email: str):
    session = SessionLocal()
    try:
        person=session.query(Person).filter(Person.id == person_id).first()
        
        if person is None:
            print("Person not Found")
            return None
        
        person.email=email
        session.commit()
        session.refresh(person)
        return person
    
    except Exception as e:
        session.rollback()
        print("Exception:", e)
        return None
    
    finally:
        session.close()


def delete_person(person_id:int):
    session=SessionLocal()
    person=session.query(Person).filter(Person.id==person_id).first()
    
    if person is None:
        print("Person nor Found")
        session.close()
        return None
    
    session.delete(person)
    session.commit()
    session.close()
    return person
    
print(get_person_by_id(3))









# new_per1=create_usert("Gowtham","gowtham10ja@gmail.com")
# new_per2=create_usert("Vijay","Vijay@gmail.com")
# new_per3=create_usert("DK","Dinesh@gmail.com")
# new_per4=create_usert("Vikra","vikram@gmail.com")

# print("Person added :",new_per1)
# print("Person added :",new_per2)
# print("Person added :",new_per3)
# print("Person added :",new_per4)

# print(get_all_users())
# get_all_users()