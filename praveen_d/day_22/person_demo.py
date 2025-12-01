from sqlalchemy import create_engine,Column,Integer,String
from sqlalchemy.orm import sessionmaker,declarative_base

DATABASE_URL="mysql+pymysql://root:pass%40word1@localhost:3306/ust_db"
engine=create_engine(DATABASE_URL,echo=True)
SessionLocal=sessionmaker(bind=engine,autoflush=False,autocommit=False)

Base=declarative_base()
class Person(Base):
    __tablename__='persons'
    
    id=Column(Integer,primary_key=True,index=True)
    name=Column(String(50))
    email=Column(String(100),unique=True,nullable=False)
    
    
print("Creatinging tables in MYSQL DB")
Base.metadata.create_all(bind=engine)

def create_user(name:str,email:str):
    try:
        # create session 
        session=SessionLocal()
        
        # Create object(User)
        new_person=Person(name=name,email=email)
        
        # Add user to session
        session.add(new_person)
        
        # Commit session
        session.commit()
        
        # Refresh session
        session.refresh(new_person)
    except Exception as e:
        session.rollback()
        print("Exception",e)
        return None
    finally:
        session.close()
        
    return new_person

# create_user("Raju","raju2.com")

# create_user("vamshi","vamshi@varisu.com")
# create_user("Ajith","veeram@varisu.com")
# create_user("Surya","Mattran")
# print(create_user("Prakesh","pkash@gmail.com"))
def get_all_users():
    try:
        session=SessionLocal()
        person=session.query(Person).all()
        return person
        # return person
    except Exception as e:
        print("Exception",e)
    finally:
        session.close()
    return person

# print(get_all_users())
# print(result)

def get_person_by_id(person_id:int):
    try:
        session=SessionLocal()
        person=session.query(Person).filter(Person.id==person_id).first()
    except Exception as e:
        session.close()
    return person

result=get_person_by_id(1)
# print(f"{result.id}{result.name}{result.email}")

def update_person(id,name,email):
    session =SessionLocal()
    person=session.query(Person).filter(Person.id==id).first()
    
    if person is None:
        print("Person not found")
        session.close()
        return None
    person.name=name
    Person.email=email
    session.commit()
    session.refresh(person)
    session.close()
    return person

def delete_person(person_id:int):
    session =SessionLocal()
    person=session.query(Person).filter(Person.id==person_id).first()
    
    if person is None:
        print("Person not found")
        session.close()
        return None
    session.delete(person)
    session.commit()
    session.close()
    return person


update_person(1,"somu","somu@123")
# delete_person(10)