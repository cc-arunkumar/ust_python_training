from sqlalchemy import create_engine,Integer,String,Column
from sqlalchemy.orm import sessionmaker,declarative_base

database_url = "mysql+pymysql://root:pass%40word1@localhost:3306/ust_db"

engine=create_engine(database_url,echo=True)
SessionLocal=sessionmaker(bind=engine,autoflush=False,autocommit=False)


Base= declarative_base()
class Person(Base):
    __tablename__="persons"
    
    id=Column(Integer,primary_key=True,index=True)
    name=Column(String(50))
    email=Column(String(50),unique=True,nullable=False)
    
    def __repr__(self):
        return f"User(id={self.id},name={self.name},email={self.email})"
    
print("creating tables")
Base.metadata.create_all(bind=engine)
print("table created ")


def create_person(name:str,email:str):
    try:
        session=SessionLocal()
        new_person=Person(name=name,email=email)
        session.add(new_person)
        session.commit()
        session.refresh(new_person)
        
    except Exception as e:
        session.rollback()
        print(e)
        return None
    finally:
        session.close()
    return new_person


# create_person("arumuekh","arum@gmsul.com")
    
# create_person("dadsa","asdasd@gmail")

def get_all():
    try:
        session=SessionLocal()
        persons=session.query(Person).all()
        # session.close()
        return persons 
    except Exception as e:
        session.rollback()
        print(e)
        return None
    finally:
        session.close()
        
def get_person_by_id(id:int):
    session=SessionLocal()
    person=session.query(Person).filter(Person.id==id).first()
    session.close()
    return person

def update_person(id:int,new_email:str):
    session=SessionLocal()
    person=session.query(Person).filter(Person.id==id).first()
    if person is None:
        print("person not found")
        session.close()
        return None
    person.email=new_email
    session.commit()
    session.refresh(person)
    
def delete_person(id:int):
    session=SessionLocal()
    person=session.query(Person).filter(Person.id==id).first()
    if person is None:
        print("person not found")
        session.close()
        return None
    session.delete(person)
# # print(get_all())
# print(get_person_by_id(1))
# print(create_person("akash","jsfvbhsjdfhyb"))
update_person(1,"aaaaaaa")
print(get_person_by_id(1))
print(delete_person(1))
