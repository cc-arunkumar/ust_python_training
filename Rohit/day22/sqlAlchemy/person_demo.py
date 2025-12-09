from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, declarative_base

Base = declarative_base()

class Person(Base):
    __tablename__ = "person"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)
    email = Column(String(100), unique=True, nullable=False)

DATABASE_URL = "mysql+pymysql://root:pass%40word1@localhost:3306/ust_db"
engine = create_engine(DATABASE_URL)
Base.metadata.create_all(engine)
SessionLocal = sessionmaker(bind=engine)

def create_person(name: str, email: str):
    session = SessionLocal()
    try:
        new_person = Person(name=name, email=email)
        session.add(new_person)
        session.commit()
        session.refresh(new_person)
        return new_person
    except Exception as e:
        session.rollback()
        print("Error:", e)
    finally:
        session.close()



def get_person_by_id(person_id:int):
    session = SessionLocal()
    person = session.query(Person).filter(person_id==Person.id).first()
    print(" data found" ,"id :",person.id, "name:",person.name,"email:", person.email)

# ans = get_all_users()
# for row in ans:
#     print("id :",row.id, "name:",row.name,"email:", row.email )
    
def update_person_by_id(person_id:int,name:str):
    session = SessionLocal()
    person=session.query(Person).filter(person_id==Person.id).first()
    
    person.name=name
    
    session.commit()
    session.refresh(person)
    session.close()

    

get_person_by_id(3)
update_person_by_id(3,"Rohit")
# get_person_by_id(3)


def delete_person(person_id:int):
    session = SessionLocal()
    person=session.query(Person).filter(person_id==Person.id).first()
    
    if person is None:
        print("person not found")
        session.close()
        return None
    
    
    session.delete(person)
    session.commit()
    session.close()
    return person


delete_person(2)


